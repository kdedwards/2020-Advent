with open("map.dat") as mapData:
    tobogganMap = mapData.read().split('\n')

column = 1
treeCount = 0
for row in tobogganMap:
    if(row[column % len(row) - 1] == '#'):
        treeCount += 1
    column += 3
print('Trees hit: {}'.format(treeCount))

# R1, D1
column = 1
treeCountR1D1 = 0
for row in tobogganMap:
    if(row[column % len(row) - 1] == '#'):
        treeCountR1D1 += 1
    column += 1
print('Trees hit (R1D1): {}'.format(treeCountR1D1))

# R3, D1
column = 1
treeCountR3D1 = 0
for row in tobogganMap:
    if(row[column % len(row) - 1] == '#'):
        treeCountR3D1 += 1
    column += 3
print('Trees hit (R3D1): {}'.format(treeCountR3D1))

# R5, D1
column = 1
treeCountR5D1 = 0
for row in tobogganMap:
    if(row[column % len(row) - 1] == '#'):
        treeCountR5D1 += 1
    column += 5
print('Trees hit (R5D1): {}'.format(treeCountR5D1))

# R7, D1
column = 1
treeCountR7D1 = 0
for row in tobogganMap:
    if(row[column % len(row) - 1] == '#'):
        treeCountR7D1 += 1
    column += 7
print('Trees hit (R7D1): {}'.format(treeCountR7D1))

# R1, D2
column = 1
treeCountR1D2 = 0
idx = 0
for row in tobogganMap:
    if(idx % 2 == 0):
        if(row[column % len(row) - 1] == '#'):
            treeCountR1D2 += 1
        column += 1
    idx += 1
print('Trees hit (R1D2): {}'.format(treeCountR1D2))

print('Answer: {}'.format(treeCountR1D1 * treeCountR3D1 * treeCountR5D1 * treeCountR7D1 * treeCountR1D2))
