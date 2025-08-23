## 🔹 Check Level of Water Tank; 
##    def-> level_of_water(Ls, Ts, Tw)
```tefcha
try
    Check Level
    if Ls>=20-BL1
        OPEN 20-K5
        while Ls>=20-BL1
            if Tw>=Ts
            else
                ERROR:=True
                break  
    if if 20-K5 is OPEN
        CLOSE 20-K5    

except
    
    if ERROR==True
    Failed attempt\n fill of water tank 
    if if 20-K5 is OPEN
        CLOSE 20-K5 
Return: Flag_Level
end
```
## 🔹 Fill System of Water
##  def-> fill_system_of_water(Pm, Ppa, Ppr, Tw, Ts)
```tefcha
try
    try
        Check if system\n is empty

        if Pm>20-BP1 && Pm>20-BP2
            OPEN 20-K2 \n\nOPEN 20-K8

            while Ppa>20-BP1 && Ppa>20-BP2 
                if Tw>Ts
                    ERROR:=True
                    break    
            CLOSE 20-K2 \nCLOSE 20-K8

    except
        if ERROR==True
        Cooling system\n is not empty
        if if 20-K2 is OPEN
            CLOSE 20-K2    

    try
        Fill of System

        
        OPEN 20-K8
        START 20-M3
        T1- delay
        20-K8 CLOSE
            
        while Ppr>20-PB2
            if Tw>Ts
                ERROR:=True
                break
        STOP 20-M3
        CALL: level_of_water(20-BL1)
 
    except
        if ERROR==True
        Failed attept\n fill of system
        
        STOP 20-M3
        if if 20-K8 is OPEN
            CLOSE 20-K8

except

    STOP 20-M3
    OPEN 20-K2
    OPEN 20-K8
Return: Flag_Filling   
end
```

## 🔹 Pressure Test
##  def-> pressure Test(Ps, Psw, Pta, Td, Ts1, Ts2)
```tefcha
try
    Pressure Test (Air)
    OPEN 20-K6
    while Ps>20-BP1
        if Td>Ts
            ERROR:=True
            break

    CLOSE 20-K6
    Delay:= Td
    if Pta<=20-BP1
        Test Air Result:=Pass
    
        if Pressure Test\n      (water)
        
            if Psp<20-BP1
                Test Result:=Pass                

            else 
                Test Result:=FAILED

            OPEN 20-K2\n Delay T:=Ts1 \nCLOSE 20-K2 

            CALL: fill_system_of_water()
            Delay T:=Ts2
                            
            if Psw<20-BP1
                Test Result:=Pass                
            else 
                Test Result:=FAILED
            OPEN 20-K2 \nDelay T:=Ts1 \nCLOSE 20-K2
        else
    else
        Test Result:=FAILED
 

except
    if ERROR==True
    Test pressure None
    if if 20-K6 is OPEN
        CLOSE 20-K6
    OPEN 20-K2 \nDelay T:=Ts1 \nCLOSE 20-K2  
Return: Flag_Terst_Result 
end
```

## 🔹 Filter Degree of Clogging: Warning 
##  def-> check_of _filter(Ps)
```tefcha
try
    Check of Filter
    while 20-M1 is RUN
        ∆P:=(20-BP2 - 20-PB3)
        if ∆P>Ps 
            Warning:= Rinsing of Filter 
        else
            Warning:= None
        break
except
    Pressure measurement ERROR

Return: Flag_FiltrStatus
end
```

## 🔹 Filter Degree of Clogging
##  def-> degree_of_cligging(Tc)
```tefcha
try

    if Flag: Filtr Status  
        if Test is STOPED
            if Push Button\n START Rinsing 
                Locked Start of Test
                OPEN 20-M_Filter
                Delay:=Tc
                CLOSE 20-K9
                Unlocked Start of Test
                Warning: None

except
    Manual stopped
    if if 20-K9 is OPEN
        CLOSE 20-K9

Return: CleaningStatus     
end
```

## 🔹 Setting and controlling flow 
##  def-> flow_control()
```tefcha
try
    flow control
    while P<PB1 && 


except
    
Return: CleaningStatus   
end
```