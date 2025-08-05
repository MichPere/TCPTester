## 🔹 Check Level of Water Tank; 
##    def-> level_of_water(Ls, Tw)
```tefcha
try
    call: \nCheck Level
    if Ls<=20-BL1
        OPEN 20-K5
        while Ls<=20-BL1
            if Tw>=Ts
            else
                set: \nERROR:=True
                break  
    if if 20-K5 is OPEN
        CLOSE 20-K5    

except
    
    if ERROR==True
    Failed attempt\n fill of water tank 
    if if 20-K5 is OPEN
        CLOSE 20-K5 
Return: \nFlag_Level
End
```
## 🔹 Fill System of Water
##  def-> fill_system_of_water(Pm, Ppa, Ppr, Tw, T1)
```tefcha
try
    try
        call: \nCheck if system\n is empty

        if Pm>20-BP1 && Pm>20-BP2
            OPEN 20-K2 \n\nOPEN 20-K8

            while Ppa>20-BP1 && Ppa>20-BP2 
                if Tw>Ts
                    set: \nERROR:=True
                    break    

            CLOSE 20-K2

    except
        if ERROR==True
            Cooling system \nis not empty, \ndoesn't ability to empty
        if if 20-K2 is OPEN
            CLOSE 20-K2    

    try
        call: \nFill of System

        
        OPEN 20-K8
        START 20-M3
        call: \n Delay(T1)
        20-K8 CLOSE
            
        while Ppr<20-PB2
            if Tw>Ts
                set: \nERROR:=True
                break
        STOP 20-M3
 
    except
        if ERROR==True
            Failed attept\n fill of system
        
        STOP 20-M3
        if if 20-K8 is OPEN
            CLOSE 20-K8

except

    if if 20-M3 is RUN
        STOP 20-M3
    if if 20-K2 is CLOSE
        OPEN 20-K2
    if if 20-K8 is CLOSE
        OPEN 20-K8
Return: \nFlag_Filling   
End
```

## 🔹 Pressure Air Test
##  def-> pressure air test(Ps, Pda, Twa Td, Ts1)
```tefcha
call: \nPressure Air Test
try
    OPEN 20-K6
    while Ps>20-BP1
        if Twa>Ts1
            set: \nERROR:=True
            break

    CLOSE 20-K6

    # Pta - wyliczone minimalne ciśnienie w UUT po zakończeniu testu. 
    Pta:=20-PB1 - Pda

    # Td - czas potrzebny na stabilizacje ciśnienienia
    call: \nDelay(Td)

    if Pta<=20-BP1
        set: \nAir Test Result:=Pass

    else
        set: \nAir Test Result:=FAILED
 

except
    if ERROR==True
    set Pressure Air Test: None
    if if 20-K6 is OPEN
        CLOSE 20-K6
    OPEN 20-K2 \nDelay T:=Ts1 \nCLOSE 20-K2  
Return: Flag_ATerst_Result 
End
```

## 🔹 Pressure Water Test
##  def-> pressure water test(Ppa, Pd, Tw, Td, Ts1)
```tefcha
call: \nWater test presure
try

    while Ppa<20-BP1
        if 20-M3 is STOP
            START 20-M3
        if Tw>=Ts
            set: \nERROR:=True
            break
    STOP 20-M3
    ∆P:=20-BP1-Pd
    call: \nDelay(Td)
    if ∆P<=20-PB1
        set: \nWater Test Result:=Pass
    else
        set: \nWater Test Result:=FAILED
except
    if ERROR==True
    set Pressure Water Test: None
    if if 20-M3 is RUN
        STOP 20-M3
    OPEN 20-K2 \nDelay T:=Ts1 \nCLOSE 20-K2  
Return: Flag_WTest_Result
End
```


