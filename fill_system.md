## 🔹 Fill System of Water
##  def-> fill_system_of_water
```tefcha
try
    try
        Check if system\n is empty
        
        while 20-BP1 & 20-BP2
            20-K2 & 20-K8 OPEN
        
        if 20-K2 is OPEN
            20-K2 CLOSE



    except
        Cooling system\n is not empty
    try
        Fill of System
        20-K8 OPEN
        20-M3 START
        while 20-PB2<Ppr
            T- delay
            20-K8 CLOSE
        
        20-M3 STOP
                

    except
        Failed attept\n fill of system
        20-M3 STOP

except

    20-M3 STOP
    20-K2 OPEN
    20-K8 OPEN
    
end
```