# app.py
import streamlit as st
import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from streamlit_app.calculator import ResourceCalculator # Import the class from calculator.py

st.set_page_config(
    layout="wide", 
    page_title="🚐 Smart EV Camper Resource Calculator",
    page_icon="🚐",
    initial_sidebar_state="expanded"
)

# --- DATA LOADING ---
@st.cache_data
def load_data():
    """Loads the lookup data from the JSON file."""
    try:
        with open('streamlit_app/lookup_data.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error("Fatal Error: `lookup_data.json` not found. Please ensure the file is in the same directory.")
        return None

LOOKUP_DATA = load_data()
if not LOOKUP_DATA:
    st.stop()

# --- PLOTLY VISUALIZATION FUNCTIONS ---
def create_consumption_pie_chart(results_breakdown, resource_type):
    """Creates a pie chart for energy or water consumption."""
    labels = []
    values = []
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F']
    
    if resource_type == 'energy':
        unit = 'kWh'
        key = 'energy_wh'
        divisor = 1000
    else: # water
        unit = 'gal'
        key = 'water_gal'
        divisor = 1

    for category, data in results_breakdown.items():
        if data[key] > 0: # Only include consumption, not production
            labels.append(category.title())
            values.append(data[key] / divisor)
    
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.4,
        marker=dict(colors=colors[:len(labels)], line=dict(color='#FFFFFF', width=2)),
        hovertemplate='<b>%{label}</b><br>%{value:.2f} ' + unit + '<br>%{percent}<extra></extra>',
        textinfo='label+percent',
        textfont_size=12
    )])
    fig.update_layout(
        title={
            'text': f"💧 {resource_type.title()} Consumption Breakdown" if resource_type == 'water' else f"⚡ {resource_type.title()} Consumption Breakdown",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2C3E50'}
        },
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
        margin=dict(t=60, b=60, l=20, r=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def create_tank_gauge(value, title, unit, is_waste_tank=False):
    """Creates a simplified half donut chart with visible values."""
    # Determine color and icon - Green for positive values, Red for negative
    if is_waste_tank:
        icon = "🚽" if "Black" in title else "🚿"
    else:
        icon = "🔋" if "Battery" in title else "💧"
    
    # Color based on positive/negative values
    if value >= 0:
        color = "#2ECC71"  # Green for positive values
    else:
        color = "#E74C3C"  # Red for negative values
    
    # Handle negative values by converting to absolute value for display
    display_value = abs(value)
    # Cap the display value at 100 for the chart
    chart_value = min(display_value, 100)
    
    # Create half donut chart
    fig = go.Figure()
    
    # Background arc (empty portion)
    fig.add_trace(go.Pie(
        values=[100],
        hole=0.7,
        marker=dict(colors=['#F8F9FA']),
        showlegend=False,
        hoverinfo='skip',
        textinfo='none'
    ))
    
    # Value arc (filled portion) - direction based on positive/negative
    direction = 'counterclockwise' if value <= 0 else 'clockwise'
    
    fig.add_trace(go.Pie(
        values=[chart_value, 100-chart_value],
        hole=0.7,
        marker=dict(colors=[color, 'rgba(0,0,0,0)']),
        showlegend=False,
        hoverinfo='skip',
        textinfo='none',
        rotation=1,  # Start from top middle (12 o'clock)
        direction=direction
    ))
    
    # Add text annotations - show original value with sign
    fig.add_annotation(
        text=f"<b>{value:.1f}{unit}</b>",
        x=0.5, y=0.4,
        font=dict(size=24, color='#2C3E50'),
        showarrow=False
    )
    
    fig.add_annotation(
        text=f"{icon} {title}",
        x=0.5, y=0.6,
        font=dict(size=14, color='#34495E'),
        showarrow=False
    )
    
    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_energy_bar_chart(summary):
    """Creates an enhanced bar chart comparing energy consumed vs. produced."""
    consumed = summary['total_consumption']['energy_kwh']
    produced = summary['total_production']['solar_energy_kwh']
    net = summary['net_consumption']['energy_kwh']
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['⚡ Consumption', '☀️ Solar Production', '📊 Net Usage'],
        y=[consumed, produced, net],
        marker_color=['#E74C3C', '#2ECC71', '#3498DB'],
        text=[f"{consumed:.2f} kWh", f"{produced:.2f} kWh", f"{net:.2f} kWh"],
        textposition='auto',
        textfont={'size': 14, 'color': 'white'},
        hovertemplate='<b>%{x}</b><br>%{y:.2f} kWh<extra></extra>'
    ))
    
    # Add a reference line at zero
    fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Zero Line")
    
    fig.update_layout(
        title={
            'text': "⚡ Energy Balance Overview",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2C3E50'}
        },
        yaxis_title="Energy (kWh)",
        yaxis={'title_font': {'size': 14}},
        xaxis={'title_font': {'size': 14}},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=40, l=40, r=40),
        height=400
    )
    return fig

