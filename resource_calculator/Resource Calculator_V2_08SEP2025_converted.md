# Excel to Markdown Conversion
**Source File:** Resource Calculator_V2_08SEP2025.xlsx
**Generated:** 2025-09-10 21:47:41
**Total Sheets:** 24

## Sheet: Summary

### CSV Data
```csv
Note: Updated 9/2/2025 to reflect feature set detailed in document 1764-D009 Product Breakdown Structure,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17
Key,,,TRIP DESIGNER,,,,System/Activity,Cycles,Energy [Wh],Energy [kWh],% Energy Consumption,Water [gal],% Water Consumption,,,,
Input Fields,,,User type,Typical,,,Living (8),3,91145.78899,91.14578899,0.6991273704,4.982142857,0.08057919982,,Waste Monitor,,
Output Fields,,,Number of people (1-4),1,,,Cooking (10),6,14833.775,14.833775,0.1137814289,12.75,0.2062134361,,Grey water produced [gal],46.82914286,Dump Trip Required
Driven By User Matrix,,,Trip duration [days],3,,,Shower,3,2573.7,2.5737,0.01974138502,36,0.5822497019,,Black water produced [gal],16.125,Dump Trip Required
"Formulas, Use Caution",,,Number of rainy days (25),0,,,Toilet,15,540.24,0.54024,0.004143872962,5.625,0.09097651593,,Dumpstation Trip Cycles,0.0,
"Note, See Appendix ",(#),,"HVAC/Water Gen (2, 25) [hrs/day]",12,,,Laundry,0.6,207.6923077,0.2076923077,0.001593089253,2.472,0.0399811462,,Grey water tank level [gal],46.82914286,Level remaining
,,,Temperature (3),Hot,,,Actuation (11),6,298.2804,0.2982804,0.002287938851,0,0,,Black water tank level [gal],16.125,Level remaining
,,,Humidity,Comfortable,,,"Non-Potable Water (12, 25)",1,0,0,0,0,0,,,,
,,,Sunlight,Hi- Sunny,,,Grey/blackwater dump (13),0,0.05,5e-05,3.835214869e-07,0,0,,,,
,,,Relocation count (24),2,,,HVAC & Water Generator Output (4),,20771.26531,20.77126531,0.1593245311,0,,,,,
,,,,,,,Rainwater capture (14),,-,-,,0,,,,,
,,,TRAILER SPECIFICATIONS,,,,Total Consumption ,,130370.792,130.370792,,61.82914286,,,,,
,,,Battery capacity (1) [kWh],100,,,Energy Produced (Solar),,-85205.59038,-85.20559038,,,,,,,
,,,Solar capcity [kW],5.25,,,NET RESOURCE CONSUMPTION,,45165.20162,45.16520162,,61.82914286,,,,,
,,,No. of solar panels,35,,,,,,Dead Battery,,Out of Water,,,,,
,,,Freshwater capacity [gal] ,100,,,,,,,,,,,,,
,,,Blackwater capacity [gal],45,,,,,,,,,,,,,
,,,Greywater capacity [gal],50,,,,,,,,,,,,,

```

### Formulas Used

- **I3:** `=1*E5`
- **J3:** `=Living!I6*I3`
- **K3:** `=J3/1000`
- **L3:** `=K3/$K$13`
- **M3:** `=Living!I7*I3`
- **N3:** `=M3/$M$13`
- **I4:** `='User Matrix'!G26*E5`
- **J4:** `=Cooking!I6*I4`
- **K4:** `=J4/1000`
- **L4:** `=K4/$K$13`
- **M4:** `=Cooking!I7*I4`
- **N4:** `=M4/$M$13`
- **Q4:** `='Lookup Tables'!C31`
- **I5:** `=E4*E5*'User Matrix'!G43`
- **J5:** `=Shower!J6*I5`
- **K5:** `=J5/1000`
- **L5:** `=K5/$K$13`
- **M5:** `=Shower!J7*I5`
- **N5:** `=M5/$M$13`
- **Q5:** `='Lookup Tables'!D31`
- **I6:** `=E4*E5*'User Matrix'!G35`
- **J6:** `=Toilet!I6*I6`
- **K6:** `=J6/1000`
- **L6:** `=K6/$K$13`
- **M6:** `=Toilet!I7*I6`
- **N6:** `=M6/$M$13`
- **Q6:** `=ROUNDDOWN( IF(Q4/E19 > Q5/E18, Q4/E19, Q5/E18),0)`
- **I7:** `=E5*E4*'User Matrix'!G51`
- **J7:** `=I7*Laundry!C21`
- **K7:** `=J7/1000`
- **L7:** `=K7/$K$13`
- **M7:** `=Laundry!J7*I7`
- **N7:** `=M7/$M$13`
- **Q7:** `=IF(Q4-(E19*Q6)<0, 0, Q4-(E19*Q6))`
- **I8:** `=(2+(E11*2)+(IF(Q6>1, Q6*2, 0)))`
- **J8:** `=Actuation!H7*I8`
- **K8:** `=J8/1000`
- **L8:** `=K8/$K$13`
- **N8:** `=M8/$M$13`
- **Q8:** `=IF(Q5-(E18*Q6)<0, 0, Q5-(E18*Q6))`
- **J9:** `='Non-Potable Water'!J6`
- **K9:** `=J9/1000`
- **L9:** `=K9/$K$13`
- **M9:** `='Non-Potable Water'!J7`
- **N9:** `=M9/$M$13`
- **I10:** `=Q6`
- **J10:** `=Dumping!I7`
- **K10:** `=J10/1000`
- **L10:** `=K10/$K$13`
- **N10:** `=M10/$M$13`
- **J11:** `=VLOOKUP(E8, 'Lookup Tables'!B4:C6, 2, FALSE)*E5`
- **K11:** `=J11/1000`
- **L11:** `=K11/$K$13`
- **M11:** `=((if(E7>12,12,E7)*INDEX('Lookup Tables'!$C$13:$E$15, MATCH(E9, 'Lookup Tables'!B13:B15, 0), MATCH(E8, 'Lookup Tables'!C12:E12, 0)))+(if(E7>12,E7-12,0)*INDEX('Lookup Tables'!$C$17:$E$19, MATCH(E9, 'Lookup Tables'!$B$17:$B$19, 0), MATCH(E8, 'Lookup Tables'!$C$16:$E$16, 0)))*E5)*-1`
- **M12:** `='Lookup Tables'!A38*E6*-1`
- **J13:** `=SUM(J3:J12)`
- **K13:** `=J13/1000`
- **M13:** `=SUM(M3:M10)`
- **J14:** `=-1*E5*(INDEX(Solar!S4:V7,MATCH(E8,Solar!S4:S7,0),MATCH(E9,Solar!S4:V4,0))*VLOOKUP(E10, Solar!X5:Y7, 2, 0))`
- **K14:** `=J14/1000`
- **E15:** `=Solar!N17/1000`
- **J15:** `=sum(J13:J14)`
- **K15:** `=J15/1000`
- **M15:** `=SUM(M3:M12)`

---

## Sheet: User Matrix

### CSV Data
```csv
Unnamed: 0,This sheet defines users and use-cases. Input fields (in yellow) should be filled or informed by AC Future,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8
,Current use selcted in Summary,Typical,,,,,,
,,User (7),,,,,,
,Activity,Glamper,Typical,Expert,Unit,Selected Outputs,Linked,Notes
Living,Audio Amplifier,240,120,10,mins/day,120,True,
,Television,120,60,30,mins/day,60,True,
,Party lighting window perimeter,6,2.5,1,hrs/day,2.5,False,
,Smart Glass (Transparent Display),10,6,3,hrs/day,6,False,
,Refrigerator,24,24,24,[hrs/day],24,,
,Starlink Satalite Internet,1440,1440,1440,[mins/day],1440,True,
,Lighting,450,300,240,[mins/day],300,True,
,Tire and Temp Sensors,24,24,24,[hrs/day],24,False,
,Various sensors and controllers,24,24,24,[hrs/day],24,False,
,Security Cameras,24,24,24,[hrs/day],24,True,
,Consumer Electronics - living,24,16,10,[hrs/day],16,True,
,Refrigerator - ice maker water,0.29,0.29,0.29,[gal/day],0.29,False,
,Exterior camp lights,4,2,1,hrs/day,2,False,
,Exterior porch lighting,4,2,1,hrs/day,2,False,
,Smart Key Lighting,8,4,2,cycles,4,False,
,SmartTint,12,10,8,hrs/day,10,False,
,Misc. cleaning - hand washing,0.75,0.625,0.5,gal/day,0.625,True,
,Drinking water,0.5,0.75,1,gal/day,0.75,True,
Cooking,Stove top,20,15,10,mins/meal,15,True,"One burner on ""high"""
,Stove top - No. of burners used,2,1,1,burners/meal,1,False,"Burners on ""high"""
,Range Hood,22,17,12,mins/meal,17,False,
,Meals prepared each day,3,2,1,meals,2,True,
,Microwave,5,3.5,2,mins/meal,3.5,True,
,Dishwasher,1,0.5,0.33,Cycles/meal,0.5,True,
,Garbage disposal,1,0.5,0.1666666667,mins/meal,0.5,True,
,Consumer Electronics - cooking,8,5,3,mins/meal,5,True,Assumes 2gpm faucet
,Tankless water heater - cooking,4,3,1,mins/meal,3,True,
,Water pump - cooking,5.585,3.625,1.4125,mins/meal,3.625,True,
,Dishwasher - water,3.17,1.25,0.825,gal/meal,1.25,True,"DW's ""intensive mode"" uses 3.17 gal/cycle. ""Normal"" mode uses 2.5 gal/cycle "
,Kitchen faucet - water,2,1.5,0.5,gal/meal,1.5,True,
Toilet,Toilet system,7,5,3,cycles/day/person,5,True,Daily toilet use per person
,Water pump - toilet system/activity,1.13,1.05,0.967,min/cycle,1.05,True,3.7 GPM 
,Vent fan - toilet,5,4,2.5,min/cycle,4,True,
,Tankless water heater,0.33,0.25,0.167,min/cycle,0.25,True,
,Toilet (gravity),0.4,0.4,0.4,gal/cycle,0.4,False,
,toilet (incinerator),,,,,,False,
,,,,,,,False,
,Sink - water,0.495,0.375,0.2505,gal/cycle,0.375,True,Based on Average 1.5 GPM pump
Shower,Shower system,1.5,1,0.5,cycles/day/person,1,True,
,Solar heated water,0,0,0,min/cycle,,False,How much time uses solar heated water. Up to max 4mins w/ 8gal cap & assumed 2gpm showerhead.
,Electric shower,10,6,3,min/cycle,6,True,Total shower duration
,Water pump,10,6,3,min/cycle,6,False,Set equal to shower duration in Shower sheet
,Vent fan,20,15,10,min/cycle,15,True,
,Consumer Electronics,10,5,2,min/cycle,5,True,
,Shower recirculation,0,0,0,percentage of total shower duration,,True,
,Electric shower - water,20,12,6,gal/cycle,12,True,"This assumes no water recirculation. Maybe we should assume some baseline water recirc amount to limit total water used
Calcs done using 1gpm for 5 min for expert, 1.2gpm for 10 min for typical, and 1.5gpm for 15 min for glamper"
Laundry,Laundry system,0.3333333333,0.2,0.1428571429,cycles/day/person,0.2,True,
,Washer dryer combo,346.15,346.15,346.15,energy/cycle [Wh],346.15,False,
,Tankless water heater,30,30,30,min/cycle,0.25,False,
,Water pump,30,30,30,min/cycle,6,False,
,Washer dryer combo,20.6,20.6,20.6,gal/cycle,346.15,False,
Actuation,Actuation system,,,,cycles/day,,False,
,Actuators,30,30,30,sec/cycle,30,False,
Dumping,Dump frequency,,,,,,False,Should be highest for Glampers and lowest for Experts
,Dump valves,2,2,2,min/cycle,2,False,
,Grey water pump,2,2,2,min/cycle,2,False,
,Macerating pump,7.69,7.69,7.69,min/cycle,7.69,False,
HVAC,Duty cycle when HOT or COLD,0.8835,0.589,0.2325,percentage,0.589,True,Calculated based on existing MrCool DIY Minisplit (15)
,Duty cycle when TEMPERATE,0.3565,0.1395,0.062,percentage,0.1395,,Calculated based on existing MrCool DIY Minisplit (15)
Non-Potable Water,Off-grid local source water collection,0,20,50,gallons,20,,
,Pressurised grey-water use,0,5,15,gallons,5,,

```

### Formulas Used

