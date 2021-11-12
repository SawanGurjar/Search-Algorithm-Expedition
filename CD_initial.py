import random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def prepare_testcase(dottedNum):
    data = [0 if i == '.' else i for i in dottedNum]
    grid = []
    row = []
    for i,dottedNum in enumerate(data):
        row.append(int(dottedNum))
        if(i%9 == 8):
            grid.append(row)
            row = []
    return grid