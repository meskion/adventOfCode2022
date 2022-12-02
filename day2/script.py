import functools


def computePoints(acc, line):
    print(line)
    dict = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }
    return acc + dict.get(line.rstrip('\n'))

def computeWinner(acc, line):
    dict = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }
    return acc + dict.get(line.rstrip('\n'))


# 10 1
# 21 2
# 02 3
# 00 4
# 11 5
# 22 6
# 20 7
# 01 8
# 12 9
# 10 21 2 0 11 22 20 01 12
#  +11-19-2+11+11-2-19+11


with open("day2/input.data") as file:
    lines = file.readlines()
    res = functools.reduce(computeWinner, lines, 0)
    print(res)