def create_resource_efficiency_chart(breakdown):
    """Creates a horizontal bar chart showing resource efficiency by category."""
    categories = []
    energy_values = []
    water_values = []
    
    for category, data in breakdown.items():
        if data['energy_wh'] > 0 or data['water_gal'] > 0:
            categories.append(category.title())
            energy_values.append(data['energy_wh'] / 1000)  # Convert to kWh
            water_values.append(data['water_gal'])
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Energy Usage (kWh)", "Water Usage (gal)"),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Energy bars
    fig.add_trace(
        go.Bar(
            y=categories,
            x=energy_values,
            orientation='h',
            marker_color='#3498DB',
            name="Energy",
            text=[f"{val:.1f}" for val in energy_values],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>%{x:.2f} kWh<extra></extra>'
        ),
        row=1, col=1
    )
    
    # Water bars
    fig.add_trace(
        go.Bar(
            y=categories,
            x=water_values,
            orientation='h',
            marker_color='#1ABC9C',
            name="Water",
            text=[f"{val:.1f}" for val in water_values],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>%{x:.2f} gal<extra></extra>'
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        title={
            'text': "📊 Resource Usage by Category",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2C3E50'}
        },
        showlegend=False,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=40, l=120, r=40)
    )
    
    return fig

def create_daily_projection_chart(summary, trip_duration):
    """Creates a line chart showing daily resource projection over trip duration."""
    days = list(range(1, trip_duration + 1))
    daily_energy = summary['total_consumption']['energy_kwh'] / trip_duration
    daily_water = summary['total_consumption']['water_gal'] / trip_duration
    daily_solar = summary['total_production']['solar_energy_kwh'] / trip_duration
    
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Daily Energy Trend", "Daily Water Usage"),
        vertical_spacing=0.12
    )
    
    # Energy consumption and production
    fig.add_trace(
        go.Scatter(
            x=days,
            y=[daily_energy * day for day in days],
            mode='lines+markers',
            name='Energy Consumed',
            line=dict(color='#E74C3C', width=3),
            marker=dict(size=8)
        ),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=days,
            y=[daily_solar * day for day in days],
            mode='lines+markers',
            name='Solar Produced',
            line=dict(color='#2ECC71', width=3),
            marker=dict(size=8)
        ),
        row=1, col=1
    )
    
    # Water consumption
    fig.add_trace(
        go.Scatter(
            x=days,
            y=[daily_water * day for day in days],
            mode='lines+markers',
            name='Water Consumed',
            line=dict(color='#3498DB', width=3),
            marker=dict(size=8),
            fill='tonexty' if len(days) > 1 else None
        ),
        row=2, col=1
    )
    
    fig.update_layout(
        title={
            'text': "📈 Daily Resource Projection",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2C3E50'}
        },
        height=500,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=40, l=40, r=40)
    )
    
    fig.update_xaxes(title_text="Trip Day", row=2, col=1)
    fig.update_yaxes(title_text="Cumulative Energy (kWh)", row=1, col=1)
    fig.update_yaxes(title_text="Cumulative Water (gal)", row=2, col=1)
    
    return fig

