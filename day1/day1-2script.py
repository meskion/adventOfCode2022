

with open("day1/input1") as file:
    MaxTop = 0
    MaxMid = 0
    MaxBot = 0
    Current = 0
    for line in file:
        if line in ["", " ", "\n"]:
            if Current > MaxTop:
                MaxBot = MaxMid
                MaxMid = MaxTop
                MaxTop = Current
            elif Current > MaxMid:
                MaxBot = MaxMid
                MaxMid = Current    
            elif Current >MaxBot:
                MaxBot = Current

            Current = 0
        else:
            Current += int(line)

    print(MaxTop + MaxMid + MaxBot)
