## 🔹 Check Level of Water Tank; 
##    def-> level_of_water
```tefcha
try
    Check Level
    while !20-BL1
      -20-K5 OPEN
      continue
    
    if 20-K5 is OPEN
        20-K5 CLOSE 


    end
except
    Failed attempt\n fill of water tank
    20-K5 CLOSE

```