
import functools



# test = "holamanu"
# print(test[int(len(test)/2):])
types = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
typesDict = {}
cont = 1
for ch in types:
    typesDict[ch] = cont
    cont+=1

def computePriority(acc, line):
    firstHalf = line[:int(len(line)/2)]    
    secondHalf = line[int(len(line)/2):]
    prior = 0
    for c in firstHalf:
        if c in secondHalf:
            prior = typesDict[c]
            break

    return acc + prior

# def computeBadgePriority(acc, line):


with open("day3/input.data") as file:
    lines = file.readlines()
    # res = functools.reduce(computePriority, lines, 0)
    res = 0
    for i in range(0,len(lines),3):
        lineOne = lines[i]
        lineTwo = lines[i+1]
        lineThree = lines[i+2]
        suspects = []
        for c in lineOne:
            if c in lineTwo:
                suspects.append(c)
        
        for c in suspects:
            if c in lineThree:
                res += typesDict[c]
                break

    print(res)
