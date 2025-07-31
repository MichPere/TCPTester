## 🔹 Check Level of Water Tank
```tefcha
try
    Check Level
    while !20-BL1
      -20-K5 OPEN
      continue

    -20-K5 CLOSE 


    end
except
    Failed attempt\n fill of water tank

```
## 🔹 Fill System of Water
```tefcha
try
    Fill System 
    
    while 20-BP1 & 20-BP2
        20-K2 & 20-K8 OPEN
    
    20-K2 CLOSE


except
    Cooling system\n is not empty
try
    20-K8 OPEN
    20-M3 START
    while 20-PB2<Ppr
        T- delay
        20-K8 CLOSE
      
    20-M3 STOP
            

except
    Failed attept\n fill of system




    
end
```