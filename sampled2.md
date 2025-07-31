## 🔹 Check Level of Water Tank
```tefcha
try
    Check Level
    while !20-BL1
        -20-K5 OPEN
        if -20-BL1
            -20-K5 CLOSE
            continue   
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
        if !(20-BP1 & 20-BP2)
            continue
        else
            20-K2 CLOSE
            break
except
    Cooling system\n is not empty
try
    while 20-PB2<Ppr
        20-K8 OPEN
        20-M3 START
        T- delay
        20-K8 CLOSE
        if 20-PB2>=Ppr
            20-M3 STOP
            break

except
    Failed attept\n fill of system




    
end
```