def create_sustainability_metrics(summary):
    """Creates a metrics display for sustainability indicators."""
    consumed = summary['total_consumption']['energy_kwh']
    produced = summary['total_production']['solar_energy_kwh']
    
    # Calculate sustainability metrics
    energy_independence = min(100, (produced / consumed * 100)) if consumed > 0 else 100
    water_efficiency = summary['total_production']['generated_water_gal'] / summary['total_consumption']['water_gal'] * 100 if summary['total_consumption']['water_gal'] > 0 else 0
    
    # Create a radar chart for sustainability metrics
    categories = ['Energy Independence', 'Water Efficiency', 'Resource Optimization', 'Eco-Friendliness']
    values = [
        energy_independence,
        min(100, water_efficiency),
        75,  # Placeholder - could be calculated based on efficiency
        min(100, energy_independence * 0.8)  # Simplified eco-score
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Close the polygon
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(52, 152, 219, 0.2)',
        line=dict(color='#3498DB', width=3),
        marker=dict(size=8, color='#2980B9'),
        name='Sustainability Score'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            )
        ),
        title={
            'text': "🌱 Sustainability Metrics",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2C3E50'}
        },
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=40, l=40, r=40)
    )
    
    return fig

# --- CUSTOM CSS FOR ENHANCED STYLING ---
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    
    .stMetric {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #f1f3f4;
        border-radius: 4px 4px 0px 0px;
        color: #5f6368;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #1976d2;
        color: white;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 4px;
    }
    
    .stNumberInput > div > div {
        background-color: white;
        border-radius: 4px;
    }
    
    .stSlider > div > div {
        background-color: white;
        border-radius: 4px;
    }
    
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e1e5e9;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
        transition: all 0.3s cubic-bezier(.25,.8,.25,1);
    }
    
    div[data-testid="metric-container"]:hover {
        box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
    }
    
    .element-container:has(iframe[height="400"]) {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR FOR USER INPUTS ---
st.sidebar.markdown("""
<div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
            padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
    <h2 style="color: white; margin: 0; text-align: center;">⚙️ Trip Configuration</h2>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9; text-align: center; font-size: 0.9rem;">
        Customize your camper journey parameters
    </p>
</div>
""", unsafe_allow_html=True)

inputs = LOOKUP_DATA.get('inputs', {}).get('params', {})

# Trip Planning Section
st.sidebar.markdown("### 🗓️ Trip Planning")
user_type = st.sidebar.selectbox(
    "👤 User Profile",
    options=inputs.get('user_type', {}).get('options', ['Typical']),
    index=1, # Default to 'Typical'
    help="Select your camping experience level and resource usage pattern"
)

col1, col2 = st.sidebar.columns(2)
with col1:
    num_people = st.number_input(
        "👥 People",
        min_value=1,
        max_value=4,
        value=inputs.get('num_people', {}).get('value', 1),
        step=1
    )

with col2:
    trip_duration_days = st.number_input(
        "📅 Days",
        min_value=1,
        value=inputs.get('trip_duration_days', {}).get('value', 3),
        step=1
    )

hvac_runtime_hrs = st.sidebar.slider(
    "🌡️ HVAC Runtime (hrs/day)",
    min_value=0,
    max_value=24,
    value=inputs.get('hvac_runtime_hrs', {}).get('value', 12),
    step=1,
    help="Hours per day that heating/cooling system will be active"
)

relocation_count = st.sidebar.number_input(
    "🚚 Relocation Count",
    min_value=0,
    value=inputs.get('relocation_count', {}).get('value', 2),
    step=1,
    help="Number of times you'll move to different campsites"
)

# Environmental Conditions Section
st.sidebar.markdown("### 🌍 Environmental Conditions")
temperature = st.sidebar.selectbox(
    "🌡️ Ambient Temperature",
    options=inputs.get('temperature', {}).get('options', ['Hot']),
    index=0, # Default to 'Hot'
    help="Expected temperature range during your trip"
)

humidity = st.sidebar.selectbox(
    "💧 Ambient Humidity",
    options=inputs.get('humidity', {}).get('options', ['Comfortable']),
    index=1, # Default to 'Comfortable'
    help="Expected humidity levels (affects water generation from HVAC)"
)

sunlight = st.sidebar.selectbox(
    "☀️ Sunlight Exposure",
    options=inputs.get('sunlight', {}).get('options', ['Hi- Sunny']),
    index=0, # Default to 'Hi- Sunny'
    help="Expected sunlight conditions for solar panel efficiency"
)

# Add a calculation button and status
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔄 Calculation Status")
if st.sidebar.button("🔄 Recalculate", type="primary"):
    st.rerun()

# Add helpful tips
st.sidebar.markdown("### 💡 Quick Tips")
st.sidebar.info("""
**🔋 Energy Saving:**
- Reduce HVAC runtime during mild weather
- Use LED lighting efficiently

**💧 Water Conservation:**
- Take shorter showers
- Reuse grey water when possible

**☀️ Solar Optimization:**
- Park in sunny locations
- Keep panels clean
""")

# Display current configuration summary
st.sidebar.markdown("### 📋 Current Config")
config_summary = f"""
- **Profile:** {user_type}
- **Duration:** {trip_duration_days} days
- **People:** {num_people}
- **HVAC:** {hvac_runtime_hrs}hrs/day
- **Relocations:** {relocation_count}
- **Weather:** {temperature}, {humidity}
- **Sun:** {sunlight}
"""
st.sidebar.markdown(config_summary)

# --- MAIN PAGE ---
st.title("🚐 Smart EV Camper Resource Calculator")
st.markdown("""
<div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
            padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
    <h3 style="color: white; margin: 0;">🎯 Plan Your Perfect Off-Grid Adventure</h3>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
        Configure your trip parameters in the sidebar to get detailed resource consumption analysis, 
        sustainability metrics, and actionable insights for your smart EV camper journey.
    </p>
</div>
""", unsafe_allow_html=True)

# --- PERFORM CALCULATION ---
user_inputs = {
    'user_type': user_type,
    'num_people': num_people,
    'trip_duration_days': trip_duration_days,
    'hvac_runtime_hrs': hvac_runtime_hrs,
    'relocation_count': relocation_count,
    'temperature': temperature,
    'humidity': humidity,
    'sunlight': sunlight
}

calculator = ResourceCalculator(lookup_data=LOOKUP_DATA, **user_inputs)
results = calculator.calculate()

summary = results['summary']
breakdown = results['breakdown']
tanks = summary['final_tank_levels']

# --- DISPLAY RESULTS IN TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Executive Dashboard", "📈 Analytics & Trends", "🔢 Detailed Summary", "📝 Raw Data"])

with tab1:
    # Key Performance Indicators
    st.markdown("### 🎯 Trip Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        net_energy = summary['net_consumption']['energy_kwh']
        energy_status = "✅ Surplus" if net_energy < 0 else "⚠️ Deficit" if net_energy > 5 else "✅ Balanced"
        st.metric("Net Energy Usage", f"{net_energy:.1f} kWh", energy_status)
    
    with col2:
        fresh_remaining = tanks['fresh_water_percent']
        water_status = "🟢 Good" if fresh_remaining > 30 else "🟡 Low" if fresh_remaining > 10 else "🔴 Critical"
        st.metric("Fresh Water Remaining", f"{fresh_remaining:.1f}%", water_status)
    
    with col3:
        dump_trips = summary['waste_summary']['required_dump_trips']
        st.metric("Required Dump Trips", f"{dump_trips}", "📍 Plan accordingly")
    
    with col4:
        energy_independence = min(100, (summary['total_production']['solar_energy_kwh'] / summary['total_consumption']['energy_kwh'] * 100)) if summary['total_consumption']['energy_kwh'] > 0 else 100
        st.metric("Energy Independence", f"{energy_independence:.0f}%", "☀️ Solar powered")
    
    st.divider()
    
    # Resource Consumption Overview
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_consumption_pie_chart(breakdown, 'energy'), use_container_width=True)
    with col2:
        st.plotly_chart(create_consumption_pie_chart(breakdown, 'water'), use_container_width=True)
        
    st.divider()
    
    # Tank Status Dashboard
    st.markdown("### 🔋 System Status")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.plotly_chart(create_tank_gauge(tanks['battery_percent'], "Battery", "%"), use_container_width=True)
    with col2:
        st.plotly_chart(create_tank_gauge(tanks['fresh_water_percent'], "Fresh Water", "%"), use_container_width=True)
    with col3:
        st.plotly_chart(create_tank_gauge(tanks['grey_water_percent'], "Grey Water", "%", is_waste_tank=True), use_container_width=True)
    with col4:
        st.plotly_chart(create_tank_gauge(tanks['black_water_percent'], "Black Water", "%", is_waste_tank=True), use_container_width=True)
        
    st.divider()
    
    # Energy Balance
    st.plotly_chart(create_energy_bar_chart(summary), use_container_width=True)

with tab2:
    st.markdown("### 📊 Resource Analysis & Projections")
    
    # Resource efficiency comparison
    st.plotly_chart(create_resource_efficiency_chart(breakdown), use_container_width=True)
    
    st.divider()
    
    # Daily projections and sustainability metrics
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_daily_projection_chart(summary, trip_duration_days), use_container_width=True)
    with col2:
        st.plotly_chart(create_sustainability_metrics(summary), use_container_width=True)
    
    st.divider()
    
    # Additional insights
    st.markdown("### 💡 Smart Insights")
    
    # Calculate some insights
    energy_ratio = summary['total_production']['solar_energy_kwh'] / summary['total_consumption']['energy_kwh'] if summary['total_consumption']['energy_kwh'] > 0 else 0
    water_generation = summary['total_production']['generated_water_gal']
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        if energy_ratio >= 1.0:
            st.success("🌟 **Energy Positive Trip!** Your solar panels will generate more energy than you consume.")
        elif energy_ratio >= 0.8:
            st.info("⚡ **Nearly Self-Sufficient!** Consider reducing high-energy activities or adding solar capacity.")
        else:
            st.warning("🔋 **Energy Deficit Expected.** Plan for charging stops or reduce consumption.")
    
    with insight_col2:
        if water_generation > 5:
            st.success(f"💧 **HVAC Water Recovery:** Your system will generate {water_generation:.1f} gallons of water from humidity!")
        elif tanks['fresh_water_percent'] < 20:
            st.warning("💧 **Low Water Alert:** Consider water conservation or plan refill stops.")
        else:
            st.info("💧 **Water Usage:** Monitor consumption and consider conservation practices.")
    
    with insight_col3:
        if dump_trips <= 1:
            st.success("🚽 **Minimal Waste Management:** Low maintenance trip with minimal dump requirements.")
        else:
            st.info(f"🚽 **Waste Planning:** Schedule {dump_trips} dump stops during your trip.")

