## 🔹 Check Level of Water Tank; 
##    def-> level_of_water
```tefcha
try
    Check Level
    if !20-BL1
        20-K5 OPEN
        while !20-BL1 
            if Twd>Ts
                ERROR:=True
                break  
    if 20-K5 is OPEN
        20-K5 CLOSE    
    end
except
    
    if ERROR==True
    Failed attempt\n fill of water tank
    if 20-K5 is OPEN
        20-K5 CLOSE

```
## 🔹 Fill System of Water
##  def-> fill_system_of_water
```tefcha
try
    try
        Check if system\n is empty

        if 20-BP1 & 20-BP2
            20-K2 & 20-K8 OPEN
            while 20-BP1 & 20-BP2
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
    
end
```

## 🔹 Pressure Test
##  def-> Pressure Test
```tefcha
try
    Pressure Test (Air)
    20-K6 OPEN
    while 20-BP1<Ps
        if Td>Ts
            ERROR:=True
            break

    20-K6 CLOSE
    Delay T:=Ts1
    
    if 20-BP1>Psp
        Test Result:=True                

    else 
        Test Result:=FAILED

    20-K2 OPEN


except
    if ERROR==True
    Test pressure failed
    if 20-K6 is OPEN
        20-K6 CLOSE
    20-K2 OPEN

   

```