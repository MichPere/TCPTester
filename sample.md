## 🔹 Check Level of Water Tank; 
##    def-> level_of_water(Ls, Ts, Tdw)
```tefcha
try
    Check Level
    if 20-BL1<=Ls
        20-K5 OPEN
        while 20-BL1<=Ls
            if Twd>Ts
                ERROR:=True
                break  
    if 20-K5 is OPEN
        20-K5 CLOSE    

except
    
    if ERROR==True
    Failed attempt\n fill of water tank
    if 20-K5 is OPEN
        20-K5 CLOSE
Return: Flag_Level
end
```
## 🔹 Fill System of Water
##  def-> fill_system_of_water(Pp, Tdw, Ts, Ppr)
```tefcha
try
    try
        Check if system\n is empty

        if (20-BP1 & 20-BP2)>Pp
            20-K2 & 20-K8 OPEN
            while (20-BP1 & 20-BP2)>Pp
                if Tdw>Ts
                    ERROR:=True
                    break
            20-K2 & 20-K8 CLOSE    

    except
        if ERROR==True
        Cooling system\n is not empty
        if 20-K2 is OPEN
            20-K2 CLOSE    

    try
        Fill of System

        
        20-K8 OPEN
        20-M3 START
        T1- delay
        20-K8 CLOSE
            
        while 20-PB2<Ppr
            if Tdw>Ts
                ERROR:=True
                break
        20-M3 STOP
        CALL: level_of_water(20-BL1)
 
    except
        if ERROR==True
        Failed attept\n fill of system
        
        20-M3 STOP
        if 20-K8 is OPEN
            20-K8 CLOSE

except

    20-M3 STOP
    20-K2 OPEN
    20-K8 OPEN
Return: Flag_Filling   
end
```

## 🔹 Pressure Test
##  def-> Pressure Test(Ps, Ts, Td, Psw)
```tefcha
try
    Pressure Test (Air)
    20-K6 OPEN
    while 20-BP1<Ps
        if Td>Ts
            ERROR:=True
            break

    20-K6 CLOSE
    if Pressure Test\n      (water)
     
        if 20-BP1>Psp
            Test Result:=True                

        else 
            Test Result:=FAILED

        20-K2 OPEN\n Delay T:=Ts1\n 20-K2 CLOSE 

        CALL: fill_system_of_water()
        Delay T:=Ts2
                        
        if 20-BP1>Psw
            Test Result:=True                
        else 
            Test Result:=FAILED
        20-K2 OPEN\n Delay T:=Ts1\n 20-K2 CLOSE
    else 

except
    if ERROR==True
    Test pressure None
    if 20-K6 is OPEN
        20-K6 CLOSE
    20-K2 OPEN\n Delay T:=Ts1\n 20-K2 CLOSE  
Return: Flag_Result 
end
```

## 🔹 Filter Degree of Clogging: Warning 
##  def-> check_of _filter(Ps)
```tefcha
try
    Check of Filter
    while 20-M1 RUN
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
                20-M_Filter OPEN
                Delay:=Tc
                20-K9 CLOSE
                Unlocked Start of Test
                Warning: None

except
    Manual stopped
    if 20-K9 OPEN
        20-K9 CLOSE

Return: CleaningStatus     
end
```

## 🔹 Setting and controlling flow 
##  def-> flow_control()
```tefcha
try
    flow control


except
    
Return: CleaningStatus   
end
```