## 🔹 Filter Degree of Clogging: Warning 
##  def-> check_of _filter(Ps)
```tefcha
try
    Check of Filter
    while 20-M1 is RUN
        ∆P:=(20-BP2 - 20-BP3)
        if ∆P>Ps 
            Warning:= Rinsing of Filter 
        else
            Warning:= None
        break
except
    Pressure measurement ERROR

Return: Flag_FiltrStatus
End
```

## 🔹 Filter Rinsing of Filter
##  def-> rinsing_of_filter(Tc)
```tefcha
try

    if Flag: Filtr Status  
        if Test is STOPED
            if Push Button\n START Rinsing 
                Locked Start of Test
                while Tc<Ts
                    if if 20-K9 is CLOSE
                        OPEN 20-K9
                    if call: \nCANCEL Rinsing
                        Return status: \nManual stopped
                        break
                    
                
                CLOSE 20-K9
                Unlocked Start of Test
                Warning: None

except
    Manual stopped
    if if 20-K9 is OPEN
        CLOSE 20-K9
    Unlocked Start of Test
Return: CleaningStatus     
End
```

## 🔹 Setting and controlling flow of pumps 
##  def-> flow_control_of_pumps(Fmin, Fn)
```tefcha
Handling pumps
try
    Randomly select LeadPump from {M1, M2}
    Set Fmin:= Fmin
    Set Fn:= Fn

    call: \nStart LeadPump
    Set current_signal to Fmin
    Activate PID regulator for LeadPump with feedback from flowmeter

    if Vn <= 300 then
                    # Fc - current flow
        while Test is Run
            if Fn <= Fc
                call: PID \nRamp Up current signal gradually to achieve Fn
                call: \ncheck_of _filter(Ps)
        call: \nSTOP Lead Pump    
    else
        call: \nStart SecondPump
        Set current_signal = Fmin
        Activate PID regulator for StandbyPump with feedback from flowmeter

        while Test is Run
            if Fc < Fn
                call: PID \nRamp Up current signal gradually to achieve Fn
        call: \nSTOP Second Pump

except
    Handling errors
Return: PumpsStatus 
End
```
## 🔹## 🔹 Emptying water of the system 
##  def-> empting(Ts)
```tefcha
call:\nEmptying water of the system
try

    OPEN 20-K2
    OPEN 20-K6

    while Tt<Ts 
        if Tw>Ts
            set: \nERROR:=True
            break    
    CLOSE 20-K6
    CLOSE 20-K2

except
    if ERROR==True
        Cooling system \nis not empty, \ndoesn't ability to empting
    if if 20-K2 is OPEN
        CLOSE 20-K2 
    if if 20-K6 is OPEN       
    CLOSE 20-K6
Return: EmptingStatus 
End
```


## 🔹 Flushing of the system 
##  def-> flushing(Q, Im, Tp, Tw)
```tefcha
call:\nFlushing of the system 
try
    Randomly select LeadPump from {M1, M2}
    call: \nSTART chosen Pump
    Qt=1
    while Q<=Qt
        Set current signal to Im
        call: \nDelay(Tp)
        Set current signal to I:=4mA
        Qt +=1
        call: \nDelay(Tp)
        if Tw<Ts
            set: \nERROR:=True
            break
    call: \nSTOP chosen Pump

except 
    if ERROR==True
        Flusing is Failed
        call: \nSTOP chosen Pump

Return: FlushingStatus 
End
```

## 🔹 Comparing flows
##  def-> comparing(Im)
```tefcha
try
    Randomly select LeadPump from {M1, M2}
    call: \nSTART chosen Pump
    while RUN pomp
        Set current signal to Im
        if call: \nSTOP
            call: \nSTOP chosen pump
            break
except

End
```
## 🔹 Layout 
##  def-> flayout()
```tefcha
Level of water tank
if Check filtr condition
else 
    Rinsign    

Pressure air test
Fill system of water
if Requirement water test
    Pressure water test
Flushing of the system
if RequirementCompare flows
    Compare flows
Flow control of pumps
call: \nTEST of Panel
Remove water from system


End
```