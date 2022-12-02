

with open("input1") as file:
    Max = 0
    Current = 0
    for line in file:
        
        if line in [""," ","\n"]:
            if Current > Max:
                Max = Current
            Current = 0
        else:
            print("found " + line)
            Current += int(line)
    
    print(Max)