- **C2:** `=Summary!E3`
- **G5:** `=INDEX($C$5:$E$62, MATCH(B5, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G6:** `=INDEX($C$5:$E$62, MATCH(B6, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G7:** `=INDEX($C$5:$E$62, MATCH(B7, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G8:** `=INDEX($C$5:$E$62, MATCH(B8, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G9:** `=INDEX($C$5:$E$62, MATCH(B9, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C10:** `=24*60`
- **D10:** `=24*60`
- **E10:** `=24*60`
- **G10:** `=INDEX($C$5:$E$62, MATCH(B10, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C11:** `=60*7.5`
- **D11:** `=60*5`
- **E11:** `=60*4`
- **G11:** `=INDEX($C$5:$E$62, MATCH(B11, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G12:** `=INDEX($C$5:$E$62, MATCH(B12, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G13:** `=INDEX($C$5:$E$62, MATCH(B13, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G14:** `=INDEX($C$5:$E$62, MATCH(B14, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G15:** `=INDEX($C$5:$E$62, MATCH(B15, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G16:** `=INDEX($C$5:$E$62, MATCH(B16, $B$5:$B$62, 0), MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G17:** `=INDEX($C$5:$E$62, MATCH(B17, $B$5:$B$62, 0), MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G18:** `=INDEX($C$5:$E$62, MATCH(B18, $B$5:$B$62, 0), MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G19:** `=INDEX($C$5:$E$62, MATCH(B19, $B$5:$B$62, 0), MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G20:** `=INDEX($C$5:$E$62, MATCH(B20, $B$5:$B$62, 0), MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G21:** `=INDEX($C$5:$E$62, MATCH(B21, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G22:** `=INDEX($C$5:$E$62, MATCH(B22, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G23:** `=INDEX($C$5:$E$62, MATCH(B23, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G24:** `=INDEX($C$5:$E$62, MATCH(B24, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G25:** `=INDEX($C$5:$E$62, MATCH(B25, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G26:** `=INDEX($C$5:$E$62, MATCH(B26, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G27:** `=INDEX($C$5:$E$62, MATCH(B27, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G28:** `=INDEX($C$5:$E$62, MATCH(B28, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **E29:** `=1/6`
- **G29:** `=INDEX($C$5:$E$62, MATCH(B29, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G30:** `=INDEX($C$5:$E$62, MATCH(B30, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C31:** `=C34*2`
- **D31:** `=D34*2`
- **E31:** `=E34*2`
- **G31:** `=INDEX($C$5:$E$62, MATCH(B31, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C32:** `=C31+(C33/2)`
- **D32:** `=D31+(D33/2)`
- **E32:** `=E31+(E33/2)`
- **G32:** `=INDEX($C$5:$E$62, MATCH(B32, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C33:** `=3.17*C28`
- **D33:** `=2.5*D28`
- **E33:** `=2.5*E28`
- **G33:** `=INDEX($C$5:$E$62, MATCH(B33, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G34:** `=INDEX($C$5:$E$62, MATCH(B34, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G35:** `=INDEX($C$5:$E$62, MATCH(B35, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C36:** `=C39/0.5+C38`
- **D36:** `=D39/0.5+D38`
- **E36:** `=E39/0.5+E38`
- **G36:** `=INDEX($C$5:$E$62, MATCH(B36, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G37:** `=INDEX($C$5:$E$62, MATCH(B37, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G38:** `=INDEX($C$5:$E$62, MATCH(B38, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G39:** `=INDEX($C$5:$E$62, MATCH(B39, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G40:** `=INDEX($C$5:$E$62, MATCH(B40, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C42:** `=C38*1.5`
- **D42:** `=D38*1.5`
- **E42:** `=E38*1.5`
- **G42:** `=INDEX($C$5:$E$62, MATCH(B42, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G43:** `=INDEX($C$5:$E$62, MATCH(B43, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G45:** `=INDEX($C$5:$E$62, MATCH(B45, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C46:** `=C45`
- **D46:** `=D45`
- **E46:** `=E45`
- **G46:** `=INDEX($C$5:$E$62, MATCH(B46, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G47:** `=INDEX($C$5:$E$62, MATCH(B47, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G48:** `=INDEX($C$5:$E$62, MATCH(B48, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C50:** `=(2*C45)*(1-C49)`
- **D50:** `=(2*D45)*(1-D49)`
- **E50:** `=(2*E45)*(1-E49)`
- **G50:** `=INDEX($C$5:$E$62, MATCH(B50, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C51:** `=1/3`
- **D51:** `=1/5`
- **E51:** `=1/7`
- **G51:** `=INDEX($C$5:$E$62, MATCH(B51, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G52:** `=INDEX($C$5:$E$62, MATCH(B52, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G53:** `=INDEX($C$5:$E$62, MATCH(B53, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G54:** `=INDEX($C$5:$E$62, MATCH(B54, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G55:** `=INDEX($C$5:$E$62, MATCH(B55, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G56:** `=INDEX($C$5:$E$62, MATCH(B56, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G57:** `=INDEX($C$5:$E$62, MATCH(B57, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G58:** `=INDEX($C$5:$E$62, MATCH(B58, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G59:** `=INDEX($C$5:$E$62, MATCH(B59, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G60:** `=INDEX($C$5:$E$62, MATCH(B60, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G61:** `=INDEX($C$5:$E$62, MATCH(B61, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C62:** `=57%*1.55`
- **D62:** `=38%*1.55`
- **E62:** `=15%*1.55`
- **G62:** `=INDEX($C$5:$E$62, MATCH(B62, $B$5:$B$62, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **C63:** `=23%*1.55`
- **D63:** `=9%*1.55`
- **E63:** `=4%*1.55`
- **G63:** `=INDEX($C$5:$E$63, MATCH(B63, $B$5:$B$63, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G64:** `=INDEX($C$5:$E$67, MATCH(B64, $B$5:$B$67, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`
- **G65:** `=INDEX($C$5:$E$67, MATCH(B65, $B$5:$B$67, 0),MATCH(Summary!$E$3, $C$4:$E$4, 0))`

---

## Sheet: Living

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
System Inputs,,,,,,,,System Outputs,,,,,,,,,,,Sheet Key,
Value,Unit,Description,,,,,,Value,Unit,Description,,,Used for,,,,,,Input field,
1,-,Factor of safety applied to total energy required,,,,,,242.5803653,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field,
24,hr / day,Max operation time / day,,,,,,30381.92966,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,,
1,cycles / day,n,,,,,,30381.92966,Wh,Total energy / day w/o factor of safety applied,,,,,,,,,,
1440,min,Max single cycle duration,,,,,,1.660714286,Gal,Total water / day w/o factor of safety applied,,,-,,,,,,,
Typical,User,From Summary Selection,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations,
Component,Make,Model,Water Used (gal/cycle),Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget,Water Used per Day (Gal)
Audio Amplifier,Pioneer,GM-E3604,,12,1,6,10,1,1,7200,120,2,2,22,12,72,264,144,0.01342903511,0
Television,Samsung,QN55LS03FAF / QN55LS03FAFXZA,,120,0,0.7,0,2,1,7200,60,1,1,22,0,168,0,168,0.00552960269,0
Surround Sound,Sonus ,Ultimate Immersive Set,,120,0.1316666667,0.625,2.75,1,1,0,0,2.5,2.5,21.5,15.8,75,339.7,187.5,0.01735241987,0
Refrigerator,Samsung,RF18A5101SG / RF18A5101SG/AA,0.2857142857,120,0.5136986301,0.5136986301,0.5136986301,1,1,86400,1440,24,24,0,61.64383562,61.64383562,0,1479.452055,0.04869513132,0.2857142857
Satellite Internet,Starlink,Mini,,120,0,0.25,0,0,1,0,1440,24,24,0,0,0,0,0,0,0
Satellite Internet,DC Power supply,DC-DC PSU,,12,0,2.5,0,1,1,0,1440,24,24,0,0,30,0,720,0.02369829724,0
Lighting,estimate,estimate,,12,0,12,0,1,1,0,300,5,5,0,0,144,0,720,0.02369829724,0
Tire Pressure,BTI,TPMS CAN System,,24,0,0.4,0,1,1,0,0,0,24,0,0,9.6,0,230.4,0.007583455118,0
"Various sensors and controllers: 
- tank level sensors, module and panel
- sensor multiplexor
- tablet UI
- solar water pressure sensor
- inverters
- hall sensors
- LAN switch
- DCDC",estimate,,,12,5,0,0,1,1,0,0,24,24,24,60,0,1440,0,0.04739659449,0
Camera system,Continental,ProViu360,,12,0,2,0,1,1,0,0,24,24,0,0,24,0,576,0.0189586378,0
Consumer electronics,estimate,"phone & laptop chargers, other misc.",,120,0,0.5,0,1,1,0,0,16,16,0,0,60,0,960,0.03159772966,0
Misc. cleaning,estimate,estimate,0.625,,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0.625
Drinking water tap,estimate,estimate,0.75,,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0.75
Solar hot water heater glycol pump (P4),Bayite,BYT-7A006,,12,0,0.7,0,1,1,0,0,10,10,0,0,8.4,0,84,0.002764801345,0
Water pump,SHURflo,4048-153-E75 / 4048-153-A75,,12,0,8.5,0,1,1,0,0.8303571429,0.01383928571,0.01383928571,0,0,102,0,1.411607143,4.646206342e-05,0
UV Water System,Viqua,VT4,,12,0,1.8,0,1,1,0,0,24,24,0,0,21.6,0,518.4,0.01706277402,0
Shower control keypad,CZone,Landscape 80-911-0162-00 & Portrait 80-911-0163-00,,12,0.0018,0,0,1,1,0,0,0,24,0,0.0216,0,0,0,0,0
Tablet UI,Samsung,Galaxy Tab S10+,,12,0,0.4166666667,0,1,1,0,0,24,24,0,0,5,0,120,0.003949716207,0
SmartTint (19),AC Power Supply,H-100,,120,0,0.8333333333,0,0,1,0,0,10,10,0,0,0,0,0,0,0
SmartTint (20),DC Power Supply,12 Volt DC Adapter,,12,0,2.5,0,7,1,0,0,10,10,0,0,210,0,2100,0.06912003363,0
Exterior Camp Lights,Optronics LED,BUL78CB,,12,0,0.054,0,6,1,0,0,2,2,0,0,3.888,0,7.776,0.0002559416102,0
Ext Porch Lighting,Diamond/etrailer.com,DG52526PB,,12,0,0.14,0,1,1,0,0,2,2,0,0,1.68,0,3.36,0.0001105920538,0
Motion Activated Storage lights,RECPRO,RP-1981,,12,0,0.325,0,2,1,0,5,0.08333333333,0.08333333333,0,0,7.8,0,0.65,2.139429612e-05,0
Exterior Strip Lighting,ColorBright,CB-RGBW-24V-98FT,,24,0,23.68333333,0,0,0,0,0,0,0,0,0,0,0,0,0,0
LAN Switch PSU,Mean Well,MDR-60-24,,120,0,0.25,0,2,1,0,0,24,24,0,0,60,0,1440,0.04739659449,0
Secure Gateway,Continental ,Gateway,,12,0.416,0.8333333333,0,1,1,0,0,24,0,24,4.992,10,119.808,0,0.003943396662,0
Telematics T-Box,Continental ,estimate,,12,0.25,1.25,0,1,1,0,0,24,0,24,3,15,72,0,0.002369829724,0
4G LTE Antenna,Wineguard,Rangepro WB-1035,,12,0.75,0,0,1,1,0,0,24,0,24,9,0,216,0,0.007109489173,0
Air Purifier,PuroAir,240 Hepa,,120,0,0.375,0,1,1,0,0,24,24,0,0,45,0,1080,0.03554744587,0
AI Compute,Nvidia,Orin,,12,1.25,20.83333333,41.66666667,2,1,0,0,24,12,12,30,500,360,6000,0.209334959,0
Party lighting window perimeter,Flexfire,RGB LED Strip,,12,0,18.33333333,110,1,1,0,0,24,12,12,0,220,0,2640,0.08689375656,0
Smart Glass,LG,"Transparent Display (T-OLED) 30""",,120,0.8333333333,0.7166666667,4.583333333,1,1,0,0,6,12,12,100,86,1200,1032,0.07346472146,0
Smart Key Lighting,estimate,Passive Keyless Entry (PKE),,12,0.004,8,0,1,4,30,0.5,0.008333333333,0.03333333333,12,0.048,96,0.576,3.2,0.0001242844033,0
Home assistant server & central control computer,estimate,needs component selection,,12,0.004,12.5,0,1,1,0,0,24,24,12,0.048,150,0.576,3600,0.1185104449,0
HVAC Controller,New Eagle,Raptor,,12,0.01,7.855,15.7,1,1,0,0,24,24,12,0.12,94.26,1.44,2262.24,0.07450744654,0
Obstruction & Safety Sensors,estimate,estimate,,12,0.01,1,15.7,1,1,0,0,24,24,12,0.12,12,1.44,288,0.009526715492,0
,,,,,,,,,,,,,,,,,,,1,
,Samsung Fridge Calcs,,,,,,,,,,,,,,,,,,,
,Energy per year [kWh],Energy per day [Wh],Power [W],,Voltage [VAC],Current,,,,,,,,,,,,,,
,540,1479.452055,61.64383562,,120,0.5136986301,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,Solar Water Heater Pump Run Time [hrs],,,,,,,,,,,,,,,,,,,
,,Summer,Spring/Fall,Winter,,,,,,,,,,,,,,,,
,,Hot,Temperate,Cold,,,,,,,,,,,,,,,,
,Hi- Sunny,10,8,4,,,,,,,,,,,,,,,,
,Mid- Cloudy,3.5,2,0.5,,,,,,,,,,,,,,,,
,Lo- Shady,1,1,0,,,,,,,,,,,,,,,,

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H53,I12:I53)`
- **I5:** `=$A$4 * I6`
- **I6:** `=SUM(R12:S52)`
- **I7:** `=SUM(U12:U27)`
- **A8:** `=Summary!E3`
- **K12:** `=60*60*2`
- **L12:** `='User Matrix'!G5`
- **M12:** `=L12/60`
- **N12:** `=J12*M12`
- **O12:** `=IF(F12 = 0, 0, $A$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=PRODUCT(E12,G12,I12)`
- **R12:** `=P12*O12`
- **S12:** `=Q12*N12`
- **T12:** `=(N12*Q12+O12*P12) / $I$6`
- **U12:** `=D12*J12*I12`
- **K13:** `=60*60*2`
- **L13:** `='User Matrix'!G6`
- **M13:** `=L13/60`
- **N13:** `=J13*M13`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `=PRODUCT(E13,G13,I13)`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13`
- **T13:** `=(N13*Q13+O13*P13) / $I$6`
- **U13:** `=D13*J13*I13`
- **F14:** `=15.8/E14`
- **G14:** `=75/E14`
- **H14:** `=330/E14`
- **L14:** `=K14/60`
- **M14:** `='User Matrix'!G7`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $A$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$6`
- **U14:** `=D14*J14*I14`
- **D15:** `=(2/7)*I15`
- **F15:** `=G51`
- **G15:** `=G51`
- **H15:** `=G51`
- **K15:** `=24*60*60`
- **L15:** `=K15/60`
- **O15:** `=IF(F15 = 0, 0, $A$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$6`
- **U15:** `=D15*J15*I15`
- **G16:** `=30/120`
- **L16:** `='User Matrix'!$G$10`
- **M16:** `=L16/60`
- **N16:** `=J16*M16`
- **O16:** `=IF(F16 = 0, 0, $A$5-N16)`
- **P16:** `=PRODUCT(E16,F16,I16)`
- **Q16:** `=PRODUCT(E16,G16,I16)`
- **R16:** `=P16*O16`
- **S16:** `=Q16*N16`
- **T16:** `=(N16*Q16+O16*P16) / $I$6`
- **U16:** `=D16*J16*I16`
- **L17:** `='User Matrix'!$G$10`
- **M17:** `=L17/60`
- **N17:** `=J17*M17`
- **O17:** `=IF(F17 = 0, 0, $A$5-N17)`
- **P17:** `=PRODUCT(E17,F17,I17)`
- **Q17:** `=PRODUCT(E17,G17,I17)`
- **R17:** `=P17*O17`
- **S17:** `=Q17*N17`
- **T17:** `=(N17*Q17+O17*P17) / $I$6`
- **U17:** `=D17*J17*I17`
- **L18:** `='User Matrix'!G11`
- **M18:** `=L18/60`
- **N18:** `=J18*M18`
- **O18:** `=IF(F18 = 0, 0, $A$5-N18)`
- **P18:** `=PRODUCT(E18,F18,I18)`
- **Q18:** `=PRODUCT(E18,G18,I18)`
- **R18:** `=P18*O18`
- **S18:** `=Q18*N18`
- **T18:** `=(N18*Q18+O18*P18) / $I$6`
- **U18:** `=D18*J18*I18`
- **L19:** `=K19/60`
- **M19:** `=L19/60`
- **P19:** `=PRODUCT(E19,F19,I19)`
- **Q19:** `=PRODUCT(E19,G19,I19)`
- **R19:** `=P19*O19`
- **S19:** `=Q19*N19`
- **T19:** `=(N19*Q19+O19*P19) / $I$6`
- **U19:** `=D19*J19*I19`
- **L20:** `=K20/60`
- **P20:** `=PRODUCT(E20,F20,I20)`
- **Q20:** `=PRODUCT(E20,G20,I20)`
- **R20:** `=P20*O20`
- **S20:** `=Q20*N20`
- **T20:** `=(N20*Q20+O20*P20) / $I$6`
- **U20:** `=D20*J20*I20`
- **L21:** `=K21/60`
- **M21:** `='User Matrix'!G14`
- **N21:** `=J21*M21`
- **O21:** `=IF(F21 = 0, 0, $A$5-N21)`
- **P21:** `=PRODUCT(E21,F21,I21)`
- **Q21:** `=PRODUCT(E21,G21,I21)`
- **R21:** `=P21*O21`
- **S21:** `=Q21*N21`
- **T21:** `=(N21*Q21+O21*P21) / $I$6`
- **U21:** `=D21*J21*I21`
- **L22:** `=K22/60`
- **M22:** `='User Matrix'!G15`
- **N22:** `=J22*M22`
- **O22:** `=IF(F22 = 0, 0, $A$5-N22)`
- **P22:** `=PRODUCT(E22,F22,I22)`
- **Q22:** `=PRODUCT(E22,G22,I22)`
- **R22:** `=P22*O22`
- **S22:** `=Q22*N22`
- **T22:** `=(N22*Q22+O22*P22) / $I$6`
- **U22:** `=D22*J22*I22`
- **D23:** `='User Matrix'!G21`
- **L23:** `=K23/60`
- **M23:** `=L23/60`
- **N23:** `=J23*M23`
- **O23:** `=IF(F23 = 0, 0, $A$5-N23)`
- **P23:** `=PRODUCT(E23,F23,I23)`
- **Q23:** `=PRODUCT(E23,G23,I23)`
- **R23:** `=P23*O23`
- **S23:** `=Q23*N23`
- **T23:** `=(N23*Q23+O23*P23) / $I$6`
- **U23:** `=D23*J23*I23`
- **D24:** `='User Matrix'!G22`
- **L24:** `=K24/60`
- **M24:** `=L24/60`
- **N24:** `=J24*M24`
- **O24:** `=IF(F24 = 0, 0, $A$5-N24)`
- **P24:** `=PRODUCT(E24,F24,I24)`
- **Q24:** `=PRODUCT(E24,G24,I24)`
- **R24:** `=P24*O24`
- **S24:** `=Q24*N24`
- **T24:** `=(N24*Q24+O24*P24) / $I$6`
- **U24:** `=D24*J24*I24`
- **L25:** `=K25/60`
- **M25:** `=INDEX(Living!C56:E58, MATCH(Summary!E8, Living!C55:E55, 0), MATCH(Summary!E10, Living!B56:B58, 0))`
- **N25:** `=J25*M25`
- **O25:** `=IF(F25 = 0, 0, $A$5-N25)`
- **P25:** `=PRODUCT(E25,F25,I25)`
- **Q25:** `=PRODUCT(E25,G25,I25)`
- **R25:** `=P25*O25`
- **S25:** `=Q25*N25`
- **T25:** `=(N25*Q25+O25*P25) / $I$6`
- **U25:** `=D25*J25*I25`
- **L26:** `=I7/2`
- **M26:** `=L26/60`
- **N26:** `=J26*M26`
- **O26:** `=IF(F26 = 0, 0, $A$5-N26)`
- **P26:** `=PRODUCT(E26,F26,I26)`
- **Q26:** `=PRODUCT(E26,G26,I26)`
- **R26:** `=P26*O26`
- **S26:** `=Q26*N26`
- **T26:** `=(N26*Q26+O26*P26) / $I$6`
- **U26:** `=D26*J26*I26`
- **L27:** `=K27/60`
- **N27:** `=J27*M27`
- **O27:** `=IF(F27 = 0, 0, $A$5-N27)`
- **P27:** `=PRODUCT(E27,F27,I27)`
- **Q27:** `=PRODUCT(E27,G27,I27)`
- **R27:** `=P27*O27`
- **S27:** `=Q27*N27`
- **T27:** `=(N27*Q27+O27*P27) / $I$6`
- **U27:** `=D27*J27*I27`
- **L28:** `=K28/60`
- **O28:** `=IF(F28 = 0, 0, $A$5-N28)`
- **P28:** `=PRODUCT(E28,F28,I28)`
- **Q28:** `=PRODUCT(E28,G28,I28)`
- **R28:** `=P28*O28`
- **S28:** `=Q28*N28`
- **T28:** `=(N28*Q28+O28*P28) / $I$6`
- **U28:** `=D28*J28*I28`
- **G29:** `=5/E29`
- **L29:** `=K29/60`
- **N29:** `=J29*M29`
- **O29:** `=IF(F29 = 0, 0, $A$5-N29)`
- **P29:** `=PRODUCT(E29,F29,I29)`
- **Q29:** `=PRODUCT(E29,G29,I29)`
- **R29:** `=P29*O29`
- **S29:** `=Q29*N29`
- **T29:** `=(N29*Q29+O29*P29) / $I$6`
- **U29:** `=D29*J29*I29`
- **G30:** `=100/E30`
- **L30:** `=K30/60`
- **M30:** `='User Matrix'!$G$20`
- **N30:** `=J30*M30`
- **O30:** `=IF(F30 = 0, 0, $A$5-N30)`
- **P30:** `=PRODUCT(E30,F30,I30)`
- **Q30:** `=PRODUCT(E30,G30,I30)`
- **R30:** `=P30*O30`
- **S30:** `=Q30*N30`
- **T30:** `=(N30*Q30+O30*P30) / $I$6`
- **U30:** `=D30*J30*I30`
- **L31:** `=K31/60`
- **M31:** `='User Matrix'!$G$20`
- **N31:** `=J31*M31`
- **O31:** `=IF(F31 = 0, 0, $A$5-N31)`
- **P31:** `=PRODUCT(E31,F31,I31)`
- **Q31:** `=PRODUCT(E31,G31,I31)`
- **R31:** `=P31*O31`
- **S31:** `=Q31*N31`
- **T31:** `=(N31*Q31+O31*P31) / $I$6`
- **U31:** `=D31*J31*I31`
- **L32:** `=K32/60`
- **M32:** `='User Matrix'!G17`
- **N32:** `=J32*M32`
- **O32:** `=IF(F32 = 0, 0, $A$5-N32)`
- **P32:** `=PRODUCT(E32,F32,I32)`
- **Q32:** `=PRODUCT(E32,G32,I32)`
- **R32:** `=P32*O32`
- **S32:** `=Q32*N32`
- **T32:** `=(N32*Q32+O32*P32) / $I$6`
- **U32:** `=D32*J32*I32`
- **L33:** `=K33/60`
- **M33:** `='User Matrix'!G18`
- **N33:** `=J33*M33`
- **O33:** `=IF(F33 = 0, 0, $A$5-N33)`
- **P33:** `=PRODUCT(E33,F33,I33)`
- **Q33:** `=PRODUCT(E33,G33,I33)`
- **R33:** `=P33*O33`
- **S33:** `=Q33*N33`
- **T33:** `=(N33*Q33+O33*P33) / $I$6`
- **U33:** `=D33*J33*I33`
- **G34:** `=3.9/E34`
- **M34:** `=L34/60`
- **N34:** `=J34*M34`
- **O34:** `=IF(F34 = 0, 0, $A$5-N34)`
- **P34:** `=PRODUCT(E34,F34,I34)`
- **Q34:** `=PRODUCT(E34,G34,I34)`
- **R34:** `=P34*O34`
- **S34:** `=Q34*N34`
- **T34:** `=(N34*Q34+O34*P34) / $I$6`
- **U34:** `=D34*J34*I34`
- **G35:** `=(5.8*98)/E35`
- **L35:** `=K35/60`
- **N35:** `=J35*M35`
- **O35:** `=IF(F35 = 0, 0, $A$5-N35)`
- **P35:** `=PRODUCT(E35,F35,I35)`
- **Q35:** `=PRODUCT(E35,G35,I35)`
- **R35:** `=P35*O35`
- **S35:** `=Q35*N35`
- **T35:** `=(N35*Q35+O35*P35) / $I$6`
- **U35:** `=D35*J35*I35`
- **G36:** `=(60/E36)/2`
- **L36:** `=K36/60`
- **N36:** `=J36*M36`
- **O36:** `=IF(F36 = 0, 0, $A$5-N36)`
- **P36:** `=PRODUCT(E36,F36,I36)`
- **Q36:** `=PRODUCT(E36,G36,I36)`
- **R36:** `=P36*O36`
- **S36:** `=Q36*N36`
- **T36:** `=(N36*Q36+O36*P36) / $I$6`
- **U36:** `=D36*J36*I36`
- **G37:** `=10/E37`
- **L37:** `=K37/60`
- **P37:** `=PRODUCT(E37,F37,I37)`
- **Q37:** `=PRODUCT(E37,G37,I37)`
- **R37:** `=P37*O37`
- **S37:** `=Q37*N37`
- **T37:** `=(N37*Q37+O37*P37) / $I$6`
- **U37:** `=D37*J37*I37`
- **F38:** `=3/E38`
- **G38:** `=15/E38`
- **L38:** `=K38/60`
- **P38:** `=PRODUCT(E38,F38,I38)`
- **Q38:** `=PRODUCT(E38,G38,I38)`
- **R38:** `=P38*O38`
- **S38:** `=Q38*N38`
- **T38:** `=(N38*Q38+O38*P38) / $I$6`
- **U38:** `=D38*J38*I38`
- **F39:** `=9/E39`
- **L39:** `=K39/60`
- **P39:** `=PRODUCT(E39,F39,I39)`
- **Q39:** `=PRODUCT(E39,G39,I39)`
- **R39:** `=P39*O39`
- **S39:** `=Q39*N39`
- **T39:** `=(N39*Q39+O39*P39) / $I$6`
- **U39:** `=D39*J39*I39`
- **G40:** `=45/E40`
- **L40:** `=K40/60`
- **P40:** `=PRODUCT(E40,F40,I40)`
- **Q40:** `=PRODUCT(E40,G40,I40)`
- **R40:** `=P40*O40`
- **S40:** `=Q40*N40`
- **T40:** `=(N40*Q40+O40*P40) / $I$6`
- **U40:** `=D40*J40*I40`
- **F41:** `=15/E41`
- **G41:** `=250/E41`
- **H41:** `=500/E41`
- **L41:** `=K41/60`
- **P41:** `=PRODUCT(E41,F41,I41)`
- **Q41:** `=PRODUCT(E41,G41,I41)`
- **R41:** `=P41*O41`
- **S41:** `=Q41*N41`
- **T41:** `=(N41*Q41+O41*P41) / $I$6`
- **U41:** `=D41*J41*I41`
- **G42:** `=220/E42`
- **H42:** `=1320/E42`
- **L42:** `=K42/60`
- **P42:** `=PRODUCT(E42,F42,I42)`
- **Q42:** `=PRODUCT(E42,G42,I42)`
- **R42:** `=P42*O42`
- **S42:** `=Q42*N42`
- **T42:** `=(N42*Q42+O42*P42) / $I$6`
- **U42:** `=D42*J42*I42`
- **F43:** `=100/E43`
- **G43:** `=86/E43`
- **H43:** `=550/E43`
- **L43:** `=K43/60`
- **M43:** `='User Matrix'!G8`
- **P43:** `=PRODUCT(E43,F43,I43)`
- **Q43:** `=PRODUCT(E43,G43,I43)`
- **R43:** `=P43*O43`
- **S43:** `=Q43*N43`
- **T43:** `=(N43*Q43+O43*P43) / $I$6`
- **U43:** `=D43*J43*I43`
- **J44:** `='User Matrix'!G19`
- **L44:** `=K44/60`
- **M44:** `=L44/60`
- **N44:** `=J44*M44`
- **P44:** `=PRODUCT(E44,F44,I44)`
- **Q44:** `=PRODUCT(E44,G44,I44)`
- **R44:** `=P44*O44`
- **S44:** `=Q44*N44`
- **T44:** `=(N44*Q44+O44*P44) / $I$6`
- **U44:** `=D44*J44*I44`
- **G45:** `=150/E45`
- **L45:** `=K45/60`
- **N45:** `=J45*M45`
- **P45:** `=PRODUCT(E45,F45,I45)`
- **Q45:** `=PRODUCT(E45,G45,I45)`
- **R45:** `=P45*O45`
- **S45:** `=Q45*N45`
- **T45:** `=(N45*Q45+O45*P45) / $I$6`
- **U45:** `=D45*J45*I45`
- **G46:** `=(H46+F46)/2`
- **L46:** `=K46/60`
- **N46:** `=J46*M46`
- **P46:** `=PRODUCT(E46,F46,I46)`
- **Q46:** `=PRODUCT(E46,G46,I46)`
- **R46:** `=P46*O46`
- **S46:** `=Q46*N46`
- **T46:** `=(N46*Q46+O46*P46) / $I$6`
- **U46:** `=D46*J46*I46`
- **L47:** `=K47/60`
- **N47:** `=J47*M47`
- **P47:** `=PRODUCT(E47,F47,I47)`
- **Q47:** `=PRODUCT(E47,G47,I47)`
- **R47:** `=P47*O47`
- **S47:** `=Q47*N47`
- **T47:** `=(N47*Q47+O47*P47) / $I$6`
- **U47:** `=D47*J47*I47`
- **T48:** `=SUM(T12:T47)`
- **C51:** `=(B51/365)*1000`
- **D51:** `=C51/24`
- **G51:** `=D51/F51`

---

## Sheet: Cooking

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
System Inputs,,,,,,,,System Outputs,,,,,,,,,,,,
Value,Unit,Description,,,,,,Value,Unit,Description,,,Used for,,,,,,,
1,-,Factor of safety applied to total energy required,,,,,,67.58333333,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,,
24,hr / day,Max operation time / day,,,,,,2472.295833,Wh,Total energy / cycle with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,,
1,cycles / day,Number of times operated / day,,,,,,2472.295833,Wh,Total energy / meal w/o factor of safety applied,,,,,,,,,,
Typical,-,User (Selected in Summary),,,,,,2.125,Gal,Total water / meal w/o factor of safety applied,,,,,,,,,,
2,Meals/day,From user matrix,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
Component,Make,Model,Water Used (gal/cycle),Voltage (V),Idle (A),Average,Peak (A),Qty,Cycles/Meal,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle (W),Average (W),Idle Contribution (Wh),Average Contribution (Wh),% Contribution to energy budget,Water Used per Day (Gal)
Stove (14) (18),Samsung,NZ24T4360RK/AA / NZ24T4360RK/AA,,240,0,3.645,14.58,0,1,0,15,0.25,0.25,0,0,0,0,0,0,0
Stove,Samsung,NZ30K6330RS/AA / NZ30K6330RS/AA,,240,0,12.5,39.58333333,1,1,0,15,0.25,0.25,0,0,3000,0,750,0.3033617538,0
Portable two-burner Induction Cooktop,Cuisinart,ICT-60P1,,120,0,7.5,15,1,1,0,15,0.25,0.25,0,0,900,0,225,0.09100852615,0
Microwave,Samsung,ME21DB630012AA / ME21DB630012AA,,120,0,14.16666667,0,0,1,0,3.5,0.05833333333,0.05833333333,0,0,0,0,0,0,0
4-1 Microwave,Panasonic,NN-CD87KS,,120,0,8.333333333,0,1,1,0,0.5,0.008333333333,0.008333333333,0,0,1000,0,8.333333333,0.003370686154,0
Dishwasher,Fotile,SD2F-P3,1.25,120,0,5.35,13,1,0.5,0,80,1.333333333,0.6666666667,0,0,642,0,428,0.1731184409,0.625
Garbage disposal,InSinkErator, Badger 1XL,,120,0,5.6,0,1,1,0,0.5,0.008333333333,0.008333333333,0,0,672,0,5.6,0.002265101095,0
Range hood,Samsung,NK30N7000UG/AA,,120,0,3.52,0,1,17,0,5,0.08333333333,1.416666667,0,0,422.4,0,598.4,0.2420422313,0
Consumer electronics,example,"blender, coffee maker, kettle, food processor, mixer, rice maker, toaster",,120,0,5,0,1,1,0,5,0.08333333333,0.08333333333,0,0,600,0,50,0.02022411692,0
Tankless water heater,Camplux,8kw,,240,0,33.4,0,1,1,0,3,0.05,0.05,0,0,8016,0,400.8,0.1621165212,0
Water pump,SHURflo,4048-153-E75 / 4048-153-A75,,12,0,8.5,0,1,1,0,3.625,0.06041666667,0.06041666667,0,0,102,0,6.1625,0.002492622411,0
Kitchen faucet,estimate,estimate,1.5,,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1.5
,,,,,,,,,,,,,,,,,,,1,
,,,,,,,,,,,,,,,,,,,,
,,Appliance Energy Calcs,,,,,,,,,,,,,,,,,,
,,Dishwasher EnergyGuide [kWh/yr],178,,,,,,,,,,,,,,,,,
,,Dishwasher Energy per cycle [Wh],855.7692308,,,,,,,,,,,,,,,,,
,,Samsung NZ30 average power (W) (17) ,3000,,,,,,,,,,,,,,,,,
,,Samsung NZ30 voltage (VAC),240,,,,,,,,,,,,,,,,,
,,Samsung NZ30 average current (A),12.5,,,,,,,,,,,,,,,,,
,,Samsung NZ30 peak power (W),9500,,,,,,,,,,,,,,,,,
,,Samsung NZ30 peak current (A),39.58333333,,,,,,,,,,,,,,,,,
,,Cuisinart ICT-60P1 peak power (W),1800,,,,,,,,,,,,,,,,,
,,Cuisinart ICT-60P1 small burner (W),600,,,,,,,,,,,,,,,,,
,,Cuisinart ICT-60P1 large burner (W),1200,,,,,,,,,,,,,,,,,

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H29,I12:I29)`
- **I5:** `=$A$4 * I6`
- **I6:** `=SUM(R12:S23)`
- **A7:** `=Summary!E3`
- **I7:** `=SUM(U12:U25)`
- **A8:** `='User Matrix'!G26`
- **G12:** `=14.58/4`
- **J12:** `='User Matrix'!G24`
- **L12:** `='User Matrix'!G23`
- **M12:** `=L12/60`
- **N12:** `=J12*M12`
- **O12:** `=IF(F12 = 0, 0, $A$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=PRODUCT(E12,G12,I12)`
- **R12:** `=P12*O12`
- **S12:** `=Q12*N12`
- **T12:** `=(N12*Q12+O12*P12) / $I$6`
- **U12:** `=D12*J12*I12`
- **G13:** `=D31`
- **H13:** `=D33`
- **L13:** `='User Matrix'!$G$23`
- **M13:** `=L13/60`
- **N13:** `=J13*M13`
- **O13:** `=IF(F13 = 0, 0, $A$5-N13)`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `=PRODUCT(E13,G13,I13)`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13`
- **T13:** `=(N13*Q13+O13*P13) / $I$6`
- **U13:** `=D13*J13*I13`
- **G14:** `=(D34/E14)/2`
- **H14:** `=D34/E14`
- **L14:** `='User Matrix'!$G$23`
- **M14:** `=L14/60`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $A$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$6`
- **U14:** `=D14*J14*I14`
- **G15:** `=1700/120`
- **L15:** `='User Matrix'!G27`
- **M15:** `=L15/60`
- **N15:** `=J15*M15`
- **O15:** `=IF(F15 = 0, 0, $A$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$6`
- **U15:** `=D15*J15*I15`
- **G16:** `=1000/E16`
- **L16:** `='User Matrix'!G28`
- **M16:** `=L16/60`
- **N16:** `=J16*M16`
- **O16:** `=IF(F16 = 0, 0, $A$5-N16)`
- **P16:** `=PRODUCT(E16,F16,I16)`
- **Q16:** `=PRODUCT(E16,G16,I16)`
- **R16:** `=P16*O16`
- **S16:** `=Q16*N16`
- **T16:** `=(N16*Q16+O16*P16) / $I$6`
- **U16:** `=D16*J16*I16`
- **D17:** `='User Matrix'!G33 * I17`
- **J17:** `='User Matrix'!G28`
- **M17:** `=L17/60`
- **N17:** `=J17*M17`
- **O17:** `=IF(F17 = 0, 0, $A$5-N17)`
- **P17:** `=PRODUCT(E17,F17,I17)`
- **Q17:** `=PRODUCT(E17,G17,I17)`
- **R17:** `=P17*O17`
- **S17:** `=Q17*N17`
- **T17:** `=(N17*Q17+O17*P17) / $I$6`
- **U17:** `=D17*J17*I17`
- **L18:** `='User Matrix'!G29`
- **M18:** `=L18/60`
- **N18:** `=J18*M18`
- **O18:** `=IF(F18 = 0, 0, $A$5-N18)`
- **P18:** `=PRODUCT(E18,F18,I18)`
- **Q18:** `=PRODUCT(E18,G18,I18)`
- **R18:** `=P18*O18`
- **S18:** `=Q18*N18`
- **T18:** `=(N18*Q18+O18*P18) / $I$6`
- **U18:** `=D18*J18*I18`
- **J19:** `='User Matrix'!G25`
- **L19:** `='User Matrix'!G30`
- **M19:** `=L19/60`
- **N19:** `=J19*M19`
- **O19:** `=IF(F19 = 0, 0, $A$5-N19)`
- **P19:** `=PRODUCT(E19,F19,I19)`
- **Q19:** `=PRODUCT(E19,G19,I19)`
- **R19:** `=P19*O19`
- **S19:** `=Q19*N19`
- **T19:** `=(N19*Q19+O19*P19) / $I$6`
- **U19:** `=D19*J19*I19`
- **L20:** `='User Matrix'!G30`
- **M20:** `=L20/60`
- **N20:** `=J20*M20`
- **O20:** `=IF(F20 = 0, 0, $A$5-N20)`
- **P20:** `=PRODUCT(E20,F20,I20)`
- **Q20:** `=PRODUCT(E20,G20,I20)`
- **R20:** `=P20*O20`
- **S20:** `=Q20*N20`
- **T20:** `=(N20*Q20+O20*P20) / $I$6`
- **U20:** `=D20*J20*I20`
- **L21:** `='User Matrix'!G31`
- **M21:** `=L21/60`
- **N21:** `=J21*M21`
- **O21:** `=IF(F21 = 0, 0, $A$5-N21)`
- **P21:** `=PRODUCT(E21,F21,I21)`
- **Q21:** `=PRODUCT(E21,G21,I21)`
- **R21:** `=P21*O21`
- **S21:** `=Q21*N21`
- **T21:** `=(N21*Q21+O21*P21) / $I$6`
- **U21:** `=D21*J21*I21`
- **L22:** `='User Matrix'!G32`
- **M22:** `=L22/60`
- **N22:** `=J22*M22`
- **O22:** `=IF(F22 = 0, 0, $A$5-N22)`
- **P22:** `=PRODUCT(E22,F22,I22)`
- **Q22:** `=PRODUCT(E22,G22,I22)`
- **R22:** `=P22*O22`
- **S22:** `=Q22*N22`
- **T22:** `=(N22*Q22+O22*P22) / $I$6`
- **U22:** `=D22*J22*I22`
- **D23:** `='User Matrix'!G34`
- **L23:** `=K23/60`
- **M23:** `=L23/60`
- **N23:** `=J23*M23`
- **O23:** `=IF(F23 = 0, 0, $A$5-N23)`
- **P23:** `=PRODUCT(E23,F23,I23)`
- **Q23:** `=PRODUCT(E23,G23,I23)`
- **R23:** `=P23*O23`
- **S23:** `=Q23*N23`
- **T23:** `=(N23*Q23+O23*P23) / $I$6`
- **U23:** `=D23*J23*I23`
- **T24:** `=SUM(T12:T23)`
- **D28:** `=D27/(52*4)*1000`
- **D31:** `=D29/D30`
- **D33:** `=D32/D30`

---

## Sheet: Toilet

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
System Inputs,,,,,,,,System Outputs,,,,,,,,,,,Sheet Key,
Value,Unit,Description,,,,,,Value,Unit,Description,,,Used for,,,,,,Input field,
1,-,Factor of safety applied to total energy required,,,,,,0,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field,
24,hr / day,Max operation time / day,,,,,,36.016,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,,
,,,,,,,,36.016,Wh,Total energy / day w/o factor of safety applied,,,,,,,,,,
1440,min,Max single cycle duration,,,,,,0.375,Gal,Total water / day w/o factor of safety applied,,,-,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations,
Component,Make,Model,Water Used (gal/cycle),Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget,Water Used per Day (Gal)
Grey water pump (P7),Whale Pumps,Gulper 220,,12,0,2.4,0,1,1,63,1.05,0.0175,0.0175,0,0,28.8,0,0.504,0.01399378054,0
Bathroom vent fan,Maxxair,00-003801 Mini Vent Plus,,12,0,1.9,0,1,1,0,4,0.06666666667,0.06666666667,0,0,22.8,0,1.52,0.04220346513,0
Macerating pump (P10),Pentair,3200-001,,12,0,17,0,1,1,10,0.1666666667,0.002777777778,0.002777777778,0,0,204,0,0.5666666667,0.01573374796,0
Tankless water heater,Camplux,8kW,,240,0,33.4,0,1,1,0,0.25,0.004166666667,0.004166666667,0,0,8016,0,33.4,0.9273656153,0
Toilet (gravity) (9),estimate,estimate,0,,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0
Toilet (incinerator),Cinderella,Comfort Incineration Toilet,,240,0,5,0,0,0.25,0,0,1.583333333,0.3958333333,0,0,0,0,0,0,0
Bathroom sink,Pentair,Shurflo SLV,0.375,12,0,1.9,0,1,1,4,0.06666666667,0.001111111111,0.001111111111,0,0,22.8,0,0.02533333333,0.0007033910854,0.375
,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H20,I12:I20)`
- **I5:** `=$A$4 * I6`
- **I6:** `=SUM(R12:S19)`
- **I7:** `=SUM(U12:U19)`
- **K12:** `=L12*60`
- **L12:** `='User Matrix'!G36`
- **M12:** `=L12/60`
- **N12:** `=J12*M12`
- **O12:** `=IF(F12 = 0, 0, $A$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=PRODUCT(E12,G12,I12)`
- **R12:** `=P12*O12`
- **S12:** `=Q12*N12`
- **T12:** `=(N12*Q12+O12*P12) / $I$6`
- **U12:** `=D12*J12*I12`
- **L13:** `='User Matrix'!G37`
- **M13:** `=L13/60`
- **N13:** `=J13*M13`
- **O13:** `=IF(F13 = 0, 0, $A$5-N13)`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `=PRODUCT(E13,G13,I13)`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13`
- **T13:** `=(N13*Q13+O13*P13) / $I$6`
- **U13:** `=D13*J13*I13`
- **L14:** `=K14/60`
- **M14:** `=L14/60`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $A$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$6`
- **U14:** `=D14*J14*I14`
- **L15:** `='User Matrix'!G38`
- **M15:** `=L15/60`
- **N15:** `=J15*M15`
- **O15:** `=IF(F15 = 0, 0, $A$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$6`
- **U15:** `=D15*J15*I15`
- **D16:** `=IF('Lookup Tables'!C31<1, 0.4, 0)`
- **L16:** `=K16/60`
- **M16:** `=L16/60`
- **N16:** `=J16*M16`
- **O16:** `=IF(F16 = 0, 0, $A$5-N16)`
- **P16:** `=PRODUCT(E16,F16,I16)`
- **Q16:** `=PRODUCT(E16,G16,I16)`
- **R16:** `=P16*O16`
- **S16:** `=Q16*N16`
- **T16:** `=(N16*Q16+O16*P16) / $I$6`
- **U16:** `=D16*J16*I16`
- **L17:** `=K17/60`
- **M17:** `=1900/1200`
- **N17:** `=J17*M17`
- **O17:** `=IF(F17 = 0, 0, $A$5-N17)`
- **P17:** `=PRODUCT(E17,F17,I17)`
- **Q17:** `=PRODUCT(E17,G17,I17)`
- **R17:** `=P17*O17`
- **S17:** `=Q17*N17`
- **T17:** `=(N17*Q17+O17*P17) / $I$6`
- **U17:** `=D17*J17*I17`
- **D18:** `='User Matrix'!G42`
- **L18:** `=K18/60`
- **M18:** `=L18/60`
- **N18:** `=J18*M18`
- **O18:** `=IF(F18 = 0, 0, $A$5-N18)`
- **P18:** `=PRODUCT(E18,F18,I18)`
- **Q18:** `=PRODUCT(E18,G18,I18)`
- **R18:** `=P18*O18`
- **S18:** `=Q18*N18`
- **T18:** `=(N18*Q18+O18*P18) / $I$6`
- **U18:** `=D18*J18*I18`
- **L19:** `=K19/60`
- **M19:** `=L19/60`
- **N19:** `=J19*M19`
- **O19:** `=IF(F19 = 0, 0, $A$5-N19)`
- **P19:** `=PRODUCT(E19,F19,I19)`
- **Q19:** `=PRODUCT(E19,G19,I19)`
- **R19:** `=P19*O19`
- **S19:** `=Q19*N19`
- **T19:** `=(N19*Q19+O19*P19) / $I$6`
- **U19:** `=D19*J19*I19`

---

## Sheet: Shower

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20,Unnamed: 21
,System Inputs,,,,,,,,System Outputs,,,,,,,,,,Sheet Key,,
,Value,Unit,Description,,,,,,Value,Unit,Description,,,Used for,,,,,Input field,,
,1,-,Factor of safety applied to total energy required,,,,,,81.8,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,Output / calculated field,,
,24,hr / day,Max operation time / day,,,,,,857.9,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,,
,1,cycles / day / person,Number of times operated / day,,,,,,857.9,Wh,Total energy / day w/o factor of safety applied,,,,,,,,,,
,1440,min,Max single cycle duration,,,,,,12,Gal,Total water / day w/o factor of safety applied,,,-,,,,,,,
,Typical,,User selected on summary sheet,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations,
,Component,Make,Model,Water Used (gal/cycle),Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget,Water Used per Day (Gal)
,Electric shower,Aqualisa,eMotion,,240,0,33,0,1,1,360,6,0.1,0.1,0,0,7920,0,792,0.9231845203,0
,Bathroom vent fan,Maxxair,00-003801 Mini Vent Plus,,12,0,1.9,0,1,1,0,15,0.25,0.25,0,0,22.8,0,5.7,0.006644131018,0
,Consumer electronics,various,"ex: hair dryer, toothbrush/electric razor chargers",,120,0,5,0,1,1,0,5,0.08333333333,0.08333333333,0,0,600,0,50,0.05828185103,0
,Water pump,SHURflo,4048-153-E75 / 4048-153-A75,,12,0,8.5,0,1,1,0,6,0.1,0.1,0,0,102,0,10.2,0.01188949761,0
,Shower control keypad (6),CZone,Landscape 80-911-0162-00 & Portrait 80-911-0163-00,,12,0,0.056,0,0,1,0,6,0.1,0.1,0,0,0,0,0,0,0
,Tankless water heater,Camplux,8kW,,240,0,33.4,0,1,0,0,0,0,0,0,0,8016,0,0,0,0
,UV Water System(5),Viqua,VT4,,12,0,1.8,0,0,1,0,6,0.1,0.1,0,0,0,0,0,0,0
,Shower recirc 3-way valve,HSH-Flo,3 Way 24VAC/DC 4-20ma Proportional Integral Control Ball Valve,,24,0,0.95,0,0,2,1,0.01666666667,0.0002777777778,0.0005555555556,0,0,0,0,0,0,0
,Shower recirc pump (P5),US Solar ,S5 12V 12.6L PV,,12,0,1.25,0,0,1,0,0,0,0,0,0,0,0,0,0,0
,Grey water pump (P9),Whale Pumps,Gulper 220,,12,0,2.5,0,0,1,0,0,0,0,0,0,0,0,0,0,0
,Calorifier (22),SureCal,30 liter / 7.92 gal Horizontal Single Coil,,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,Electronically controlled blend valve (23),Caleffi,600054A,,120,0,6,0,0,1,0,0,0,0,0,0,0,0,0,0,0
,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,1,
,Capacity of Solar Shower [gal],8,,,,,,,,,,,,,,,,,,,
,Target heated water temp [F°],100,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,Temp of Water in Solar Shower [estimates],,,,,Solar Shower Power Factor (16) ,,,,,,,,,,,,,,,
,,Hot,Temperate,Cold,,,Hot,Temperate,Cold,,,,,,,,,,,,
,Sunny,100,80,60,,Hi- Sunny,0,0.66,1.66,,,,,,,,,,,,
,Cloudy,80,70,50,,Mid- Cloudy,0.66,1,1.33,,,,,,,,,,,,
,Shady,60,50,40,,Lo- Shady,1.66,1.33,2,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,,Glamper,Typical,Expert,Unit,Notes,,,,,,,,,,,,,,,
,Total shower time,10,6,3,mins,Defined in user matrix,,,,,,,,,,,,,,,
,Solar heated water (Solar Factor * Electric shower water heater pwr),0,0,0,min,Defined in user matrix. Up to max 4mins w/ assumed 2gpm showerhead. Removed solar heating capability,,,,,,,,,,,,,,,
,Solar shower period power factor Output,0,0,0,,Dependent on environmental conditions. Multiplied by water heater max pwr (~8.5kW) ,,,,,,,,,,,,,,,
,Solar period power,0,0,0,W,,,,,,,,,,,,,,,,
,Solar period energy,0,0,0,Wh,,,,,,,,,,,,,,,,
,Solar period water consumption,0,0,0,gallons,,,,,,,,,,,,,,,,
,Recirculated percentage,0,0,0,percentage,Defined in user matrix,,,,,,,,,,,,,,,
,Recirculated shower time,0,0,0,mins,Total shower time * recirc % . During this phase all water is recirculated/no  freshwater is used,,,,,,,,,,,,,,,
,Recirc Shower power factor,0.2,0.2,0.2,%,Estimated addl heating required for solar-heated & recirc'd water,,,,,,,,,,,,,,,
,Recirc Shower pwr,1584,1584,1584,W,,,,,,,,,,,,,,,,
,Recirc Shower Energy,0,0,0,Wh,,,,,,,,,,,,,,,,
,Recirc water consumption,0,0,0,,,,,,,,,,,,,,,,,
,Electrically heated shower duration,10,6,3,mins,,,,,,,,,,,,,,,,
,Electrically heated shower energy,1320,792,396,Wh,,,,,,,,,,,,,,,,
,Electrically heated shower water consumption,20,12,6,gallons,,,,,,,,,,,,,,,,
,Total shower Energy W/ Solar & Recirc,1320,792,396,Wh,,,,,,,,,,,,,,,,
,Total shower energy w/out solar & recirc,1320,792,396,Wh,,,,,,,,,,,,,,,,
,Energy reduction w/ solar & recirc,0,0,0,percentage,,,,,,,,,,,,,,,,
,Total water consumption w/ solar & recirc,20,12,6,Gallons,,,,,,,,,,,,,,,,
,Total water consumption w/out solar & recirc,20,12,6,Gallons,,,,,,,,,,,,,,,,
,Water reduction w/ solar & recirc,0,0,0,percentage,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,Lookup Table: Shower Duration per User Chart,,,,,Lookeup Table: Electronic Blend Valve Cycles,,,,,,,,,,,,,,,
,USER,Solar heated water,Recirculated solar heated water,Electrically heated water [mins],,,Hot,Temperate,Cold,,,,,,,,,,,,
,Expert,0,0,3,,Hi- Sunny,1,1,0,,,,,,,,,,,,
,Typical,0,0,6,,Mid- Cloudy,1,1,0,,,,,,,,,,,,
,Glamper,0,0,10,,Lo- Shady,0,0,0,,,,,,,,,,,,

```

### Formulas Used

- **J4:** `=SUMPRODUCT(H12:H31,J12:J31)`
- **J5:** `=$B$4 * J6`
- **B6:** `='User Matrix'!G43`
- **J6:** `=SUM(S13:T23)+HLOOKUP(Summary!E3, C36:E57, 17, FALSE)`
- **J7:** `=HLOOKUP(Summary!E3, C36:E57, 20, FALSE)`
- **B8:** `=Summary!E3`
- **L12:** `=M12*60`
- **M12:** `='User Matrix'!G45`
- **N12:** `=M12/60`
- **O12:** `=K12*N12`
- **P12:** `=IF(G12 = 0, 0, $B$5-O12)`
- **Q12:** `=PRODUCT(F12,G12,J12)`
- **R12:** `=PRODUCT(F12,H12,J12)`
- **S12:** `=Q12*P12`
- **T12:** `=R12*O12`
- **U12:** `=(O12*R12+P12*Q12) / $J$6`
- **V12:** `=E12*K12*J12`
- **M13:** `='User Matrix'!G47`
- **N13:** `=M13/60`
- **O13:** `=K13*N13`
- **P13:** `=IF(G13 = 0, 0, $B$5-O13)`
- **Q13:** `=PRODUCT(F13,G13,J13)`
- **R13:** `=PRODUCT(F13,H13,J13)`
- **S13:** `=Q13*P13`
- **T13:** `=R13*O13`
- **U13:** `=(O13*R13+P13*Q13) / $J$6`
- **V13:** `=E13*K13*J13`
- **M14:** `='User Matrix'!G48`
- **N14:** `=M14/60`
- **O14:** `=K14*N14`
- **P14:** `=IF(G14 = 0, 0, $B$5-O14)`
- **Q14:** `=PRODUCT(F14,G14,J14)`
- **R14:** `=PRODUCT(F14,H14,J14)`
- **S14:** `=Q14*P14`
- **T14:** `=R14*O14`
- **U14:** `=(O14*R14+P14*Q14) / $J$6`
- **V14:** `=E14*K14*J14`
- **M15:** `=HLOOKUP(Summary!E3, C36:E49, 14, FALSE)`
- **N15:** `=M15/60`
- **O15:** `=K15*N15`
- **P15:** `=IF(G15 = 0, 0, $B$5-O15)`
- **Q15:** `=PRODUCT(F15,G15,J15)`
- **R15:** `=PRODUCT(F15,H15,J15)`
- **S15:** `=Q15*P15`
- **T15:** `=R15*O15`
- **U15:** `=(O15*R15+P15*Q15) / $J$6`
- **V15:** `=E15*K15*J15`
- **M16:** `=HLOOKUP(Summary!E3, C36:E49, 2, FALSE)`
- **N16:** `=M16/60`
- **O16:** `=K16*N16`
- **P16:** `=IF(G16 = 0, 0, $B$5-O16)`
- **Q16:** `=PRODUCT(Living!E28,G16,J16)`
- **R16:** `=PRODUCT(Living!E28,H16,J16)`
- **S16:** `=Q16*P16`
- **T16:** `=R16*O16`
- **U16:** `=(O16*R16+P16*Q16) / $J$6`
- **V16:** `=Living!D28*K16*J16`
- **M17:** `=L17/60`
- **N17:** `=M17/60`
- **O17:** `=K17*N17`
- **P17:** `=IF(G17 = 0, 0, $B$5-O17)`
- **Q17:** `=PRODUCT(F17,G17,J17)`
- **R17:** `=PRODUCT(F17,H17,J17)`
- **S17:** `=Q17*P17`
- **T17:** `=R17*O17`
- **U17:** `=(O17*R17+P17*Q17) / $J$6`
- **V17:** `=E17*K17*J17`
- **M18:** `=HLOOKUP(Summary!E3, C36:E49, 14, FALSE)`
- **N18:** `=M18/60`
- **O18:** `=K18*N18`
- **P18:** `=IF(G18 = 0, 0, $B$5-O18)`
- **Q18:** `=PRODUCT(F18,G18,J18)`
- **R18:** `=PRODUCT(F18,H18,J18)`
- **S18:** `=Q18*P18`
- **T18:** `=R18*O18`
- **U18:** `=(O18*R18+P18*Q18) / $J$6`
- **V18:** `=E18*K18*J18`
- **M19:** `=L19/60`
- **N19:** `=M19/60`
- **O19:** `=K19*N19`
- **P19:** `=IF(G19 = 0, 0, $B$5-O19)`
- **Q19:** `=PRODUCT(F19,G19,J19)`
- **R19:** `=PRODUCT(F19,H19,J19)`
- **S19:** `=Q19*P19`
- **T19:** `=R19*O19`
- **U19:** `=(O19*R19+P19*Q19) / $J$6`
- **V19:** `=E19*K19*J19`
- **M20:** `=HLOOKUP(Summary!E3,C36:E44, 9, FALSE)`
- **N20:** `=M20/60`
- **O20:** `=K20*N20`
- **P20:** `=IF(G20 = 0, 0, $B$5-O20)`
- **Q20:** `=PRODUCT(F20,G20,J20)`
- **R20:** `=PRODUCT(F20,H20,J20)`
- **S20:** `=Q20*P20`
- **T20:** `=R20*O20`
- **U20:** `=(O20*R20+P20*Q20) / $J$6`
- **V20:** `=E20*K20*J20`
- **M21:** `=HLOOKUP(Summary!E3,C36:E44, 9, FALSE)`
- **N21:** `=M21/60`
- **O21:** `=K21*N21`
- **P21:** `=IF(G21 = 0, 0, $B$5-O21)`
- **Q21:** `=PRODUCT(F21,G21,J21)`
- **R21:** `=PRODUCT(F21,H21,J21)`
- **S21:** `=Q21*P21`
- **T21:** `=R21*O21`
- **U21:** `=(O21*R21+P21*Q21) / $J$6`
- **V21:** `=E21*K21*J21`
- **M22:** `=L22/60`
- **N22:** `=M22/60`
- **O22:** `=K22*N22`
- **P22:** `=IF(G22 = 0, 0, $B$5-O22)`
- **Q22:** `=PRODUCT(F22,G22,J22)`
- **R22:** `=PRODUCT(F22,H22,J22)`
- **S22:** `=Q22*P22`
- **T22:** `=R22*O22`
- **U22:** `=(O22*R22+P22*Q22) / $J$6`
- **V22:** `=E22*K22*J22`
- **K23:** `=INDEX(H61:J63, MATCH(Summary!E10, G61:G63, 0), MATCH(Summary!E8, H60:J60, 0))`
- **M23:** `=HLOOKUP(Summary!E3,C36:E44, 3, FALSE)`
- **N23:** `=M23/60`
- **O23:** `=K23*N23`
- **P23:** `=IF(G23 = 0, 0, $B$5-O23)`
- **Q23:** `=PRODUCT(F23,G23,J23)`
- **R23:** `=PRODUCT(F23,H23,J23)`
- **S23:** `=Q23*P23`
- **T23:** `=R23*O23`
- **U23:** `=(O23*R23+P23*Q23) / $J$6`
- **V23:** `=E23*K23*J23`
- **U26:** `=SUM(U12:U15)`
- **C37:** `='User Matrix'!C45`
- **D37:** `='User Matrix'!D45`
- **E37:** `='User Matrix'!E45`
- **C38:** `='User Matrix'!C44`
- **D38:** `='User Matrix'!D44`
- **E38:** `='User Matrix'!E44`
- **C39:** `=INDEX($H$32:$J$34, MATCH(Summary!$E$10, $G$32:$G$34, 0),MATCH(Summary!$E$8, $H$31:$J$31, 0))`
- **D39:** `=INDEX($H$32:$J$34, MATCH(Summary!$E$10, $G$32:$G$34, 0),MATCH(Summary!$E$8, $H$31:$J$31, 0))`
- **E39:** `=INDEX($H$32:$J$34, MATCH(Summary!$E$10, $G$32:$G$34, 0),MATCH(Summary!$E$8, $H$31:$J$31, 0))`
- **C40:** `=C39*$R$12`
- **D40:** `=D39*$R$12`
- **E40:** `=E39*$R$12`
- **C41:** `=(C38/60)*C40`
- **D41:** `=(D38/60)*D40`
- **E41:** `=(E38/60)*E40`
- **C42:** `=2*C38`
- **D42:** `=2*D38`
- **E42:** `=2*E38`
- **C43:** `='User Matrix'!C49`
- **D43:** `='User Matrix'!D49`
- **E43:** `='User Matrix'!E49`
- **C44:** `=C37*C43`
- **D44:** `=D37*D43`
- **E44:** `=E37*E43`
- **C46:** `=$R$12*(C45)`
- **D46:** `=$R$12*(D45)`
- **E46:** `=$R$12*(E45)`
- **C47:** `=(C44/60)*C46`
- **D47:** `=(D44/60)*D46`
- **E47:** `=(E44/60)*E46`
- **C49:** `=C37-C38-C44`
- **D49:** `=D37-D38-D44`
- **E49:** `=IF(E37-E38-E44 > 0, E37-E38-E44, 0)`
- **C50:** `=(C49/60)*$R$12`
- **D50:** `=(D49/60)*$R$12`
- **E50:** `=(E49/60)*$R$12`
- **C51:** `=2*C49`
- **D51:** `=2*D49`
- **E51:** `=2*E49`
- **C52:** `=C41+C47+C50`
- **D52:** `=D41+D47+D50`
- **E52:** `=E41+E47+E50`
- **C53:** `=$R$12*C37/60`
- **D53:** `=$R$12*D37/60`
- **E53:** `=$R$12*E37/60`
- **C54:** `=(C52-C53)/C53`
- **D54:** `=(D52-D53)/D53`
- **E54:** `=(E52-E53)/E53`
- **C55:** `=C42+C48+C51`
- **D55:** `=D42+D48+D51`
- **E55:** `=E42+E48+E51`
- **C56:** `=2*C37`
- **D56:** `=2*D37`
- **E56:** `=2*E37`
- **C57:** `=(C55-C56)/C56`
- **D57:** `=(D55-D56)/D56`
- **E57:** `=(E55-E56)/E56`
- **C61:** `=E38`
- **D61:** `=E44`
- **E61:** `=IF(E37-(D61+C61) > 0, E37-(D61+C61), 0)`
- **C62:** `=D38`
- **D62:** `=D44`
- **E62:** `=D37-(D62+C62)`
- **C63:** `=C38`
- **D63:** `=C44`
- **E63:** `=C37-(D63+C63)`

---

## Sheet: Laundry

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20,Unnamed: 21
,System Inputs,,,,,,,,System Outputs,,,,,,,,,,,Sheet Key,
,Value,Unit,Description,,,,,,Value,Unit,Description,,,Used for,,,,,,Input field,
,1,-,Factor of safety applied to total energy required,,,,,,0,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field,
,24,hr / day,Max operation time / day,,,,,,757.1538462,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,,
,0.2,cycles / day,"Defined in User Matrix, used here for water calc",,,,,,757.1538462,Wh,Total energy / day w/o factor of safety applied,,,,,,,,,,
,1440,min,Max single cycle duration,,,,,,4.12,Gal,Total water / day w/o factor of safety applied,,,-,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,
,,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations,
Selected?,Component,Make,Model,Water Used (gal/cycle),Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget,Water Used per Day (Gal)
False,Front Load Washer/Condenser Dryer Combo,GE,GFQ14ESSNWW,20.6,120,0,15,0,1,0.2,0,0,0,0,0,0,1800,0,346.1538462,0,4.12
False,Ultra Capacity Washer Ventless Heat Pump Dryer Combo,Samsung,WD53DBA900HZA1 / WD53DBA900HZA1,0,120,0,15,0,0,0.2,0,0,0,0,0,0,0,0,0,0,0
False,Tankless water heater,Camplux,8kw,,240,0,33.4,0,1,0.2,0,15,0.25,0.05,0,0,8016,0,400.8,0.5293508077,0
False,Water pump,SHURflo,4048-153-E75 / 4048-153-A75,,12,0,8.5,0,1,0.2,0,30,0.5,0.1,0,0,102,0,10.2,0.01347150259,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,,,,,,,,,,,,,,,,,,,,,
,Appliance Energy Calcs,,,,,,,,,,,,,,,,,,,,
,GE Washer/Dryer,,,,,,,,,,,,,,,,,,,,
,Energy Consumption [kWh per yr],Energy per laundry load [Wh],,,,,,,,,,,,,,,,,,,
,108,346.1538462,,,,,,,,,,,,,,,,,,,
,Water consumption per load [gal],20.6,,,,,,,,,,,,,,,,,,,
,Samsung Washer/Dryer,,,,,,,,,,,,,,,,,,,,
,Washer energy per load [kWh],0.3491525424,,,,,,,,,,,,,,,,,,,
,Dryer energy per laod [kWh],1.127208481,,,,,,,,,,,,,,,,,,,
,Energy per load washed and dryed [Wh],1476.361023,,,,,,,,,,,,,,,,,,,

```

### Formulas Used

- **J4:** `=SUMPRODUCT(I12:I23,J12:J23)`
- **J5:** `=$B$4 * J6`
- **B6:** `='User Matrix'!G51`
- **J6:** `=SUM(S12:T16)`
- **B7:** `=60*24`
- **J7:** `=SUM(V12:V16)`
- **E12:** `=20.6*J12`
- **K12:** `=B6`
- **N12:** `=M12/60`
- **O12:** `=K12*N12`
- **R12:** `=PRODUCT(F12,H12,J12)`
- **S12:** `=Q12*P12`
- **T12:** `=C21*J12`
- **U12:** `=(O12*R12+P12*Q12) / $J$6`
- **V12:** `=E12*K12*J12`
- **E13:** `=(4500/295)*J13`
- **K13:** `=B6`
- **M13:** `=L13/60`
- **N13:** `=M13/60`
- **O13:** `=K13*N13`
- **P13:** `=IF(G13 = 0, 0, $B$5-O13)`
- **Q13:** `=PRODUCT(F13,G13,J13)`
- **R13:** `=PRODUCT(F13,H13,J13)`
- **S13:** `=Q13*P13`
- **T13:** `=C26*J13`
- **U13:** `=(O13*R13+P13*Q13) / $J$6`
- **V13:** `=E13*K13*J13`
- **K14:** `=B6`
- **N14:** `=M14/60`
- **O14:** `=K14*N14`
- **P14:** `=IF(G14 = 0, 0, $B$5-O14)`
- **Q14:** `=PRODUCT(F14,G14,J14)`
- **R14:** `=PRODUCT(F14,H14,J14)`
- **S14:** `=Q14*P14`
- **T14:** `=R14*O14`
- **U14:** `=(O14*R14+P14*Q14) / $J$6`
- **V14:** `=E14*K14*J14`
- **K15:** `=B6`
- **N15:** `=M15/60`
- **O15:** `=K15*N15`
- **P15:** `=IF(G15 = 0, 0, $B$5-O15)`
- **Q15:** `=PRODUCT(F15,G15,J15)`
- **R15:** `=PRODUCT(F15,H15,J15)`
- **S15:** `=Q15*P15`
- **T15:** `=R15*O15*J15`
- **U15:** `=(O15*R15+P15*Q15) / $J$6`
- **V15:** `=E15*K15*J15`
- **M16:** `=L16/60`
- **N16:** `=M16/60`
- **O16:** `=K16*N16`
- **P16:** `=IF(G16 = 0, 0, $B$5-O16)`
- **Q16:** `=PRODUCT(F16,G16,J16)`
- **R16:** `=PRODUCT(F16,H16,J16)`
- **S16:** `=Q16*P16`
- **T16:** `=R16*O16`
- **U16:** `=(O16*R16+P16*Q16) / $J$6`
- **V16:** `=E16*K16*J16`
- **C21:** `=B21/(6*52)*1000`
- **C24:** `=103/295`
- **C25:** `=319/283`
- **C26:** `=SUM(C24:C25)*1000`

---

## Sheet: Actuation

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18
System Inputs,,,,,,,System Outputs,,,,,,,,,,,Sheet Key
Value,Unit,Description,,,,,Value,Unit,Description,,,Used for,,,,,,Input field
1,-,Factor of safety applied to total energy required,,,,,69.195,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field
24,hr / day,Max operation time / day,,,,,49.7134,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,
1440,min,Max single cycle duration,,,,,49.7134,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,
,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,
,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Component,Make,Model,Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
Side room floor actuators,,,24,0,1.4,2.2,1,1,30,0.5,0.008333333333,0.008333333333,0,0,33.6,0,0.28,0.005632284253
Side room wall actuators,,,24,0,1.1,1.1,1,1,30,0.5,0.008333333333,0.008333333333,0,0,26.4,0,0.22,0.004425366199
Front room actuators,,,24,0,0.427,0.7,1,1,30,0.5,0.008333333333,0.008333333333,0,0,10.248,0,0.0854,0.001717846697
Rear room actuators,,,24,0,0.61,1,1,1,30,0.5,0.008333333333,0.008333333333,0,0,14.64,0,0.122,0.00245406671
Chassis leveling jacks,,,24,0,9.3,0,4,1,10,0.1666666667,0.002777777778,0.002777777778,0,0,892.8,0,2.48,0.04988594624
Room support jacks,Thomson,HD12B017-1000EXX2EESD,12,0,15,18,1,1,30,0.5,0.008333333333,0.008333333333,0,0,180,0,1.5,0.03017295136
Gearage actuators,,,24,0,0.13,0.195,1,1,30,0.5,0.008333333333,0.008333333333,0,0,3.12,0,0.026,0.0005229978235
Air Compressor,Valid,Valid AAC04A001-02,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
Awning,RecPro,RP-PAFRM-W,12,0,10,15,1,1,0,1,0.01666666667,0.01666666667,0,0,120,0,2,0.04023060181
Furniture automation,estimate,estimate,120,0,10,15,1,1,0,1,0.01666666667,0.01666666667,0,0,1200,0,20,0.4023060181
TV Rise systems,Nexus 21,L-27,120,0,3.5,8,2,1,0,1,0.01666666667,0.01666666667,0,0,840,0,14,0.2816142127
Electric Tongue Jack,Stromberg Carlson,JET-5000,12,0,30,0,1,1,0,1.5,0.025,0.025,0,0,360,0,9,0.1810377081
Motor controllers,Kollmorgan,TBD,12,0,1.25,0,8,1,0,0.5,0.008333333333,0.008333333333,0,0,120,0,1,0.0201153009

```

### Formulas Used

- **H4:** `=SUMPRODUCT(G12:G22,H12:H22)`
- **H5:** `=$A$4 * H7`
- **H7:** `=SUM(Q12:R23)`
- **K12:** `=J12/60`
- **L12:** `=K12/60`
- **M12:** `=I12*L12`
- **N12:** `=IF(E12 = 0, 0, $A$5-M12)`
- **O12:** `=PRODUCT(D12,E12,H12)`
- **P12:** `=PRODUCT(D12,F12,H12)`
- **Q12:** `=O12*N12`
- **R12:** `=P12*M12`
- **S12:** `=(M12*P12+N12*O12) / $H$7`
- **K13:** `=J13/60`
- **L13:** `=K13/60`
- **M13:** `=I13*L13`
- **N13:** `=IF(E13 = 0, 0, $A$5-M13)`
- **O13:** `=PRODUCT(D13,E13,H13)`
- **P13:** `=PRODUCT(D13,F13,H13)`
- **Q13:** `=O13*N13`
- **R13:** `=P13*M13`
- **S13:** `=(M13*P13+N13*O13) / $H$7`
- **F14:** `=0.7*F15`
- **G14:** `=0.7*G15`
- **K14:** `=J14/60`
- **L14:** `=K14/60`
- **M14:** `=I14*L14`
- **N14:** `=IF(E14 = 0, 0, $A$5-M14)`
- **O14:** `=PRODUCT(D14,E14,H14)`
- **P14:** `=PRODUCT(D14,F14,H14)`
- **Q14:** `=O14*N14`
- **R14:** `=P14*M14`
- **S14:** `=(M14*P14+N14*O14) / $H$7`
- **K15:** `=J15/60`
- **L15:** `=K15/60`
- **M15:** `=I15*L15`
- **N15:** `=IF(E15 = 0, 0, $A$5-M15)`
- **O15:** `=PRODUCT(D15,E15,H15)`
- **P15:** `=PRODUCT(D15,F15,H15)`
- **Q15:** `=O15*N15`
- **R15:** `=P15*M15`
- **S15:** `=(M15*P15+N15*O15) / $H$7`
- **K16:** `=J16/60`
- **L16:** `=K16/60`
- **M16:** `=I16*L16`
- **N16:** `=IF(E16 = 0, 0, $A$5-M16)`
- **O16:** `=PRODUCT(D16,E16,H16)`
- **P16:** `=PRODUCT(D16,F16,H16)`
- **Q16:** `=O16*N16`
- **R16:** `=P16*M16`
- **S16:** `=(M16*P16+N16*O16) / $H$7`
- **K17:** `=J17/60`
- **L17:** `=K17/60`
- **M17:** `=I17*L17`
- **N17:** `=IF(E17 = 0, 0, $A$5-M17)`
- **O17:** `=PRODUCT(D17,E17,H17)`
- **P17:** `=PRODUCT(D17,F17,H17)`
- **Q17:** `=O17*N17`
- **R17:** `=P17*M17`
- **S17:** `=(M17*P17+N17*O17) / $H$7`
- **G18:** `=F18*1.5`
- **K18:** `=J18/60`
- **L18:** `=K18/60`
- **M18:** `=I18*L18`
- **N18:** `=IF(E18 = 0, 0, $A$5-M18)`
- **O18:** `=PRODUCT(D18,E18,H18)`
- **P18:** `=PRODUCT(D18,F18,H18)`
- **Q18:** `=O18*N18`
- **R18:** `=P18*M18`
- **S18:** `=(M18*P18+N18*O18) / $H$7`
- **K19:** `=J19/60`
- **L19:** `=K19/60`
- **M19:** `=I19*L19`
- **N19:** `=IF(E19 = 0, 0, $A$5-M19)`
- **O19:** `=PRODUCT(D19,E19,H19)`
- **P19:** `=PRODUCT(D19,F19,H19)`
- **Q19:** `=O19*N19`
- **R19:** `=P19*M19`
- **S19:** `=(M19*P19+N19*O19) / $H$7`
- **L20:** `=K20/60`
- **M20:** `=I20*L20`
- **N20:** `=IF(E20 = 0, 0, $A$5-M20)`
- **O20:** `=PRODUCT(D20,E20,H20)`
- **P20:** `=PRODUCT(D20,F20,H20)`
- **Q20:** `=O20*N20`
- **R20:** `=P20*M20`
- **S20:** `=(M20*P20+N20*O20) / $H$7`
- **L21:** `=K21/60`
- **M21:** `=I21*L21`
- **N21:** `=IF(E21 = 0, 0, $A$5-M21)`
- **O21:** `=PRODUCT(D21,E21,H21)`
- **P21:** `=PRODUCT(D21,F21,H21)`
- **Q21:** `=O21*N21`
- **R21:** `=P21*M21`
- **S21:** `=(M21*P21+N21*O21) / $H$7`
- **L22:** `=K22/60`
- **M22:** `=I22*L22`
- **N22:** `=IF(E22 = 0, 0, $A$5-M22)`
- **O22:** `=PRODUCT(D22,E22,H22)`
- **P22:** `=PRODUCT(D22,F22,H22)`
- **Q22:** `=O22*N22`
- **R22:** `=P22*M22`
- **S22:** `=(M22*P22+N22*O22) / $H$7`
- **L23:** `=K23/60`
- **M23:** `=I23*L23`
- **N23:** `=IF(E23 = 0, 0, $A$5-M23)`
- **O23:** `=PRODUCT(D23,E23,H23)`
- **P23:** `=PRODUCT(D23,F23,H23)`
- **Q23:** `=O23*N23`
- **R23:** `=P23*M23`
- **S23:** `=(M23*P23+N23*O23) / $H$7`
- **F24:** `=15/D24`
- **L24:** `=K24/60`
- **M24:** `=I24*L24`
- **N24:** `=IF(E24 = 0, 0, $A$5-M24)`
- **O24:** `=PRODUCT(D24,E24,H24)`
- **P24:** `=PRODUCT(D24,F24,H24)`
- **Q24:** `=O24*N24`
- **R24:** `=P24*M24`
- **S24:** `=(M24*P24+N24*O24) / $H$7`

---

## Sheet: Non-Potable Water

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
,System Inputs,,,,,,,,System Outputs,,,,,,,,,,,Sheet Key
,Value,Unit,Description,,,,,,Value,Unit,Description,,,Used for,,,,,,Input field
,1,-,Factor of safety applied to total energy required,,,,,,0,A,Maximum total current draw,,,,,,,,,Output / calculated field
,24,hr / day,Max operation time / day,,,,,,0,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,0,Wh,Total energy / day w/o factor of safety applied,,,,,,,,,
,1440,min,Max single cycle duration,,,,,,0,Gal,Local source fresh water collected,,,-,,,,,,
,,,,,,,,,0,Gal,Grey-water expelled,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Selected?,Component,Make,Model,Water (gal/cycle),Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
False,Off-Grid Local Source Water Pump (P1),Aquatec,5513-1E12-J526,,120,0,1.75,0,0,0,0,4,0.06666666667,0,0,0,0,0,0,
False,Off-Grid Local Source Water Pump (P1),Everflow,EF5500,,12,0,17,17,0,1,0,4,0.06666666667,0.06666666667,0,0,0,0,0,
False,Rain water pump (P2),Whale Pumps,Gulper 220,,12,0,2.4,0,0,1,0,0,0,0,0,0,0,0,0,
False,UV Water System(5),Viqua,VT4,,12,0,1.8,0,0,1,0,0,0,0,0,0,0,0,0,
False,Pressurised greywater spigot pump (P8),Whale Pumps,Gupler 220,,12,0,2.4,0,0,1,0,1.351351351,0.02252252252,0.02252252252,0,0,0,0,0,
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,

```

### Formulas Used

- **J4:** `=SUMPRODUCT(H12:H17,J12:J17)`
- **J5:** `=$B$4 * J6`
- **J6:** `=SUM(S12:T17)`
- **J7:** `=-(5*M12*J12)`
- **J8:** `=-(3.7*M16*J16)`
- **M12:** `='User Matrix'!$G$64/5`
- **N12:** `=M12/60`
- **O12:** `=K12*N12`
- **P12:** `=IF(G12 = 0, 0, $B$5-O12)`
- **Q12:** `=PRODUCT(F12,G12,J12)`
- **R12:** `=PRODUCT(F12,H12,J12)`
- **S12:** `=Q12*P12`
- **T12:** `=R12*O12`
- **U12:** `=IF($J$6>0,(O12*R12+P12*Q12) / $J$6,"N/A")`
- **M13:** `='User Matrix'!$G$64/5`
- **N13:** `=M13/60`
- **O13:** `=K13*N13`
- **P13:** `=IF(G13 = 0, 0, $B$5-O13)`
- **Q13:** `=PRODUCT(F13,G13,J13)`
- **R13:** `=PRODUCT(F13,H13,J13)`
- **S13:** `=Q13*P13`
- **T13:** `=R13*O13`
- **U13:** `=IF($J$6>0,(O13*R13+P13*Q13) / $J$6,"N/A")`
- **N14:** `=M14/60`
- **O14:** `=K14*N14`
- **P14:** `=IF(G14 = 0, 0, $B$5-O14)`
- **Q14:** `=PRODUCT(F14,G14,J14)`
- **R14:** `=PRODUCT(F14,H14,J14)`
- **S14:** `=Q14*P14`
- **T14:** `=R14*O14`
- **U14:** `=IF($J$6>0,(O14*R14+P14*Q14) / $J$6,"N/A")`
- **N15:** `=M15/60`
- **O15:** `=K15*N15`
- **P15:** `=IF(G15 = 0, 0, $B$5-O15)`
- **Q15:** `=PRODUCT(F15,G15,J15)`
- **R15:** `=PRODUCT(F15,H15,J15)`
- **S15:** `=Q15*P15`
- **T15:** `=R15*O15`
- **U15:** `=IF($J$6>0,(O15*R15+P15*Q15) / $J$6,"N/A")`
- **M16:** `='User Matrix'!G65/3.7`
- **N16:** `=M16/60`
- **O16:** `=K16*N16`
- **P16:** `=IF(G16 = 0, 0, $B$5-O16)`
- **Q16:** `=PRODUCT(F16,G16,J16)`
- **R16:** `=PRODUCT(F16,H16,J16)`
- **S16:** `=Q16*P16`
- **T16:** `=R16*O16`
- **U16:** `=IF($J$6>0,(O16*R16+P16*Q16) / $J$6,"N/A")`
- **M17:** `=L17/60`
- **N17:** `=M17/60`
- **O17:** `=K17*N17`
- **P17:** `=IF(G17 = 0, 0, $B$5-O17)`
- **Q17:** `=PRODUCT(F17,G17,J17)`
- **R17:** `=PRODUCT(F17,H17,J17)`
- **S17:** `=Q17*P17`
- **T17:** `=R17*O17`
- **U17:** `=IF($J$6>0,(O17*R17+P17*Q17) / $J$6,"N/A")`

---

## Sheet: Dumping

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19
,System Inputs,,,,,,,System Outputs,,,,,,,,,,,Sheet Key
,Value,Unit,Description,,,,,Value,Unit,Description,,,Used for,,,,,,Input field
,1,-,Factor of safety applied to total energy required,,,,,0,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field
,24,hr / day,Max operation time / day,,,,,0.05,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,
,45,min,Max single cycle duration,,,,,0.05,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Selected?,Component,Make,Model,Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
False,Electric Waste Valves,Valterra,E85-8,12,0,2.5,0,1,4,1.5,0.025,0.0004166666667,0.001666666667,0,0,30,0,0.05,1
False,Grey water pump (P9),Whale Pumps,Gulper 220,12,0,2.4,0,0,1,0,14.86486486,0.2477477477,0.2477477477,0,0,0,0,0,0
False,Macerating pump,Pentair,3200-001,12,0,17,0,0,0,0,7.692307692,0.1282051282,0,0,0,0,0,0,0
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H15,I12:I15)`
- **I5:** `=$B$4 * I7`
- **B7:** `=0.75*60`
- **I7:** `=SUM(R12:S15)`
- **L12:** `=K12/60`
- **M12:** `=L12/60`
- **N12:** `=J12*M12`
- **O12:** `=IF(F12 = 0, 0, $B$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=PRODUCT(E12,G12,I12)`
- **R12:** `=P12*O12`
- **S12:** `=Q12*N12`
- **T12:** `=(N12*Q12+O12*P12) / $I$7`
- **L13:** `=55/3.7`
- **M13:** `=L13/60`
- **N13:** `=J13*M13`
- **O13:** `=IF(F13 = 0, 0, $B$5-N13)`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `=PRODUCT(E13,G13,I13)`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13`
- **T13:** `=(N13*Q13+O13*P13) / $I$7`
- **L14:** `=100/13`
- **M14:** `=L14/60`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $B$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$7`
- **L15:** `=K15/60`
- **M15:** `=L15/60`
- **N15:** `=J15*M15`
- **O15:** `=IF(F15 = 0, 0, $B$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$7`

---

## Sheet: TEMP- Hot

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
,System Inputs,,,,,Sheet Key,,,System Outputs,,,,,,,,,,,
,Value,Unit,Description,,,Input field,,,Value,Unit,Description,,,Used for,,,,,,
,1,-,Factor of safety applied to total energy required,,,Output / calculated field,,,0,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,
,24,hr / day,Max operation time / day,,,,,,6923.755102,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,,
,1440,min,Max single cycle duration,,,,,,6923.755102,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,
,,,,,,,,,0.589,,Duty Cycle,Defined in user matrix,,Energy & Water outputs,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Selected?,Component,Make,Model,Water Generated (gal/hr),Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
False,Mini-Split HVAC,MrCool DIY,"4th Gen Multi-Zone 2-Zone 18,000 BTU 21 SEER (9K + 12K)",0,240,0,4.081632653,0,1,1,0,0,0,7.068,0,0,979.5918367,0,6923.755102,1
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,,,,,,,,,,,,,,,,,,,,
,Air Conditioning Power Demand,,,,,,,,,,,,,,,,,,,
,HVAC Unit,BTU/h,SEER,EER,Watts,,,,,,,,,,,,,,,
,MrCool DIY,18000,21,18.375,979.5918367,,,,,,,,,,,,,,,

```

### Formulas Used

- **J4:** `=SUMPRODUCT(I12:I32,J12:J32)`
- **J5:** `=$B$4 * J7`
- **J7:** `=SUM(S12:T24)`
- **J8:** `='User Matrix'!G62`
- **E12:** `='Lookup Tables'!C13`
- **H12:** `=R12/F12`
- **O12:** `=Summary!E7 * J8`
- **P12:** `=IF(G12 = 0, 0, $B$5-O12)`
- **Q12:** `=PRODUCT(F12,G12,J12)`
- **R12:** `=F28`
- **S12:** `=Q12*P12`
- **T12:** `=R12*O12*J12`
- **U12:** `=(O12*R12+P12*Q12) / $J$7`
- **G13:** `=H13`
- **M13:** `=L13/60`
- **N13:** `=M13/60`
- **O13:** `=K13*N13`
- **P13:** `=IF(G13 = 0, 0, $B$5-O13)`
- **Q13:** `=PRODUCT(F13,G13,J13)`
- **R13:** `=PRODUCT(F13,H13,J13)`
- **S13:** `=Q13*P13`
- **T13:** `=R13*O13`
- **U13:** `=(O13*R13+P13*Q13) / $J$7`
- **M14:** `=L14/60`
- **N14:** `=M14/60`
- **O14:** `=K14*N14`
- **P14:** `=IF(G14 = 0, 0, $B$5-O14)`
- **Q14:** `=PRODUCT(F14,G14,J14)`
- **R14:** `=PRODUCT(F14,H14,J14)`
- **S14:** `=Q14*P14`
- **T14:** `=R14*O14`
- **U14:** `=(O14*R14+P14*Q14) / $J$7`
- **M15:** `=L15/60`
- **N15:** `=M15/60`
- **O15:** `=K15*N15`
- **P15:** `=IF(G15 = 0, 0, $B$5-O15)`
- **Q15:** `=PRODUCT(F15,G15,J15)`
- **R15:** `=PRODUCT(F15,H15,J15)`
- **S15:** `=Q15*P15`
- **T15:** `=R15*O15`
- **U15:** `=(O15*R15+P15*Q15) / $J$7`
- **M16:** `=L16/60`
- **N16:** `=M16/60`
- **O16:** `=K16*N16`
- **P16:** `=IF(G16 = 0, 0, $B$5-O16)`
- **Q16:** `=PRODUCT(F16,G16,J16)`
- **R16:** `=PRODUCT(F16,H16,J16)`
- **S16:** `=Q16*P16`
- **T16:** `=R16*O16`
- **U16:** `=(O16*R16+P16*Q16) / $J$7`
- **M17:** `=L17/60`
- **N17:** `=M17/60`
- **O17:** `=K17*N17`
- **P17:** `=IF(G17 = 0, 0, $B$5-O17)`
- **Q17:** `=PRODUCT(F17,G17,J17)`
- **R17:** `=PRODUCT(F17,H17,J17)`
- **S17:** `=Q17*P17`
- **T17:** `=R17*O17`
- **M18:** `=L18/60`
- **N18:** `=M18/60`
- **O18:** `=K18*N18`
- **P18:** `=IF(G18 = 0, 0, $B$5-O18)`
- **Q18:** `=PRODUCT(F18,G18,J18)`
- **R18:** `=PRODUCT(F18,H18,J18)`
- **S18:** `=Q18*P18`
- **T18:** `=R18*O18`
- **U18:** `=(O18*R18+P18*Q18) / $J$7`
- **M19:** `=L19/60`
- **N19:** `=M19/60`
- **O19:** `=K19*N19`
- **P19:** `=IF(G19 = 0, 0, $B$5-O19)`
- **Q19:** `=PRODUCT(F19,G19,J19)`
- **R19:** `=PRODUCT(F19,H19,J19)`
- **S19:** `=Q19*P19`
- **T19:** `=R19*O19`
- **U19:** `=(O19*R19+P19*Q19) / $J$7`
- **M20:** `=L20/60`
- **N20:** `=M20/60`
- **O20:** `=K20*N20`
- **P20:** `=IF(G20 = 0, 0, $B$5-O20)`
- **Q20:** `=PRODUCT(F20,G20,J20)`
- **R20:** `=PRODUCT(F20,H20,J20)`
- **S20:** `=Q20*P20`
- **T20:** `=R20*O20`
- **U20:** `=(O20*R20+P20*Q20) / $J$7`
- **M21:** `=L21/60`
- **N21:** `=M21/60`
- **O21:** `=K21*N21`
- **P21:** `=IF(G21 = 0, 0, $B$5-O21)`
- **Q21:** `=PRODUCT(F21,G21,J21)`
- **R21:** `=PRODUCT(F21,H21,J21)`
- **S21:** `=Q21*P21`
- **T21:** `=R21*O21`
- **U21:** `=(O21*R21+P21*Q21) / $J$7`
- **M22:** `=L22/60`
- **N22:** `=M22/60`
- **O22:** `=K22*N22`
- **P22:** `=IF(G22 = 0, 0, $B$5-O22)`
- **Q22:** `=PRODUCT(F22,G22,J22)`
- **R22:** `=PRODUCT(F22,H22,J22)`
- **S22:** `=Q22*P22`
- **T22:** `=R22*O22`
- **U22:** `=(O22*R22+P22*Q22) / $J$7`
- **M23:** `=L23/60`
- **N23:** `=M23/60`
- **O23:** `=K23*N23`
- **P23:** `=IF(G23 = 0, 0, $B$5-O23)`
- **Q23:** `=PRODUCT(F23,G23,J23)`
- **R23:** `=PRODUCT(F23,H23,J23)`
- **S23:** `=Q23*P23`
- **T23:** `=R23*O23`
- **U23:** `=(O23*R23+P23*Q23) / $J$7`
- **M24:** `=L24/60`
- **N24:** `=M24/60`
- **O24:** `=K24*N24`
- **P24:** `=IF(G24 = 0, 0, $B$5-O24)`
- **Q24:** `=PRODUCT(F24,G24,J24)`
- **R24:** `=PRODUCT(F24,H24,J24)`
- **S24:** `=Q24*P24`
- **T24:** `=R24*O24`
- **U24:** `=(O24*R24+P24*Q24) / $J$7`
- **E28:** `=D28*0.875`
- **F28:** `=C28/E28`

---

## Sheet: TEMP- Temperate

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
,System Inputs,,,,,,,System Outputs,,,,,,,,,,,Sheet Key,
,Value,Unit,Description,,,,,Value,Unit,Description,,,Used for,,,,,,Input field,
,1,-,Factor of safety applied to total energy required,,,,,0,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field,
,24,hr / day,Max operation time / day,,,,,744.6801315,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,,
,1440,min,Max single cycle duration,,,,,744.6801315,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,,
,,,,,,,,0.1395,,Duty cycle,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Pwr (W),,Device Energy (Wh),,,
Selected?,Component,Make,Model,Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget,Notes
False,Mini-Split HVAC,MrCool DIY,"4th Gen Multi-Zone 2-Zone 18,000 BTU 21 SEER (9K + 12K)",240,0,4.081632653,0,1,1,0,0,1.674,1.674,0,0,979.5918367,0,1639.836735,2.2020686,Air Conditioner
False,Mini-Split HVAC,MrCool DIY,"4th Gen Multi-Zone 2-Zone 18,000 BTU 21 SEER (9K + 12K)",240,0,9.205426357,0,1,1,0,0,1.674,1.674,0,0,2209.302326,0,3698.372093,4.966390181,Heater
False,,,,,0,0,0,0,0,0,15,0.25,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H30,I12:I30)`
- **I5:** `=$B$4 * I7`
- **I7:** `=SUM(R12:S24)*I8`
- **I8:** `='User Matrix'!G63`
- **G12:** `=Q12/E12`
- **M12:** `=Summary!$E$7 * $I$8`
- **N12:** `=J12*M12`
- **O12:** `=IF(F12 = 0, 0, $B$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `='TEMP- Hot'!F28`
- **R12:** `=P12*O12`
- **S12:** `=Q12*N12*I12`
- **T12:** `=(N12*Q12+O12*P12) / $I$7`
- **G13:** `=Q13/E13`
- **M13:** `=Summary!$E$7 * $I$8`
- **N13:** `=J13*M13`
- **O13:** `=IF(F13 = 0, 0, $B$5-N13)`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `='TEMP- Cold'!E16`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13*I13`
- **T13:** `=(N13*Q13+O13*P13) / $I$7`
- **M14:** `=L14/60`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $B$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$7`
- **L15:** `=K15/60`
- **M15:** `=L15/60`
- **N15:** `=J15*M15`
- **O15:** `=IF(F15 = 0, 0, $B$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$7`
- **L16:** `=K16/60`
- **M16:** `=L16/60`
- **N16:** `=J16*M16`
- **O16:** `=IF(F16 = 0, 0, $B$5-N16)`
- **P16:** `=PRODUCT(E16,F16,I16)`
- **Q16:** `=PRODUCT(E16,G16,I16)`
- **R16:** `=P16*O16`
- **S16:** `=Q16*N16`
- **T16:** `=(N16*Q16+O16*P16) / $I$7`
- **L17:** `=K17/60`
- **M17:** `=L17/60`
- **N17:** `=J17*M17`
- **O17:** `=IF(F17 = 0, 0, $B$5-N17)`
- **P17:** `=PRODUCT(E17,F17,I17)`
- **Q17:** `=PRODUCT(E17,G17,I17)`
- **R17:** `=P17*O17`
- **S17:** `=Q17*N17`
- **L18:** `=K18/60`
- **M18:** `=L18/60`
- **N18:** `=J18*M18`
- **O18:** `=IF(F18 = 0, 0, $B$5-N18)`
- **P18:** `=PRODUCT(E18,F18,I18)`
- **Q18:** `=PRODUCT(E18,G18,I18)`
- **R18:** `=P18*O18`
- **S18:** `=Q18*N18`
- **T18:** `=(N18*Q18+O18*P18) / $I$7`
- **L19:** `=K19/60`
- **M19:** `=L19/60`
- **N19:** `=J19*M19`
- **O19:** `=IF(F19 = 0, 0, $B$5-N19)`
- **P19:** `=PRODUCT(E19,F19,I19)`
- **Q19:** `=PRODUCT(E19,G19,I19)`
- **R19:** `=P19*O19`
- **S19:** `=Q19*N19`
- **T19:** `=(N19*Q19+O19*P19) / $I$7`
- **L20:** `=K20/60`
- **M20:** `=L20/60`
- **N20:** `=J20*M20`
- **O20:** `=IF(F20 = 0, 0, $B$5-N20)`
- **P20:** `=PRODUCT(E20,F20,I20)`
- **Q20:** `=PRODUCT(E20,G20,I20)`
- **R20:** `=P20*O20`
- **S20:** `=Q20*N20`
- **T20:** `=(N20*Q20+O20*P20) / $I$7`
- **L21:** `=K21/60`
- **M21:** `=L21/60`
- **N21:** `=J21*M21`
- **O21:** `=IF(F21 = 0, 0, $B$5-N21)`
- **P21:** `=PRODUCT(E21,F21,I21)`
- **Q21:** `=PRODUCT(E21,G21,I21)`
- **R21:** `=P21*O21`
- **S21:** `=Q21*N21`
- **T21:** `=(N21*Q21+O21*P21) / $I$7`
- **L22:** `=K22/60`
- **M22:** `=L22/60`
- **N22:** `=J22*M22`
- **O22:** `=IF(F22 = 0, 0, $B$5-N22)`
- **P22:** `=PRODUCT(E22,F22,I22)`
- **Q22:** `=PRODUCT(E22,G22,I22)`
- **R22:** `=P22*O22`
- **S22:** `=Q22*N22`
- **T22:** `=(N22*Q22+O22*P22) / $I$7`
- **L23:** `=K23/60`
- **M23:** `=L23/60`
- **N23:** `=J23*M23`
- **O23:** `=IF(F23 = 0, 0, $B$5-N23)`
- **P23:** `=PRODUCT(E23,F23,I23)`
- **Q23:** `=PRODUCT(E23,G23,I23)`
- **R23:** `=P23*O23`
- **S23:** `=Q23*N23`
- **T23:** `=(N23*Q23+O23*P23) / $I$7`
- **L24:** `=K24/60`
- **M24:** `=L24/60`
- **N24:** `=J24*M24`
- **O24:** `=IF(F24 = 0, 0, $B$5-N24)`
- **P24:** `=PRODUCT(E24,F24,I24)`
- **Q24:** `=PRODUCT(E24,G24,I24)`
- **R24:** `=P24*O24`
- **S24:** `=Q24*N24`
- **T24:** `=(N24*Q24+O24*P24) / $I$7`

---

## Sheet: TEMP- Cold

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19
,System Inputs,,,,,,,System Outputs,,,,,,,,,,,Sheet Key
,Value,Unit,Description,,,,,Value,Unit,Description,,,Used for,,,,,,Input field
,1,-,Factor of safety applied to total energy required,,,,,0,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field
,24,hr / day,Max operation time / day,,,,,15615.34884,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,
,1440,min,Max single cycle duration,,,,,15615.34884,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,
,,,,,,,,0.589,,Duty Cycle,,,,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Selected?,Component,Make,Model,Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
False,Mini-Split HVAC,Mr Cool DIY,"4th Gen Multi-Zone 2-Zone 18,000 BTU 21 SEER (9K + 12K)",240,0,9.205426357,0,1,1,0,0,0,7.068,0,0,2209.302326,0,15615.34884,1
False,,,,,,,,,,,,,,,,,,,
False,Heater Power Consumption,,,,,,,,,,,,,,,,,,
False,Component,Heating Capacity (BTU/h),"HSPF, Zone 4 vs 5",Power Consumption (Watts),,,,,,,,,,,,,,,
False,MrCoolDIY,19000,8.6,2209.302326,,,,,,,,,,,,,,,
False,MrCoolDIY,19000,10.6,1792.45283,,,,,,,,,,,,,,,

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12,I12)`
- **I5:** `=$B$4 * I7`
- **I7:** `=SUM(R12:S12)`
- **I8:** `='User Matrix'!G62`
- **G12:** `=Q12/E12`
- **N12:** `=Summary!$E$7 * $I$8`
- **O12:** `=IF(F12 = 0, 0, $B$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=E16`
- **R12:** `=P12*O12`
- **S12:** `=Q12*N12*I12`
- **T12:** `=(N12*Q12+O12*P12) / $I$7`
- **E16:** `=C16/D16`
- **E17:** `=C17/D17`

---

## Sheet: Solar

### CSV Data
```csv
Mfr,P/N,Description,Length (meters),Width (meters),Area (meters2),Power Temp Coefficient -%/°C,Pmax [W],Efficiency,Ideal Output (W),Calculated PMax using Datasheet Area,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20,Unnamed: 21,Unnamed: 22,Unnamed: 23,Unnamed: 24,Unnamed: 25,Unnamed: 26,Unnamed: 27,Unnamed: 28,Unnamed: 29
Sungold,SG-TF-S-150W,PV,1.31,0.52,0.6812,0.0027,150.0,0.244,36.6,166.2128,,Existing Trailer Area,,,,,,Energy Produced from Solar per Sunlight & Temp Condition (Wh / day),,,,,,,,,,,
Ensun,EN450-36V-MH,PVT,2.095,1.038,2.17461,0.0027,450.0,0.207,93.15,450.14427,,,Length [m],Width [m],Area [m2],Area [ft2],,Solar Insolation  * panel area  * PV efficiency factor (with temp coefficient included) * tilt factor * number of panels * general system losses,,,,,,,,,,,
,,,,,,,,,,,,Main cabin,4.265,2.24,9.5536,102.833995,,,Dry,Comfortable,Humid,,Sunlight Factor (Lookup Table),,,,,,
,,,,,,,,,,,,,,,,,,Hot,48363.13254,28401.86346,21062.94911,,Hi- Sunny,1.0,,,,,
,,,,,,,,,,,,Front popout,1.52,2.28,3.4656,37.30337184,,Temperate,27333.18,25783.38,18923.625,,Mid- Cloudy,0.5,,,,,
,,,,,,,,,,,,Left popout,4.16,1.88,7.8208,84.18230912,,Cold,18134.96828,17044.36082,11780.73212,,Lo- Shady,0.25,,,,,
,,,,,,,,,,,,Right popout,,,0,0,,,Hot = Summer Months,Temperate = Spring / Fall Months,Cold = Winter Months,,,,,,,,
,,,,,,,,,,,,Rear popout,4.165,2.28,9.4962,102.2161472,,,Tilt Factor (Lookup Table),,,,,,,,,,
,,,STC (w/m^2),,,,,,,,,Total Areas,,,,,,,Season,Tilt Factor (inefficiency based on flat mounted panels),,,,,,,,,
,,,1000,,,,,,,,,Expanded [m2],30.3362,Collapsed [m2],9.5536,,,,Winter (December),0.75,,,,,,,,,
,,,,,,,,,,,,Expanded [ft2],326.5358232,Collapsed [ft2],102.833995,,,,Spring / Fall (March),0.8,,,,,,,,,
,,,Estimated Usable Solar Cell Area  (m^2) (based on 150W output),,,,,,,,,,,,,,,,Summer (June),0.8,,,,,,,,,
,,,0.6147540984,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,Solar Area Override,,,,,,"General System Losses (soiling of panels, manufacturing defects, wiring, connections, nameplate rating, light-inducted degredation) based on PVWatts Calculator",,,,,,,,,,,
,,,,,,,,,,,,No. of panels (21) ,35,"From ""TRAILER DESIGNER"" on summary sheet",,,,0.9,,,,,,,,,,,
,,,,,,,,,,,,Total Pmax [W],5250,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,"Humidity vs Temperate (Lookup Table )
(Solar Insolation based on fabhabs.com calculator, cross referenced with Solar Electricity Handbook)",,,,,,,,,,,
,,,,,,,,,,,,Temperature vs PV Efficiency,,,,,,Season,"Solar Insolation - Phoenix - Dry
(Wh/m^2/day)","Solar Insolation - Los Angeles - Comfortable
(Wh/m^2/day)","Solar Insolation - Atlanta - Humid
(Wh/m^2/day)",,,,,,,,
,,,,,,,,,,,,PV Temp Coefficient (efficiency loss per °C),0.0027,,,,,Hot,10022,9514,7526,,,,,Total PVT Area (m^2),8.7,,
,,,,,,,,,,,,°C,°F,Efficiency x Temp Coifficient,,,,Temperate,7231,6821,5340,,,,Photovolataic Thermal Panels (PVT) Output and Heating Time,,,,
,,,,,,,,,,,,0,32,0.3115,,,,Cold,3758,3532,2604,,,,Time,Solar Irradiance in LA (W/m²),Thermal Output (W),Factors applied,Heating Time (Minutes)
,,,,,,,,,,,,1,33.8,0.3088,,,,,,,,,,,00:00:00,0,0,0,
,,,,,,,,,,,,2,35.6,0.3061,,,,,,,,,,,01:00:00,0,0,0,
,,,,,,,,,,,,3,37.4,0.3034,,,,,,,,,,,02:00:00,0,0,0,
,,,,,,,,,,,,4,39.2,0.3007,,,,PVT Thermal Table,,,,,,,03:00:00,0,0,0,
,,,,,,,,,,,,5,41,0.298,,,,"Irradiance Calculation (uses above lookup table to calculate realistic thermal irradiance in different conditions)
Converted to Wh for 4 PVT panels",,,,,,,04:00:00,0,0,0,
,,,,,,,,,,,,6,42.8,0.2953,,,,Season,"Solar Insolation - Phoenix - Dry
(Wh)","Solar Insolation - Los Angeles - Comfortable
(Wh)","Solar Insolation - Atlanta - Humid
(Wh)",,,,05:00:00,0,0,0,
,,,,,,,,,,,,7,44.6,0.2926,,,,Hot,8719.14,3448.825,2728.175,,,,06:00:00,1,0.145,6.96e-05,1000
,,,,,,,,,,,,8,46.4,0.2899,,,,Temperate,2621.2375,2472.6125,1935.75,,,,07:00:00,129,1122.3,0.538704,108.8167157
,,,,,,,,,,,,9,48.2,0.2872,,,,Cold,1362.275,1280.35,943.95,,,,08:00:00,336,2923.2,1.403136,41.7778462
,,,,,,,,,,,,10,50,0.2845,,,,Factors applied from below (kWh),,,,,,,09:00:00,540,4698,2.25504,25.9951043
,,,,,,,,,,,,11,51.8,0.2818,,,,Hot,4.1851872,1.655436,1.309524,,,,10:00:00,696,6055.2,2.906496,20.1686154
,,,,,,,,,,,,12,53.6,0.2791,,,,Temperate,1.258194,1.186854,0.92916,,,,11:00:00,830,7221,3.46608,16.9124775
,,,,,,,,,,,,13,55.4,0.2764,,,,Cold,0.653892,0.614568,0.453096,,,,12:00:00,916,7969.2,3.825216,15.32462481
,,,,,,,,,,,,14,57.2,0.2737,,,,Factors,,,,,,,13:00:00,942,8195.4,3.933792,14.90165215
,,,,,,,,,,,,15,59,0.271,,,,General Factor,Tilt Factor,Shade factor,Incomplete heat transfer factor (glycol),,,,14:00:00,906,7882.2,3.783456,15.49377077
,,,,,,,,,,,,16,60.8,0.2683,,,,0.75,0.8,1,0.8,This one to the left is just for the calorifier,,,15:00:00,810,7047,3.38256,17.33006953
,,,,,,,,,,,,17,62.6,0.2656,,,,,,,,,,,16:00:00,663,5768.1,2.768688,21.17248314
,,,,,,,,,,,,18,64.4,0.2629,,,,Time to heat up 8 Gal water thermally - minutes,,,,,,,17:00:00,479,4167.3,2.000304,29.30554556
,,,,,,,,,,,,19,66.2,0.2602,,,,Season,Solar Insolation - Phoenix - Dry,Solar Insolation - Los Angeles - Comfortable,Solar Insolation - Atlanta - Humid,,,,18:00:00,275,2392.5,1.1484,51.04493208
,,,,,,,,,,,,20,68,0.2575,,,,Hot,14.00654193,35.41061086,44.76435713,,,,19:00:00,77,669.9,0.321552,182.3033289
,,,,,,,,,,,,21,69.8,0.2548,,,,Temperate,46.59058937,49.39107927,63.0892419,,,,20:00:00,0,0,0,1000
,,,,,,,,,,,,22,71.6,0.2521,,,,Cold,89.64783175,95.38407467,129.376556,,,,21:00:00,0,0,0,
,,,,,,,,,,,,23,73.4,0.2494,,,,Time to heat up 8 Gal water electrically (1kW) - minutes,,,,,,,22:00:00,0,0,0,
,,,,,,,,,,,,24,75.2,0.2467,,,,Hot,58.62,58.62,58.62,,,,23:00:00,0,0,0,
,,,,,,,,,,,,25,77,0.244,,,,Temperate,58.62,58.62,58.62,,,,,,,,
,,,,,,,,,,,,26,78.8,0.2413,,,,Cold,58.62,58.62,58.62,,,,,,,,
,,,,,,,,,,,,27,80.6,0.2386,,,,,,,,,,,,,,,
,,,,,,,,,,,,28,82.4,0.2359,,,,,,,,,,,,,,,
,,,,,,,,,,,,29,84.2,0.2332,,,,,,,,,,,,,,,
,,,,,,,,,,,,30,86,0.2305,,,,,,,,,,,,,,,
,,,,,,,,,,,,31,87.8,0.2278,,,,,,,,,,,,,,,
,,,,,,,,,,,,32,89.6,0.2251,,,,,,,,,,,,,,,
,,,,,,,,,,,,33,91.4,0.2224,,,,,,,,,,,,,,,
,,,,,,,,,,,,34,93.2,0.2197,,,,,,,,,,,,,,,
,,,,,,,,,,,,35,95,0.217,,,,,,,,,,,,,,,
,,,,,,,,,,,,36,96.8,0.2143,,,,,,,,,,,,,,,
,,,,,,,,,,,,37,98.6,0.2116,,,,,,,,,,,,,,,
,,,,,,,,,,,,38,100.4,0.2089,,,,,,,,,,,,,,,
,,,,,,,,,,,,39,102.2,0.2062,,,,,,,,,,,,,,,
,,,,,,,,,,,,40,104,0.2035,,,,,,,,,,,,,,,
,,,,,,,,,,,,41,105.8,0.2008,,,,,,,,,,,,,,,
,,,,,,,,,,,,42,107.6,0.1981,,,,,,,,,,,,,,,
,,,,,,,,,,,,43,109.4,0.1954,,,,,,,,,,,,,,,
,,,,,,,,,,,,44,111.2,0.1927,,,,,,,,,,,,,,,
,,,,,,,,,,,,45,113,0.19,,,,,,,,,,,,,,,
,,,,,,,,,,,,46,114.8,0.1873,,,,,,,,,,,,,,,
,,,,,,,,,,,,47,116.6,0.1846,,,,,,,,,,,,,,,
,,,,,,,,,,,,48,118.4,0.1819,,,,,,,,,,,,,,,
,,,,,,,,,,,,49,120.2,0.1792,,,,,,,,,,,,,,,

```

### Formulas Used

- **D2:** `=0.669+0.641`
- **F2:** `=D2*E2`
- **J2:** `=H2*I2`
- **K2:** `=F2*$D$11*I2`
- **F3:** `=D3*E3`
- **J3:** `=H3*I3`
- **K3:** `=F3*$D$11*I3`
- **P4:** `=PRODUCT(N4, O4)`
- **Q4:** `=P4*10.7639`
- **T5:** `=T20*$D$14*O22*$U$13*$N$16*$S$16`
- **U5:** `=U20*$D$14*O66*$U$12*$N$16*$S$16`
- **V5:** `=V20*$D$14*O66*$U$11*$N$16*$S$16`
- **P6:** `=PRODUCT(N6, O6)`
- **Q6:** `=P6*10.7639`
- **T6:** `=T21*$D$14*O47*$U$13*$N$16*$S$16`
- **U6:** `=U21*$D$14*O47*$U$12*$N$16*$S$16`
- **V6:** `=V21*$D$14*O47*$U$11*$N$16*$S$16`
- **P7:** `=PRODUCT(N7, O7)`
- **Q7:** `=P7*10.7639`
- **T7:** `=T22*$D$14*O22*$U$13*$N$16*$S$16`
- **U7:** `=U22*$D$14*O22*$U$12*$N$16*$S$16`
- **V7:** `=V22*$D$14*O22*$U$11*$N$16*$S$16`
- **P8:** `=PRODUCT(N8, O8)`
- **Q8:** `=P8*10.7639`
- **P9:** `=PRODUCT(N9, O9)`
- **Q9:** `=P9*10.7639`
- **N11:** `=SUM(P4:P9)`
- **P11:** `=P4`
- **N12:** `=SUM(Q4:Q9)`
- **P12:** `=Q4`
- **D14:** `=H2/D11/I2`
- **N16:** `=Summary!E16`
- **N17:** `=N16*H2`
- **N20:** `=G2`
- **N22:** `=(M22 * (9/5))+32`
- **O22:** `=O23+$N$20`
- **N23:** `=(M23 * (9/5))+32`
- **O23:** `=O24+$N$20`
- **AB23:** `=AA23*$AB$20`
- **AC23:** `=AB23*$S$38*$T$38*$U$38*$V$38/1000`
- **N24:** `=(M24 * (9/5))+32`
- **O24:** `=O25+$N$20`
- **AB24:** `=AA24*$AB$20`
- **AC24:** `=AB24*$S$38*$T$38*$U$38*$V$38/1000`
- **N25:** `=(M25 * (9/5))+32`
- **O25:** `=O26+$N$20`
- **AB25:** `=AA25*$AB$20`
- **AC25:** `=AB25*$S$38*$T$38*$U$38*$V$38/1000`
- **N26:** `=(M26 * (9/5))+32`
- **O26:** `=O27+$N$20`
- **AB26:** `=AA26*$AB$20`
- **AC26:** `=AB26*$S$38*$T$38*$U$38*$V$38/1000`
- **N27:** `=(M27 * (9/5))+32`
- **O27:** `=O28+$N$20`
- **AB27:** `=AA27*$AB$20`
- **AC27:** `=AB27*$S$38*$T$38*$U$38*$V$38/1000`
- **N28:** `=(M28 * (9/5))+32`
- **O28:** `=O29+$N$20`
- **AB28:** `=AA28*$AB$20`
- **AC28:** `=AB28*$S$38*$T$38*$U$38*$V$38/1000`
- **N29:** `=(M29 * (9/5))+32`
- **O29:** `=O30+$N$20`
- **T29:** `=T20*8.7/10`
- **U29:** `=U20*8.7/24`
- **V29:** `=V20*8.7/24`
- **AB29:** `=AA29*$AB$20/60`
- **AC29:** `=AB29*$S$38*$T$38*$U$38*$V$38/1000`
- **N30:** `=(M30 * (9/5))+32`
- **O30:** `=O31+$N$20`
- **T30:** `=T21*8.7/24`
- **U30:** `=U21*8.7/24`
- **V30:** `=V21*8.7/24`
- **AB30:** `=AA30*$AB$20`
- **AC30:** `=AB30*$S$38*$T$38*$U$38*$V$38/1000`
- **AD30:** `=0.977/AC30*60`
- **N31:** `=(M31 * (9/5))+32`
- **O31:** `=O32+$N$20`
- **T31:** `=T22*8.7/24`
- **U31:** `=U22*8.7/24`
- **V31:** `=V22*8.7/24`
- **AB31:** `=AA31*$AB$20`
- **AC31:** `=AB31*$S$38*$T$38*$U$38*$V$38/1000`
- **AD31:** `=0.977/AC31*60`
- **N32:** `=(M32 * (9/5))+32`
- **O32:** `=O33+$N$20`
- **AB32:** `=AA32*$AB$20`
- **AC32:** `=AB32*$S$38*$T$38*$U$38*$V$38/1000`
- **AD32:** `=0.977/AC32*60`
- **N33:** `=(M33 * (9/5))+32`
- **O33:** `=O34+$N$20`
- **T33:** `=T29*$S$38*$T$38*$U$38*$V$38/1000`
- **U33:** `=U29*$S$38*$T$38*$U$38*$V$38/1000`
- **V33:** `=V29*$S$38*$T$38*$U$38*$V$38/1000`
- **AB33:** `=AA33*$AB$20`
- **AC33:** `=AB33*$S$38*$T$38*$U$38*$V$38/1000`
- **AD33:** `=0.977/AC33*60`
- **N34:** `=(M34 * (9/5))+32`
- **O34:** `=O35+$N$20`
- **T34:** `=T30*$S$38*$T$38*$U$38*$V$38/1000`
- **U34:** `=U30*$S$38*$T$38*$U$38*$V$38/1000`
- **V34:** `=V30*$S$38*$T$38*$U$38*$V$38/1000`
- **AB34:** `=AA34*$AB$20`
- **AC34:** `=AB34*$S$38*$T$38*$U$38*$V$38/1000`
- **AD34:** `=0.977/AC34*60`
- **N35:** `=(M35 * (9/5))+32`
- **O35:** `=O36+$N$20`
- **T35:** `=T31*$S$38*$T$38*$U$38*$V$38/1000`
- **U35:** `=U31*$S$38*$T$38*$U$38*$V$38/1000`
- **V35:** `=V31*$S$38*$T$38*$U$38*$V$38/1000`
- **AB35:** `=AA35*$AB$20`
- **AC35:** `=AB35*$S$38*$T$38*$U$38*$V$38/1000`
- **AD35:** `=0.977/AC35*60`
- **N36:** `=(M36 * (9/5))+32`
- **O36:** `=O37+$N$20`
- **AB36:** `=AA36*$AB$20`
- **AC36:** `=AB36*$S$38*$T$38*$U$38*$V$38/1000`
- **AD36:** `=0.977/AC36*60`
- **N37:** `=(M37 * (9/5))+32`
- **O37:** `=O38+$N$20`
- **AB37:** `=AA37*$AB$20`
- **AC37:** `=AB37*$S$38*$T$38*$U$38*$V$38/1000`
- **AD37:** `=0.977/AC37*60`
- **N38:** `=(M38 * (9/5))+32`
- **O38:** `=O39+$N$20`
- **AB38:** `=AA38*$AB$20`
- **AC38:** `=AB38*$S$38*$T$38*$U$38*$V$38/1000`
- **AD38:** `=0.977/AC38*60`
- **N39:** `=(M39 * (9/5))+32`
- **O39:** `=O40+$N$20`
- **AB39:** `=AA39*$AB$20`
- **AC39:** `=AB39*$S$38*$T$38*$U$38*$V$38/1000`
- **AD39:** `=0.977/AC39*60`
- **N40:** `=(M40 * (9/5))+32`
- **O40:** `=O41+$N$20`
- **AB40:** `=AA40*$AB$20`
- **AC40:** `=AB40*$S$38*$T$38*$U$38*$V$38/1000`
- **AD40:** `=0.977/AC40*60`
- **N41:** `=(M41 * (9/5))+32`
- **O41:** `=O42+$N$20`
- **AB41:** `=AA41*$AB$20`
- **AC41:** `=AB41*$S$38*$T$38*$U$38*$V$38/1000`
- **AD41:** `=0.977/AC41*60`
- **N42:** `=(M42 * (9/5))+32`
- **O42:** `=O43+$N$20`
- **T42:** `=0.977/T33*60`
- **U42:** `=0.977/U33*60`
- **V42:** `=0.977/V33*60`
- **AB42:** `=AA42*$AB$20`
- **AC42:** `=AB42*$S$38*$T$38*$U$38*$V$38/1000`
- **AD42:** `=0.977/AC42*60`
- **N43:** `=(M43 * (9/5))+32`
- **O43:** `=O44+$N$20`
- **T43:** `=0.977/T34*60`
- **U43:** `=0.977/U34*60`
- **V43:** `=0.977/V34*60`
- **AB43:** `=AA43*$AB$20`
- **AC43:** `=AB43*$S$38*$T$38*$U$38*$V$38/1000`
- **N44:** `=(M44 * (9/5))+32`
- **O44:** `=O45+$N$20`
- **T44:** `=0.977/T35*60`
- **U44:** `=0.977/U35*60`
- **V44:** `=0.977/V35*60`
- **AB44:** `=AA44*$AB$20`
- **AC44:** `=AB44*$S$38*$T$38*$U$38*$V$38/1000`
- **N45:** `=(M45 * (9/5))+32`
- **O45:** `=O46+$N$20`
- **AB45:** `=AA45*$AB$20`
- **AC45:** `=AB45*$S$38*$T$38*$U$38*$V$38/1000`
- **N46:** `=(M46 * (9/5))+32`
- **O46:** `=O47+$N$20`
- **T46:** `=0.977/1*60`
- **U46:** `=0.977/1*60`
- **V46:** `=0.977/1*60`
- **AB46:** `=AA46*$AB$20`
- **AC46:** `=AB46*$S$38*$T$38*$U$38*$V$38/1000`
- **N47:** `=(M47 * (9/5))+32`
- **O47:** `=I2`
- **T47:** `=0.977/1*60`
- **U47:** `=0.977/1*60`
- **V47:** `=0.977/1*60`
- **N48:** `=(M48 * (9/5))+32`
- **O48:** `=O47-$N$20`
- **T48:** `=0.977/1*60`
- **U48:** `=0.977/1*60`
- **V48:** `=0.977/1*60`
- **N49:** `=(M49 * (9/5))+32`
- **O49:** `=O48-$N$20`
- **N50:** `=(M50 * (9/5))+32`
- **O50:** `=O49-$N$20`
- **N51:** `=(M51 * (9/5))+32`
- **O51:** `=O50-$N$20`
- **N52:** `=(M52 * (9/5))+32`
- **O52:** `=O51-$N$20`
- **N53:** `=(M53 * (9/5))+32`
- **O53:** `=O52-$N$20`
- **N54:** `=(M54 * (9/5))+32`
- **O54:** `=O53-$N$20`
- **N55:** `=(M55 * (9/5))+32`
- **O55:** `=O54-$N$20`
- **N56:** `=(M56 * (9/5))+32`
- **O56:** `=O55-$N$20`
- **N57:** `=(M57 * (9/5))+32`
- **O57:** `=O56-$N$20`
- **N58:** `=(M58 * (9/5))+32`
- **O58:** `=O57-$N$20`
- **N59:** `=(M59 * (9/5))+32`
- **O59:** `=O58-$N$20`
- **N60:** `=(M60 * (9/5))+32`
- **O60:** `=O59-$N$20`
- **N61:** `=(M61 * (9/5))+32`
- **O61:** `=O60-$N$20`
- **N62:** `=(M62 * (9/5))+32`
- **O62:** `=O61-$N$20`
- **N63:** `=(M63 * (9/5))+32`
- **O63:** `=O62-$N$20`
- **N64:** `=(M64 * (9/5))+32`
- **O64:** `=O63-$N$20`
- **N65:** `=(M65 * (9/5))+32`
- **O65:** `=O64-$N$20`
- **N66:** `=(M66 * (9/5))+32`
- **O66:** `=O65-$N$20`
- **N67:** `=(M67 * (9/5))+32`
- **O67:** `=O66-$N$20`
- **N68:** `=(M68 * (9/5))+32`
- **O68:** `=O67-$N$20`
- **N69:** `=(M69 * (9/5))+32`
- **O69:** `=O68-$N$20`
- **N70:** `=(M70 * (9/5))+32`
- **O70:** `=O69-$N$20`
- **N71:** `=(M71 * (9/5))+32`
- **O71:** `=O70-$N$20`

---

## Sheet: Lookup Tables

### CSV Data
```csv
"LOOKUP TABLES, MISC",Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
HVAC Energy per Termperature,,,,,
Environment,Condition,Energy [Wh],Notes,,
Day-Time Temperature,Cold,15615.34884,40°- F [4.4°C],,
,Temperate,744.6801315,70° F [21° C],,
,Hot,6923.755102,100°+ F [38° C],,
Night-Time Temperature,Cold,15615.34884,20°- F [-6.7°C],,
,Temperate,744.6801315,50° F [10° C],,
,Hot,6923.755102,80°+ F [27° C],,
,,,,,
Water Generated from HVAC per Enviornmental Conditions (gph),,,,,
,,Hot,Temperate,Cold,
Day-Time Humidity,Humid,0,0,0,0.8
,Comfortable,0,0,0,0.5
,Dry,0,0,0,0.2
,,Hot,Temperate,Cold,
Night-Time Humidity,Humid,0,0,0,0.9
,Comfortable,0,0,0,0.6
,Dry,0,0,0,0.3
,,,,,
Waste Water Calculator,,,,,
Activiy,Description,Greywater [gal],Blackwater [gal],Notes,
Living,misc. cleaning: rinsing things in the sink,4.982142857,-,,
Cooking,dishwasher,3.75,-,,
Cooking,Sink faucet,-,6.75,"Estimated 25% is consumed, 75% is waste",
Shower,includes recirc calculation (see user matrix),36,-,,
Laundry,per load of wash,2.472,-,,
Toilet,handwashing ,5.625,-,,
Toilet (9),filling and flushing,-6,9.375,,
NPW,Press. grey water expelled,0,,,
Totals,Totals,46.82914286,16.125,,
,,,,,
Rainwater Table,,,,,
Value,Units,Notes,,,
0.62,Gal*ft^-2*in^-1,Average amount of water that can be captured in USA. Units in gallons captured per square foot of area per inch of rainfall,,,
0.08219178082,in/day,Average rainfall/day accross USA,,,
94.8,ft^2,SA of available rain collection area on trailer,,,
0,gal/day,Calulated gallons/day of rainwater collection possible,,,
,,,,,
Percentage of Rainy Days per Trip,,,,,
,Hot,Temperate,Cold,,
Humid,0,0.25,0.1,,
Comfortable,0.25,0.15,0,,
Dry,0,0,0,,
,,,,,
Gauges,,,,,
,Level,Capacity,,,
Grey Water Tank,46.82914286,50,,,
Black Water Tank,16.125,45,,,
Battery,54.83479838,100,,,
Fresh Water,38.17085714,100,,,
Solar Output [kWh],28.40186346,50,,,
,,,,,
Rain Day Helper Cells,,,,,
0,,,,,
,,,,,
Summary Sign Reverse,,,,,
-1,,,,,

```

### Formulas Used

- **C4:** `='TEMP- Cold'!I7`
- **C5:** `='TEMP- Temperate'!I7`
- **C6:** `='TEMP- Hot'!J7`
- **C7:** `='TEMP- Cold'!I7`
- **C8:** `='TEMP- Temperate'!I7`
- **C9:** `='TEMP- Hot'!J7`
- **C23:** `=Living!I7*Summary!E5`
- **C24:** `=Cooking!U17*'User Matrix'!G26*Summary!E5`
- **D25:** `=Cooking!U23*'User Matrix'!G26*Summary!E5*0.75`
- **C26:** `=Summary!M5`
- **C27:** `=Summary!M7`
- **C28:** `=Toilet!U18*Summary!I6`
- **C29:** `=IF(C31>1, -0.4*Summary!I6, 0.4)`
- **D29:** `=Summary!M6+(0.25*Summary!I6)`
- **C30:** `='Non-Potable Water'!J8`
- **C31:** `=SUM(C23:C30)`
- **D31:** `=SUM(D23:D29)`
- **A36:** `=30/365`
- **B48:** `=Summary!Q7`
- **C48:** `=Summary!E19`
- **B49:** `=Summary!Q8`
- **C49:** `=Summary!E18`
- **B50:** `=C50-Summary!K15`
- **C50:** `=Summary!E14`
- **B51:** `=Summary!E14-Summary!M15`
- **B52:** `=(INDEX(Solar!S4:V7,MATCH(Summary!E8,Solar!S4:S7,0),MATCH(Summary!E9,Solar!S4:V4,0))*VLOOKUP(Summary!E10, Solar!X5:Y7, 2, 0))/1000`
- **A55:** `=IF(Summary!E9="Dry", ("Increase Humidity"), Summary!E6)`

---

## Sheet: Appendix

### CSV Data
```csv
Unnamed: 0,GENERAL NOTES
1,"a: The ""BOM Imax"" tab contains total power demands for each voltage bus. 
b: The tab does not update automatically, but uses a macro which must be run manually. Extensions>Macros>GrabComponentCurrents
c: Currents summed in BOM Imax tab are only AVERAGES. Additional work is required to understand peak demands."
,
,
,
,
,
No.,FOOT NOTES
1,"This refers to useable (net) capacity, not total (gross) capactiy"
2,"The water generator is integrated with the HVAC. Runtime has implications for energy consumption and water generation. A user can choose to run the HVAC/WaterGen for a long time to create water or for comfort, or can use sparingly to conserve energy, but will produce little or no water."
3,"Temperature selection influces HVAC as well as solar in the following way: Hot=Summer, Temperate=Spring/Fall, and Cold=Winter. This is to account for the varying sun angles and Solar Insolation in Los Angeles, CA (based on fabhabs.com calculator, cross referenced with Solar Electricity Handbook)"
4,"a. Water gen calculates water generated assuming first 12 hours are during the day. Any amount of HVAC runtime over 12 hours comes from the nighttime water gen table which produces less water than daytime. 
b. HVAC energy consumption varies by temperature
c. Water generated varies with humidity and temperature"
5,This UV Water system is only operable when shower recirculation is engaged. 
6,Assumption: the shower control pad uses max power only during the shower period
7,"User Definitions: 
Glamper: emphasis on luxury experience over resource conservation
Typical: average expected behvaiors
Expert: emphasis on resource conservation"
8,Living is a product of days only
9,Toilet uses grey water rather than fresh water for every flush where grey water tank level exceeds 1 gallon
10,Cooking energy does not scale with number of people
11,"Actuation occurs twice per outing (deploying and retracting rooms), plus twice each per relocation and each dumpstation trip"
12,"Non-potable water activities are calculated per trip, so are always only one cycle"
13,Dump-station trip frequency driven by water use
14,Stove power is an estimate based on one burner at full power (1/4 of max rated power)
15,Duty cycles calculated using heat transfer equasion assuming 1600ft2 and average R7 
16,This factor expresses what portion of the target hot water temp is achieved with the solar water heater vs electric tankless. Cells with red outline indicate temperature rises in excess of shower's capability and would require primary (electric tankless) water heater to operate in series.
17,"One burner (9"") on high"
18,Discontinued
19,"Two required (Trailer has 250ft2 of Smart Tint, 100W can power 125ft2)"
20,QTY Four required
21,"This no. of panels includes PVT area, since the power/area is almost identical. Future revs may add number of PV + number of PVT"
22,Future versions of the model may include using a 1kW calorifier to trade energy demands of electric tankless for warming time during low ambient temps
23,"Blend valve required to provide any shower temperatures below temp of water in solar hot water system, including cold showers. "
24,Relocation is defined here as moving the trailer to a new campsite. Each move requires two actuations (e.i. room retraction and extension).
25,Feature descoped

```

*No formulas found in this sheet.*

---

## Sheet: BOM Imax

### CSV Data
```csv
Component,Make,Model,Voltage (V),Average,Qty,Source Sheet,Imax,Demand (W),Demand (kW),ComponentHash
SmartTint (20),DC Power Supply,12 Volt DC Adapter,12,2.5,7.0,Living,17.5,210.0,0.21,smarttint(20)dcpowersupply12voltdcadapter
Macerating pump (P10),Pentair,3200-001,12,17.0,1.0,Toilet,17.0,204.0,0.204,maceratingpump(p10)pentair3200-001
Off-Grid Local Source Water Pump (P1),Everflow,EF5500,12,17.0,1.0,Non-Potable Water,17.0,204.0,0.204,off-gridlocalsourcewaterpump(p1)everflowef5500
Room support jacks,Thomson,HD12B017-1000EXX2EESD,12,15.0,1.0,Actuation,15.0,180.0,0.18,roomsupportjacksthomsonhd12b017-1000exx2eesd
Lighting,estimate,estimate,12,12.0,1.0,Living,12.0,144.0,0.144,lightingestimateestimate
Water pump,SHURflo,4048-153-E75 / 4048-153-A75,12,8.5,1.0,Living,8.5,102.0,0.102,waterpumpshurflo4048-153-e75/4048-153-a75
Audio Amplifier,Pioneer,GM-E3604,12,6.0,1.0,Living,6.0,72.0,0.072,audioamplifierpioneergm-e3604
Electric Waste Valves,Valterra,E85-8,12,2.5,1.0,Dumping,2.5,30.0,0.03,electricwastevalvesvalterrae85-8
Grey water pump (P9),Whale Pumps,Gulper 220,12,2.5,1.0,Shower,2.5,30.0,0.03,greywaterpump(p9)whalepumpsgulper220
Satellite Internet,DC Power supply,DC-DC PSU,12,2.5,1.0,Living,2.5,30.0,0.03,satelliteinternetdcpowersupplydc-dcpsu
Grey water pump (P7),Whale Pumps,Gulper 220,12,2.4,1.0,Toilet,2.4,28.799999999999997,0.028799999999999996,greywaterpump(p7)whalepumpsgulper220
Pressurised greywater spigot pump (P8),Whale Pumps,Gupler 220,12,2.4,1.0,Non-Potable Water,2.4,28.799999999999997,0.028799999999999996,pressurisedgreywaterspigotpump(p8)whalepumpsgupler220
Rain water pump (P2),Whale Pumps,Gulper 220,12,2.4,1.0,Non-Potable Water,2.4,28.799999999999997,0.028799999999999996,rainwaterpump(p2)whalepumpsgulper220
Camera system,Continental,ProViu360,12,2.0,1.0,Living,2.0,24.0,0.024,camerasystemcontinentalproviu360
Bathroom vent fan,Maxxair,00-003801 Mini Vent Plus,12,1.9,1.0,Toilet,1.9,22.799999999999997,0.022799999999999997,bathroomventfanmaxxair00-003801miniventplus
UV Water System(5),Viqua,VT4,12,1.8,1.0,Shower,1.8,21.6,0.0216,uvwatersystem(5)viquavt4
UV Water System,Viqua,VT4,12,1.8,1.0,Living,1.8,21.6,0.0216,uvwatersystemviquavt4
Solar hot water heater glycol pump (P4),Bayite,BYT-7A006,12,0.7,1.0,Living,0.7,8.399999999999999,0.008399999999999998,solarhotwaterheaterglycolpump(p4)bayitebyt-7a006
Motion Activated Storage lights,RECPRO,RP-1981,12,0.325,2.0,Living,0.65,7.800000000000001,0.0078000000000000005,motionactivatedstoragelightsrecprorp-1981
Tablet UI,Samsung,Galaxy Tab S10+,12,0.4166666666666667,1.0,Living,0.4166666666666667,5.0,0.005,tabletuisamsunggalaxytabs10+
Exterior Camp Lights,Optronics LED,BUL78CB,12,0.054,6.0,Living,0.324,3.888,0.003888,exteriorcamplightsoptronicsledbul78cb
Ext Porch Lighting,Diamond/etrailer.com,DG52526PB,12,0.14,1.0,Living,0.14,1.6800000000000002,0.00168,extporchlightingdiamond/etrailer.comdg52526pb
Shower control keypad (6),CZone,Landscape 80-911-0162-00 & Portrait 80-911-0163-00,12,0.056,1.0,Shower,0.056,0.672,0.0006720000000000001,showercontrolkeypad(6)czonelandscape80-911-0162-00&portrait80-911-0163-00
Shower control keypad,CZone,Landscape 80-911-0162-00 & Portrait 80-911-0163-00,12,0.0,1.0,Living,0.0,0.0,0.0,showercontrolkeypadczonelandscape80-911-0162-00&portrait80-911-0163-00
"Various sensors and controllers: 
- tank level sensors, module and panel
- sensor multiplexor
- tablet UI
- solar water pressure sensor
- inverters
- hall sensors
- LAN switch
- DCDC",,,12,0.0,1.0,Living,0.0,0.0,0.0,"varioussensorsandcontrollers:-tanklevelsensors,moduleandpanel-sensormultiplexor-tabletui-solarwaterpressuresensor-inverters-hallsensors-lanswitch-dcdc"
,,,12 Total,,,,117.4866666666667,1409.8400000000004,1.4098400000000004,
Chassis leveling jacks,,,24,9.3,4.0,Actuation,37.2,892.8000000000001,0.8928,chassislevelingjacks
Shower recirc 3-way valve,HSH-Flo,3 Way 24VAC/DC 4-20ma Proportional Integral Control Ball Valve,24,0.95,2.0,Shower,1.9,45.599999999999994,0.045599999999999995,showerrecirc3-wayvalvehsh-flo3way24vac/dc4-20maproportionalintegralcontrolballvalve
Side room floor actuators,,,24,1.4,1.0,Actuation,1.4,33.599999999999994,0.03359999999999999,sideroomflooractuators
Side room wall actuators,,,24,1.1,1.0,Actuation,1.1,26.400000000000002,0.026400000000000003,sideroomwallactuators
Rear room actuators,,,24,0.61,1.0,Actuation,0.61,14.64,0.01464,rearroomactuators
Front room actuators,,,24,0.427,1.0,Actuation,0.427,10.248,0.010248,frontroomactuators
Tire Pressure,BTI,TPMS CAN System,24,0.4,1.0,Living,0.4,9.600000000000001,0.009600000000000001,tirepressurebtitpmscansystem
Gearage actuators,,,24,0.13,1.0,Actuation,0.13,3.12,0.00312,gearageactuators
,,,24 Total,,,,43.167,1036.008,1.036008,
Ultra Capacity Washer Ventless Heat Pump Dryer Combo,Samsung,WD53DBA900HZA1 / WD53DBA900HZA1,120,15.0,1.0,Laundry,15.0,1800.0,1.8,ultracapacitywasherventlessheatpumpdryercombosamsungwd53dba900hza1/wd53dba900hza1
Microwave,Samsung,ME21DB630012AA / ME21DB630012AA,120,14.166666666666666,1.0,Cooking,14.166666666666666,1700.0,1.7,microwavesamsungme21db630012aa/me21db630012aa
Electronically controlled blend valve (23),Caleffi,600054A,120,6.0,1.0,Shower,6.0,720.0,0.72,electronicallycontrolledblendvalve(23)caleffi600054a
Garbage disposal,InSinkErator, Badger 1XL,120,5.6,1.0,Cooking,5.6,672.0,0.672,garbagedisposalinsinkeratorbadger1xl
Dishwasher,Fotile,SD2F-P3,120,5.35,1.0,Cooking,5.35,642.0,0.642,dishwasherfotilesd2f-p3
Consumer electronics,example,"blender, coffee maker, kettle, food processor, mixer, rice maker, toaster",120,5.0,1.0,Cooking,5.0,600.0,0.6,"consumerelectronicsexampleblender,coffeemaker,kettle,foodprocessor,mixer,ricemaker,toaster"
Consumer electronics,various,"ex: hair dryer, toothbrush/electric razor chargers",120,5.0,1.0,Shower,5.0,600.0,0.6,"consumerelectronicsvariousex:hairdryer,toothbrush/electricrazorchargers"
Television,Samsung,QN55LS03FAF / QN55LS03FAFXZA,120,0.7,1.0,Living,0.7,84.0,0.084,televisionsamsungqn55ls03faf/qn55ls03fafxza
Refrigerator,Samsung,RF18A5101SG / RF18A5101SG/AA,120,0.5136986301369864,1.0,Living,0.5136986301369864,61.643835616438366,0.06164383561643837,refrigeratorsamsungrf18a5101sg/rf18a5101sg/aa
Consumer electronics,estimate,"phone & laptop chargers, other misc.",120,0.5,1.0,Living,0.5,60.0,0.06,"consumerelectronicsestimatephone&laptopchargers,othermisc."
LAN Switch PSU,Mean Well,MDR-60-24,120,0.25,1.0,Living,0.25,30.0,0.03,lanswitchpsumeanwellmdr-60-24
,,,120 Total,,,,58.080365296803656,6969.643835616439,6.969643835616439,
Tankless water heater,Camplux,8kW,240,33.4,1.0,Toilet,33.4,8016.0,8.016,tanklesswaterheatercamplux8kw
Electric shower,Aqualisa,eMotion,240,33.0,1.0,Shower,33.0,7920.0,7.92,electricshoweraqualisaemotion
Stove,Samsung,NZ30K6330RS/AA / NZ30K6330RS/AA,240,12.5,1.0,Cooking,12.5,3000.0,3.0,stovesamsungnz30k6330rs/aa/nz30k6330rs/aa
Mini-Split HVAC,MrCool DIY,"4th Gen Multi-Zone 2-Zone 18,000 BTU 21 SEER (9K + 12K)",240,9.205426356589149,1.0,TEMP- Temperate,9.205426356589149,2209.3023255813955,2.2093023255813957,"mini-splithvacmrcooldiy4thgenmulti-zone2-zone18,000btu21seer(9k+12k)"
Toilet (incinerator),Cinderella,Comfort Insineration Toilet,240,5.0,1.0,Toilet,5.0,1200.0,1.2,toilet(incinerator)cinderellacomfortinsinerationtoilet
,,,240 Total,,,,93.10542635658915,22345.302325581397,22.345302325581397,
AC BUS TOTAL,,,,,,,,29314.946161197833,29.314946161197835,

```

*No formulas found in this sheet.*

---

## Sheet: Power Supply Sizing

### CSV Data
```csv
12V Bus,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
Total Current,0.056,A,,12V Load,,,,,,,
,1.1,A,,24V Load,,,,,,,
,1.265,A,,24V Load assuming 85% efficiency,,,,,,,
,,,,,,,,UPDATE: THESE CALCS ARE NOT APPLICABLE,,,
,,,,,,,,20,1,20.0,
,Worst Case load on 12V DC DC,15.852,kW,,,,,20,0.5,10.0,
,,,,,,,,-38.679,0.25,-9.66975,
,,,,,,,,,,20.33025,A
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,243.963,W,,

```

### Formulas Used

- **B2:** `='BOM Imax'!H24`
- **B3:** `='BOM Imax'!H31`
- **B4:** `=B3*1.15`
- **K6:** `=PRODUCT(I6*J6)`
- **C7:** `=(B2+B4)*12`
- **K7:** `=PRODUCT(I7*J7)`
- **I8:** `=SUM(B2,B4)-40`
- **K8:** `=PRODUCT(I8*J8)`
- **K9:** `=SUM(K6:K8)`
- **I12:** `=12*K9`

---

## Sheet: HUMID- H20 Gen

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19
,System Inputs,,,,,,,System Outputs,,,,,,,,,,,Sheet Key
,Value,Unit,Description,,,,,Value,Unit,Description,,,Used for,,,,,,Input field
,1,-,Factor of safety applied to total energy required,,,,,10,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field
,24,hr / day,Max operation time / day,,,,,20023.98333,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,
,45,min,Max single cycle duration,,,,,20023.98333,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Selected?,Component,Make,Model,Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
False,,,,,1,5,10,1,1,600,1,0.01666666667,0.01666666667,23.98333333,1,5,23.98333333,20000,0.001201892064
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H30,I12:I30)`
- **I5:** `=$B$4 * I7`
- **B7:** `=0.75*60`
- **I7:** `=SUM(R12:S24)`
- **K12:** `=600`
- **M12:** `=L12/60`
- **N12:** `=J12*M12`
- **O12:** `=IF(F12 = 0, 0, $B$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=PRODUCT(E12,G12,I12)`
- **R12:** `=P12*O12`
- **T12:** `=(N12*Q12+O12*P12) / $I$7`
- **F13:** `=G13`
- **L13:** `=K13/60`
- **M13:** `=L13/60`
- **N13:** `=J13*M13`
- **O13:** `=IF(F13 = 0, 0, $B$5-N13)`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `=PRODUCT(E13,G13,I13)`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13`
- **T13:** `=(N13*Q13+O13*P13) / $I$7`
- **L14:** `=K14/60`
- **M14:** `=L14/60`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $B$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$7`
- **L15:** `=K15/60`
- **M15:** `=L15/60`
- **N15:** `=J15*M15`
- **O15:** `=IF(F15 = 0, 0, $B$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$7`
- **L16:** `=K16/60`
- **M16:** `=L16/60`
- **N16:** `=J16*M16`
- **O16:** `=IF(F16 = 0, 0, $B$5-N16)`
- **P16:** `=PRODUCT(E16,F16,I16)`
- **Q16:** `=PRODUCT(E16,G16,I16)`
- **R16:** `=P16*O16`
- **S16:** `=Q16*N16`
- **T16:** `=(N16*Q16+O16*P16) / $I$7`
- **L17:** `=K17/60`
- **M17:** `=L17/60`
- **N17:** `=J17*M17`
- **O17:** `=IF(F17 = 0, 0, $B$5-N17)`
- **P17:** `=PRODUCT(E17,F17,I17)`
- **Q17:** `=PRODUCT(E17,G17,I17)`
- **R17:** `=P17*O17`
- **S17:** `=Q17*N17`
- **L18:** `=K18/60`
- **M18:** `=L18/60`
- **N18:** `=J18*M18`
- **O18:** `=IF(F18 = 0, 0, $B$5-N18)`
- **P18:** `=PRODUCT(E18,F18,I18)`
- **Q18:** `=PRODUCT(E18,G18,I18)`
- **R18:** `=P18*O18`
- **S18:** `=Q18*N18`
- **T18:** `=(N18*Q18+O18*P18) / $I$7`
- **L19:** `=K19/60`
- **M19:** `=L19/60`
- **N19:** `=J19*M19`
- **O19:** `=IF(F19 = 0, 0, $B$5-N19)`
- **P19:** `=PRODUCT(E19,F19,I19)`
- **Q19:** `=PRODUCT(E19,G19,I19)`
- **R19:** `=P19*O19`
- **S19:** `=Q19*N19`
- **T19:** `=(N19*Q19+O19*P19) / $I$7`
- **L20:** `=K20/60`
- **M20:** `=L20/60`
- **N20:** `=J20*M20`
- **O20:** `=IF(F20 = 0, 0, $B$5-N20)`
- **P20:** `=PRODUCT(E20,F20,I20)`
- **Q20:** `=PRODUCT(E20,G20,I20)`
- **R20:** `=P20*O20`
- **S20:** `=Q20*N20`
- **T20:** `=(N20*Q20+O20*P20) / $I$7`
- **L21:** `=K21/60`
- **M21:** `=L21/60`
- **N21:** `=J21*M21`
- **O21:** `=IF(F21 = 0, 0, $B$5-N21)`
- **P21:** `=PRODUCT(E21,F21,I21)`
- **Q21:** `=PRODUCT(E21,G21,I21)`
- **R21:** `=P21*O21`
- **S21:** `=Q21*N21`
- **T21:** `=(N21*Q21+O21*P21) / $I$7`
- **L22:** `=K22/60`
- **M22:** `=L22/60`
- **N22:** `=J22*M22`
- **O22:** `=IF(F22 = 0, 0, $B$5-N22)`
- **P22:** `=PRODUCT(E22,F22,I22)`
- **Q22:** `=PRODUCT(E22,G22,I22)`
- **R22:** `=P22*O22`
- **S22:** `=Q22*N22`
- **T22:** `=(N22*Q22+O22*P22) / $I$7`
- **L23:** `=K23/60`
- **M23:** `=L23/60`
- **N23:** `=J23*M23`
- **O23:** `=IF(F23 = 0, 0, $B$5-N23)`
- **P23:** `=PRODUCT(E23,F23,I23)`
- **Q23:** `=PRODUCT(E23,G23,I23)`
- **R23:** `=P23*O23`
- **S23:** `=Q23*N23`
- **T23:** `=(N23*Q23+O23*P23) / $I$7`
- **L24:** `=K24/60`
- **M24:** `=L24/60`
- **N24:** `=J24*M24`
- **O24:** `=IF(F24 = 0, 0, $B$5-N24)`
- **P24:** `=PRODUCT(E24,F24,I24)`
- **Q24:** `=PRODUCT(E24,G24,I24)`
- **R24:** `=P24*O24`
- **S24:** `=Q24*N24`
- **T24:** `=(N24*Q24+O24*P24) / $I$7`

---

## Sheet: DRY- H20 Gen

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19
,System Inputs,,,,,,,System Outputs,,,,,,,,,,,Sheet Key
,Value,Unit,Description,,,,,Value,Unit,Description,,,Used for,,,,,,Input field
,1,-,Factor of safety applied to total energy required,,,,,100,A,Maximum total current draw,,,Minimum Continuous Discharge Current requirement for battery seleciton,,,,,,Output / calculated field
,24,hr / day,Max operation time / day,,,,,80056,Wh,Total energy / day with factor of safety applied,,,Minimum energy requirement for battery selection,,,,,,
,1,cycles / day,Number of times operated / day,,,,,,,,,,,,,,,,
,45,min,Max single cycle duration,,,,,80056,Wh,Total energy / day w/o factor of safety applied,,,-,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,
,,,,,Per Device Current (A),,,,Time,,,,,,Per Device Power (W),,Per Device Energy Use (Wh),,Misc. Calculations
Selected?,Component,Make,Model,Voltage (V),Idle,Average,Peak,Qty,Cycles / Day,Time/Cycle (s),Time/Cycle (min),Time/Cycle (hr),Cycle Time / Day (hr),Idle Time / Day (hr),Idle,Average,Idle Contribution,Average Contribution,% Contribution to energy budget
False,,,,,4,50,100,1,1,600,1,0.01666666667,10,14,4,50,56,80000,0.006945138403
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
False,,,,,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

```

### Formulas Used

- **I4:** `=SUMPRODUCT(H12:H30,I12:I30)`
- **I5:** `=$B$4 * I7`
- **B7:** `=0.75*60`
- **I7:** `=SUM(R12:S24)`
- **K12:** `=600`
- **M12:** `=L12/60`
- **O12:** `=IF(F12 = 0, 0, $B$5-N12)`
- **P12:** `=PRODUCT(E12,F12,I12)`
- **Q12:** `=PRODUCT(E12,G12,I12)`
- **R12:** `=P12*O12`
- **T12:** `=(N12*Q12+O12*P12) / $I$7`
- **F13:** `=G13`
- **L13:** `=K13/60`
- **M13:** `=L13/60`
- **N13:** `=J13*M13`
- **O13:** `=IF(F13 = 0, 0, $B$5-N13)`
- **P13:** `=PRODUCT(E13,F13,I13)`
- **Q13:** `=PRODUCT(E13,G13,I13)`
- **R13:** `=P13*O13`
- **S13:** `=Q13*N13`
- **T13:** `=(N13*Q13+O13*P13) / $I$7`
- **L14:** `=K14/60`
- **M14:** `=L14/60`
- **N14:** `=J14*M14`
- **O14:** `=IF(F14 = 0, 0, $B$5-N14)`
- **P14:** `=PRODUCT(E14,F14,I14)`
- **Q14:** `=PRODUCT(E14,G14,I14)`
- **R14:** `=P14*O14`
- **S14:** `=Q14*N14`
- **T14:** `=(N14*Q14+O14*P14) / $I$7`
- **L15:** `=K15/60`
- **M15:** `=L15/60`
- **N15:** `=J15*M15`
- **O15:** `=IF(F15 = 0, 0, $B$5-N15)`
- **P15:** `=PRODUCT(E15,F15,I15)`
- **Q15:** `=PRODUCT(E15,G15,I15)`
- **R15:** `=P15*O15`
- **S15:** `=Q15*N15`
- **T15:** `=(N15*Q15+O15*P15) / $I$7`
- **L16:** `=K16/60`
- **M16:** `=L16/60`
- **N16:** `=J16*M16`
- **O16:** `=IF(F16 = 0, 0, $B$5-N16)`
- **P16:** `=PRODUCT(E16,F16,I16)`
- **Q16:** `=PRODUCT(E16,G16,I16)`
- **R16:** `=P16*O16`
- **S16:** `=Q16*N16`
- **T16:** `=(N16*Q16+O16*P16) / $I$7`
- **L17:** `=K17/60`
- **M17:** `=L17/60`
- **N17:** `=J17*M17`
- **O17:** `=IF(F17 = 0, 0, $B$5-N17)`
- **P17:** `=PRODUCT(E17,F17,I17)`
- **Q17:** `=PRODUCT(E17,G17,I17)`
- **R17:** `=P17*O17`
- **S17:** `=Q17*N17`
- **L18:** `=K18/60`
- **M18:** `=L18/60`
- **N18:** `=J18*M18`
- **O18:** `=IF(F18 = 0, 0, $B$5-N18)`
- **P18:** `=PRODUCT(E18,F18,I18)`
- **Q18:** `=PRODUCT(E18,G18,I18)`
- **R18:** `=P18*O18`
- **S18:** `=Q18*N18`
- **T18:** `=(N18*Q18+O18*P18) / $I$7`
- **L19:** `=K19/60`
- **M19:** `=L19/60`
- **N19:** `=J19*M19`
- **O19:** `=IF(F19 = 0, 0, $B$5-N19)`
- **P19:** `=PRODUCT(E19,F19,I19)`
- **Q19:** `=PRODUCT(E19,G19,I19)`
- **R19:** `=P19*O19`
- **S19:** `=Q19*N19`
- **T19:** `=(N19*Q19+O19*P19) / $I$7`
- **L20:** `=K20/60`
- **M20:** `=L20/60`
- **N20:** `=J20*M20`
- **O20:** `=IF(F20 = 0, 0, $B$5-N20)`
- **P20:** `=PRODUCT(E20,F20,I20)`
- **Q20:** `=PRODUCT(E20,G20,I20)`
- **R20:** `=P20*O20`
- **S20:** `=Q20*N20`
- **T20:** `=(N20*Q20+O20*P20) / $I$7`
- **L21:** `=K21/60`
- **M21:** `=L21/60`
- **N21:** `=J21*M21`
- **O21:** `=IF(F21 = 0, 0, $B$5-N21)`
- **P21:** `=PRODUCT(E21,F21,I21)`
- **Q21:** `=PRODUCT(E21,G21,I21)`
- **R21:** `=P21*O21`
- **S21:** `=Q21*N21`
- **T21:** `=(N21*Q21+O21*P21) / $I$7`
- **L22:** `=K22/60`
- **M22:** `=L22/60`
- **N22:** `=J22*M22`
- **O22:** `=IF(F22 = 0, 0, $B$5-N22)`
- **P22:** `=PRODUCT(E22,F22,I22)`
- **Q22:** `=PRODUCT(E22,G22,I22)`
- **R22:** `=P22*O22`
- **S22:** `=Q22*N22`
- **T22:** `=(N22*Q22+O22*P22) / $I$7`
- **L23:** `=K23/60`
- **M23:** `=L23/60`
- **N23:** `=J23*M23`
- **O23:** `=IF(F23 = 0, 0, $B$5-N23)`
- **P23:** `=PRODUCT(E23,F23,I23)`
- **Q23:** `=PRODUCT(E23,G23,I23)`
- **R23:** `=P23*O23`
- **S23:** `=Q23*N23`
- **T23:** `=(N23*Q23+O23*P23) / $I$7`
- **L24:** `=K24/60`
- **M24:** `=L24/60`
- **N24:** `=J24*M24`
- **O24:** `=IF(F24 = 0, 0, $B$5-N24)`
- **P24:** `=PRODUCT(E24,F24,I24)`
- **Q24:** `=PRODUCT(E24,G24,I24)`
- **R24:** `=P24*O24`
- **S24:** `=Q24*N24`
- **T24:** `=(N24*Q24+O24*P24) / $I$7`

---

## Sheet: Component Specs

### CSV Data
```csv
"This sheet should only contain components shared across more than one Activity. Components unique to one activity should NOT be added here, and directly into thier respective Activity tab instead. For example, stove is not shared and should only appear in Meal Prep",Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,,,,,
Activity,Component,Notes,Volts,Amps,Power [W]
Shower ,Water Pump,"Should add some cycle time under ""living"" for handwashing",12,10,120
,Water Heater,"Should add some cycle time under ""living"" for handwashing",,,0
,Bathroom Vent Fan,,12,1.9,22.8
,Toilet,See Toilet tab,,,0
Meal Prep,Microwave,,,,0
,Stove,,,,0
,Oven,,,,0
,Dishwasher,,,,0
,Garbage Disposal,,,,0
,Kitchen Vent,,,,0
Laundry,Washer,,,,0
,Dryer,,,,0
,,,,,0
Living,Television,,,,0
,Sound System,,,,0
,Consumer Electronics [Estimate from typical hair dryer],"Laptop, phone charger, hairdryer, blender, vacuum",120,10,1200
,Starlink,,,,0
,Lights,,,,0
Climate Control,Air Conditioner,,,,0
,Heater,,,,0
Actuation,Wall Actuators,,,,0
,Valid Actuators,,,,0
,EV Motor/Inverter,,,,0

```

### Formulas Used

- **F4:** `=D4*E4`
- **F5:** `=D5*E5`
- **F6:** `=D6*E6`
- **F7:** `=D7*E7`
- **F8:** `=D8*E8`
- **F9:** `=D9*E9`
- **F10:** `=D10*E10`
- **F11:** `=D11*E11`
- **F12:** `=D12*E12`
- **F13:** `=D13*E13`
- **F14:** `=D14*E14`
- **F15:** `=D15*E15`
- **F16:** `=D16*E16`
- **F17:** `=D17*E17`
- **F18:** `=D18*E18`
- **F19:** `=D19*E19`
- **F20:** `=D20*E20`
- **F21:** `=D21*E21`
- **F22:** `=D22*E22`
- **F23:** `=D23*E23`
- **F24:** `=D24*E24`
- **F25:** `=D25*E25`
- **F26:** `=D26*E26`

---

## Sheet: Junction IDs

### CSV Data
```csv
PIN,Unnamed: 1,Unnamed: 2,SOCKET,Unnamed: 4,Unnamed: 5,DEVICE,Unnamed: 7,Unnamed: 8,RELAYS,Unnamed: 10
ID,Description,,ID,Description,,ID,Description,,ID,Description
JP-001,,,JS-001 ,,,E-001,,,K-001,
JP-002,,,JS-002,,,E-002,,,K-002,
JP-003,,,JS-003,,,E-003,,,K-003,
JP-004,,,JS-004,,,E-004,,,K-004,
JP-005,,,JS-005,,,E-005,,,K-005,
JP-006,,,JS-006,,,E-006,,,K-006,
JP-007,,,JS-007,,,E-007,,,K-007,
JP-008,,,JS-008,,,E-008,,,K-008,
JP-009,,,JS-009,,,E-009,,,K-009,
JP-010,,,JS-010,,,E-010,,,K-010,
JP-011,,,JS-011,,,E-011,,,K-011,
JP-012,,,JS-012,,,E-012,,,K-012,
JP-013,,,JS-013,,,E-013,,,K-013,
JP-014,,,JS-014,,,E-014,,,K-014,
JP-015,,,JS-015,,,E-015,,,K-015,
JP-016,,,JS-016,,,E-016,,,K-016,
JP-017,,,JS-017,,,E-017,,,K-017,
JP-018,,,JS-018,,,E-018,,,K-018,
JP-019,,,JS-019,,,E-019,,,K-019,
JP-020,,,JS-020,,,E-020,,,K-020,
JP-021,,,JS-021,,,E-021,,,K-021,
JP-022,,,JS-022,,,E-022,, ,K-022,
JP-023,,,JS-023,,,E-023,,,K-023,
JP-024,,,JS-024,,,E-024,,,K-024,
JP-025,,,JS-025,,,E-025,,,K-025,
JP-026,,,JS-026,,,E-026,,,K-026,
JP-027,,,JS-027,,,E-027,,,K-027,
JP-028,,,JS-028,,,E-028,,,K-028,
JP-029,,,JS-029,,,E-029,,,K-029,
JP-030,,,JS-030,,,E-030,,,K-030,
JP-031,,,JS-031,,,E-031,,,K-031,
JP-032,,,JS-032,,,E-032,,,K-032,
JP-033,,,JS-033,,,E-033,,,K-033,
JP-034,,,JS-034,,,E-034,,,K-034,
JP-035,,,JS-035,,,E-035,,,K-035,
JP-036,,,JS-036,,,E-036,,,K-036,
JP-037,,,JS-037,,,E-037,,,K-037,
JP-038,,,JS-038,,,E-038,,,K-038,
JP-039,,,JS-039,,,E-039,,,K-039,
JP-040,,,JS-040,,,E-040,,,K-040,
JP-041,,,JS-041,,,E-041,,,K-041,
JP-042,,,JS-042,,,E-042,,,K-042,
JP-043,,,JS-043,,,E-043,,,K-043,
JP-044,,,JS-044,,,E-044,,,K-044,
JP-045,,,JS-045,,,E-045,,,K-045,
JP-046,,,JS-046,,,E-046,,,K-046,
JP-047,,,JS-047,,,E-047,,,K-047,
JP-048,,,JS-048,,,E-048,,,K-048,
JP-049,,,JS-049,,,E-049,,,K-049,
JP-050,,,JS-050,,,E-050,,,K-050,
JP-051,,,JS-051,,,,,,,
JP-052,,,JS-052,,,,,,,
JP-053,,,JS-053,,,,,,,
JP-054,,,JS-054,,,,,,,
JP-055,,,JS-055,,,,,,,
JP-056,,,JS-056,,,,,,,
JP-057,,,JS-057,,,,,,,
JP-058,,,JS-058,,,,,,,
JP-059,,,JS-059,,,,,,,
JP-060,,,JS-060,,,,,,,
JP-061,,,JS-061,,,,,,,
JP-062,,,JS-062,,,,,,,
JP-063,,,JS-063,,,,,,,
JP-064,,,JS-064,,,,,,,
JP-065,,,JS-065,,,,,,,
JP-066,,,JS-066,,,,,,,
JP-067,,,JS-067,,,,,,,
JP-068,,,JS-068,,,,,,,
JP-069,,,JS-069,,,,,,,
JP-070,,,JS-070,,,,,,,
JP-071,,,JS-071,,,,,,,
JP-072,,,JS-072,,,,,,,
JP-073,,,JS-073,,,,,,,
JP-074,,,JS-074,,,,,,,
JP-075,,,JS-075,,,,,,,
JP-076,,,JS-076,,,,,,,
JP-077,,,JS-077,,,,,,,
JP-078,,,JS-078,,,,,,,
JP-079,,,JS-079,,,,,,,
JP-080,,,JS-080,,,,,,,
JP-081,,,JS-081,,,,,,,
JP-082,,,JS-082,,,,,,,
JP-083,,,JS-083,,,,,,,
JP-084,,,JS-084,,,,,,,
JP-085,,,JS-085,,,,,,,
JP-086,,,JS-086,,,,,,,
JP-087,,,JS-087,,,,,,,
JP-088,,,JS-088,,,,,,,
JP-089,,,JS-089,,,,,,,
JP-090,,,JS-090,,,,,,,
JP-091,,,JS-091,,,,,,,
JP-092,,,JS-092,,,,,,,
JP-093,,,JS-093,,,,,,,
JP-094,,,JS-094,,,,,,,
JP-095,,,JS-095,,,,,,,
JP-096,,,JS-096,,,,,,,
JP-097,,,JS-097,,,,,,,
JP-098,,,JS-098,,,,,,,
JP-099,,,JS-099,,,,,,,
JP-100,,,JS-100,,,,,,,

```

*No formulas found in this sheet.*

---

## Sheet: Test BOM 2000

### CSV Data
```csv
Description,Identifier,Manufacturer,Component PN,Subcomponent PN,Items Per Unit,Number of Units,Qty Onhand,Need Quantity,Package Quantity,Package Price,Order Qty (Pkgs),Order Qty (Total Parts),Order Price,Vendor,Notes
Test,123.0,123.0,123.0,123.0,2.0,1,1,1.2,1,100,2,2,200,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,
,,,,,,1,1,-1.0,1,0,0,0,0,,

```

### Formulas Used

- **I2:** `=F2*G2*1.1-H2`
- **M2:** `=L2*J2`
- **N2:** `=L2*K2`
- **I3:** `=F3*G3*1.1-H3`
- **M3:** `=L3*J3`
- **N3:** `=L3*K3`
- **I4:** `=F4*G4*1.1-H4`
- **M4:** `=L4*J4`
- **N4:** `=L4*K4`
- **I5:** `=F5*G5*1.1-H5`
- **M5:** `=L5*J5`
- **N5:** `=L5*K5`
- **I6:** `=F6*G6*1.1-H6`
- **M6:** `=L6*J6`
- **N6:** `=L6*K6`
- **I7:** `=F7*G7*1.1-H7`
- **M7:** `=L7*J7`
- **N7:** `=L7*K7`
- **I8:** `=F8*G8*1.1-H8`
- **M8:** `=L8*J8`
- **N8:** `=L8*K8`
- **I9:** `=F9*G9*1.1-H9`
- **M9:** `=L9*J9`
- **N9:** `=L9*K9`
- **I10:** `=F10*G10*1.1-H10`
- **M10:** `=L10*J10`
- **N10:** `=L10*K10`
- **I11:** `=F11*G11*1.1-H11`
- **M11:** `=L11*J11`
- **N11:** `=L11*K11`
- **I12:** `=F12*G12*1.1-H12`
- **M12:** `=L12*J12`
- **N12:** `=L12*K12`
- **I13:** `=F13*G13*1.1-H13`
- **M13:** `=L13*J13`
- **N13:** `=L13*K13`
- **I14:** `=F14*G14*1.1-H14`
- **M14:** `=L14*J14`
- **N14:** `=L14*K14`
- **I15:** `=F15*G15*1.1-H15`
- **M15:** `=L15*J15`
- **N15:** `=L15*K15`
- **I16:** `=F16*G16*1.1-H16`
- **M16:** `=L16*J16`
- **N16:** `=L16*K16`
- **I17:** `=F17*G17*1.1-H17`
- **M17:** `=L17*J17`
- **N17:** `=L17*K17`
- **I18:** `=F18*G18*1.1-H18`
- **M18:** `=L18*J18`
- **N18:** `=L18*K18`
- **I19:** `=F19*G19*1.1-H19`
- **M19:** `=L19*J19`
- **N19:** `=L19*K19`
- **I20:** `=F20*G20*1.1-H20`
- **M20:** `=L20*J20`
- **N20:** `=L20*K20`
- **I21:** `=F21*G21*1.1-H21`
- **M21:** `=L21*J21`
- **N21:** `=L21*K21`
- **I22:** `=F22*G22*1.1-H22`
- **M22:** `=L22*J22`
- **N22:** `=L22*K22`
- **I23:** `=F23*G23*1.1-H23`
- **M23:** `=L23*J23`
- **N23:** `=L23*K23`
- **I24:** `=F24*G24*1.1-H24`
- **M24:** `=L24*J24`
- **N24:** `=L24*K24`
- **I25:** `=F25*G25*1.1-H25`
- **M25:** `=L25*J25`
- **N25:** `=L25*K25`
- **I26:** `=F26*G26*1.1-H26`
- **M26:** `=L26*J26`
- **N26:** `=L26*K26`
- **I27:** `=F27*G27*1.1-H27`
- **M27:** `=L27*J27`
- **N27:** `=L27*K27`
- **I28:** `=F28*G28*1.1-H28`
- **M28:** `=L28*J28`
- **N28:** `=L28*K28`
- **I29:** `=F29*G29*1.1-H29`
- **M29:** `=L29*J29`
- **N29:** `=L29*K29`
- **I30:** `=F30*G30*1.1-H30`
- **M30:** `=L30*J30`
- **N30:** `=L30*K30`
- **I31:** `=F31*G31*1.1-H31`
- **M31:** `=L31*J31`
- **N31:** `=L31*K31`
- **I32:** `=F32*G32*1.1-H32`
- **M32:** `=L32*J32`
- **N32:** `=L32*K32`
- **I33:** `=F33*G33*1.1-H33`
- **M33:** `=L33*J33`
- **N33:** `=L33*K33`
- **I34:** `=F34*G34*1.1-H34`
- **M34:** `=L34*J34`
- **N34:** `=L34*K34`
- **I35:** `=F35*G35*1.1-H35`
- **M35:** `=L35*J35`
- **N35:** `=L35*K35`
- **I36:** `=F36*G36*1.1-H36`
- **M36:** `=L36*J36`
- **N36:** `=L36*K36`
- **I37:** `=F37*G37*1.1-H37`
- **M37:** `=L37*J37`
- **N37:** `=L37*K37`
- **I38:** `=F38*G38*1.1-H38`
- **M38:** `=L38*J38`
- **N38:** `=L38*K38`
- **I39:** `=F39*G39*1.1-H39`
- **M39:** `=L39*J39`
- **N39:** `=L39*K39`
- **I40:** `=F40*G40*1.1-H40`
- **M40:** `=L40*J40`
- **N40:** `=L40*K40`
- **I41:** `=F41*G41*1.1-H41`
- **M41:** `=L41*J41`
- **N41:** `=L41*K41`
- **I42:** `=F42*G42*1.1-H42`
- **M42:** `=L42*J42`
- **N42:** `=L42*K42`
- **I43:** `=F43*G43*1.1-H43`
- **M43:** `=L43*J43`
- **N43:** `=L43*K43`
- **I44:** `=F44*G44*1.1-H44`
- **M44:** `=L44*J44`
- **N44:** `=L44*K44`
- **I45:** `=F45*G45*1.1-H45`
- **M45:** `=L45*J45`
- **N45:** `=L45*K45`
- **I46:** `=F46*G46*1.1-H46`
- **M46:** `=L46*J46`
- **N46:** `=L46*K46`
- **I47:** `=F47*G47*1.1-H47`
- **M47:** `=L47*J47`
- **N47:** `=L47*K47`
- **I48:** `=F48*G48*1.1-H48`
- **M48:** `=L48*J48`
- **N48:** `=L48*K48`
- **I49:** `=F49*G49*1.1-H49`
- **M49:** `=L49*J49`
- **N49:** `=L49*K49`
- **I50:** `=F50*G50*1.1-H50`
- **M50:** `=L50*J50`
- **N50:** `=L50*K50`
- **I51:** `=F51*G51*1.1-H51`
- **M51:** `=L51*J51`
- **N51:** `=L51*K51`
- **I52:** `=F52*G52*1.1-H52`
- **M52:** `=L52*J52`
- **N52:** `=L52*K52`
- **I53:** `=F53*G53*1.1-H53`
- **M53:** `=L53*J53`
- **N53:** `=L53*K53`
- **I54:** `=F54*G54*1.1-H54`
- **M54:** `=L54*J54`
- **N54:** `=L54*K54`
- **I55:** `=F55*G55*1.1-H55`
- **M55:** `=L55*J55`
- **N55:** `=L55*K55`
- **I56:** `=F56*G56*1.1-H56`
- **M56:** `=L56*J56`
- **N56:** `=L56*K56`
- **I57:** `=F57*G57*1.1-H57`
- **M57:** `=L57*J57`
- **N57:** `=L57*K57`
- **I58:** `=F58*G58*1.1-H58`
- **M58:** `=L58*J58`
- **N58:** `=L58*K58`
- **I59:** `=F59*G59*1.1-H59`
- **M59:** `=L59*J59`
- **N59:** `=L59*K59`
- **I60:** `=F60*G60*1.1-H60`
- **M60:** `=L60*J60`
- **N60:** `=L60*K60`
- **I61:** `=F61*G61*1.1-H61`
- **M61:** `=L61*J61`
- **N61:** `=L61*K61`
- **I62:** `=F62*G62*1.1-H62`
- **M62:** `=L62*J62`
- **N62:** `=L62*K62`
- **I63:** `=F63*G63*1.1-H63`
- **M63:** `=L63*J63`
- **N63:** `=L63*K63`
- **I64:** `=F64*G64*1.1-H64`
- **M64:** `=L64*J64`
- **N64:** `=L64*K64`
- **I65:** `=F65*G65*1.1-H65`
- **M65:** `=L65*J65`
- **N65:** `=L65*K65`
- **I66:** `=F66*G66*1.1-H66`
- **M66:** `=L66*J66`
- **N66:** `=L66*K66`
- **I67:** `=F67*G67*1.1-H67`
- **M67:** `=L67*J67`
- **N67:** `=L67*K67`
- **I68:** `=F68*G68*1.1-H68`
- **M68:** `=L68*J68`
- **N68:** `=L68*K68`
- **I69:** `=F69*G69*1.1-H69`
- **M69:** `=L69*J69`
- **N69:** `=L69*K69`
- **I70:** `=F70*G70*1.1-H70`
- **M70:** `=L70*J70`
- **N70:** `=L70*K70`
- **I71:** `=F71*G71*1.1-H71`
- **M71:** `=L71*J71`
- **N71:** `=L71*K71`
- **I72:** `=F72*G72*1.1-H72`
- **M72:** `=L72*J72`
- **N72:** `=L72*K72`
- **I73:** `=F73*G73*1.1-H73`
- **M73:** `=L73*J73`
- **N73:** `=L73*K73`
- **I74:** `=F74*G74*1.1-H74`
- **M74:** `=L74*J74`
- **N74:** `=L74*K74`
- **I75:** `=F75*G75*1.1-H75`
- **M75:** `=L75*J75`
- **N75:** `=L75*K75`
- **I76:** `=F76*G76*1.1-H76`
- **M76:** `=L76*J76`
- **N76:** `=L76*K76`
- **I77:** `=F77*G77*1.1-H77`
- **M77:** `=L77*J77`
- **N77:** `=L77*K77`
- **I78:** `=F78*G78*1.1-H78`
- **M78:** `=L78*J78`
- **N78:** `=L78*K78`
- **I79:** `=F79*G79*1.1-H79`
- **M79:** `=L79*J79`
- **N79:** `=L79*K79`
- **I80:** `=F80*G80*1.1-H80`
- **M80:** `=L80*J80`
- **N80:** `=L80*K80`
- **I81:** `=F81*G81*1.1-H81`
- **M81:** `=L81*J81`
- **N81:** `=L81*K81`
- **I82:** `=F82*G82*1.1-H82`
- **M82:** `=L82*J82`
- **N82:** `=L82*K82`

---

## Sheet: Version History

### CSV Data
```csv
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Version,Changes,
,v1,Created,AF/DD
,v2,Simplified fields to neglect peaks & generate one energy req. per Gode feedback from 7/9,AF
,v3,Add peak current and change total current calc to be derived from peaks,DD
,v4,add BOM 2000 and Junction ID to create Elec Master Doc,DD

```

*No formulas found in this sheet.*

---