with tab3:
    st.markdown("### 🔢 Detailed Resource Summary")

    # Enhanced metrics display
    st.markdown("#### 📊 Net Resource Impact")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        net_energy = summary['net_consumption']['energy_kwh']
        delta_color = "normal" if abs(net_energy) < 2 else "inverse"
        st.metric(
            "Net Energy Consumption", 
            f"{net_energy:.2f} kWh",
            delta=f"{'Surplus' if net_energy < 0 else 'Deficit'}"
        )
    
    with col2:
        st.metric(
            "Fresh Water Remaining", 
            f"{tanks['fresh_water_gal']:.1f} gal",
            delta=f"{tanks['fresh_water_percent']:.1f}% capacity"
        )
    
    with col3:
        st.metric(
            "Required Dump Trips", 
            f"{summary['waste_summary']['required_dump_trips']}",
            delta="Plan route accordingly"
        )
    
    with col4:
        solar_efficiency = (summary['total_production']['solar_energy_kwh'] / summary['total_consumption']['energy_kwh'] * 100) if summary['total_consumption']['energy_kwh'] > 0 else 0
        st.metric(
            "Solar Efficiency", 
            f"{min(100, solar_efficiency):.0f}%",
            delta="Energy independence"
        )
    
    st.divider()
    
    # Enhanced breakdown table
    st.markdown("#### 📋 Detailed Consumption Breakdown")
    
    # Create enhanced DataFrame
    df_data = []
    for cat, values in breakdown.items():
        # Calculate percentages
        energy_pct = (values['energy_wh'] / sum(v['energy_wh'] for v in breakdown.values() if v['energy_wh'] > 0)) * 100 if values['energy_wh'] > 0 else 0
        water_pct = (values['water_gal'] / sum(v['water_gal'] for v in breakdown.values() if v['water_gal'] > 0)) * 100 if values['water_gal'] > 0 else 0
        
        df_data.append({
            "Category": cat.title(),
            "Energy (kWh)": values['energy_wh'] / 1000,
            "Energy %": energy_pct,
            "Water (gal)": values['water_gal'],
            "Water %": water_pct,
            "Daily Energy (kWh)": (values['energy_wh'] / 1000) / trip_duration_days,
            "Daily Water (gal)": values['water_gal'] / trip_duration_days
        })
    
    df = pd.DataFrame(df_data)
    
    # Style the dataframe
    styled_df = df.style.format({
        "Energy (kWh)": "{:.2f}",
        "Energy %": "{:.1f}%",
        "Water (gal)": "{:.2f}",
        "Water %": "{:.1f}%",
        "Daily Energy (kWh)": "{:.2f}",
        "Daily Water (gal)": "{:.2f}"
    }).background_gradient(subset=['Energy %', 'Water %'], cmap='RdYlGn_r')
    
    st.dataframe(styled_df, use_container_width=True)
    
    st.divider()
    
    # Production vs Consumption Summary
    st.markdown("#### ⚖️ Production vs Consumption Analysis")
    
    prod_cons_col1, prod_cons_col2 = st.columns(2)
    
    with prod_cons_col1:
        st.markdown("**🔋 Energy Balance**")
        energy_data = {
            "Type": ["Total Consumption", "Solar Production", "Net Balance"],
            "Value (kWh)": [
                summary['total_consumption']['energy_kwh'],
                summary['total_production']['solar_energy_kwh'],
                summary['net_consumption']['energy_kwh']
            ],
            "Status": [
                "🔴 Outgoing",
                "🟢 Incoming", 
                "🟡 Balance" if abs(summary['net_consumption']['energy_kwh']) < 2 else "🔴 Deficit" if summary['net_consumption']['energy_kwh'] > 0 else "🟢 Surplus"
            ]
        }
        st.dataframe(pd.DataFrame(energy_data), use_container_width=True)
    
    with prod_cons_col2:
        st.markdown("**💧 Water Balance**")
        water_data = {
            "Type": ["Total Consumption", "HVAC Generation", "Net Usage"],
            "Value (gal)": [
                summary['total_consumption']['water_gal'],
                summary['total_production']['generated_water_gal'],
                summary['total_consumption']['water_gal'] - summary['total_production']['generated_water_gal']
            ],
            "Status": [
                "🔴 Outgoing",
                "🟢 Incoming",
                "🔴 Net Usage"
            ]
        }
        st.dataframe(pd.DataFrame(water_data), use_container_width=True)

with tab4:
    st.markdown("### 📝 Raw Calculation Data")
    st.markdown("*Complete JSON output from the resource calculator for debugging and analysis*")
    
    # Add expandable sections for better organization
    with st.expander("🔧 Trip Configuration"):
        st.json(results['inputs'])
    
    with st.expander("📊 Resource Breakdown"):
        st.json(results['breakdown'])
    
    with st.expander("📈 Summary Results"):
        st.json(results['summary'])
    
    with st.expander("🔍 Complete Raw Data"):
        st.json(results)