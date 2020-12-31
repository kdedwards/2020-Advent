from copy import deepcopy


def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def lookDirection(floorMap, y, x, yFactor, xFactor):
    i = 1
    while True:
        newY = y + i * yFactor
        newX = x + i * xFactor
        if newY < 0 or newX < 0 or newY > len(floorMap) - 1 or newX > len(floorMap[0]) - 1:
            return False
        if floorMap[newY][newX] == '#':
            return True
        elif floorMap[newY][newX] == 'L':
            return False
        i += 1


def findDirectionalAdjacencies(floorMap, y, x):
    adjacencies = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if lookDirection(floorMap, y, x, i, j):
                    adjacencies.append('#')
    return adjacencies


def interateFloorMap(floorMap):
    newFloorMap = deepcopy(floorMap)
    for y in range(0, len(floorMap)):
        for x in range(0, len(floorMap[0])):
            if floorMap[y][x] != '.':
                adjacencies = findDirectionalAdjacencies(floorMap, y, x)
                if floorMap[y][x] == 'L' and adjacencies.count('#') == 0:
                    newFloorMap[y][x] = '#'
                if floorMap[y][x] == '#' and adjacencies.count('#') >= 5:
                    newFloorMap[y][x] = 'L'
    return newFloorMap


def countSeats(floorMap):
    occupiedSeats = 0
    for line in floorMap:
        occupiedSeats += line.count('#')
    return occupiedSeats


def printFloorMap(floorMap):
    for line in floorMap:
        print(line)
    print('-' * 50)


floorMapRaw = readFileToList(r'input-p1.dat')
floorMap = []
for line in floorMapRaw:
    floorMap.append(list(line))
# printFloorMap(floorMap)
interation = 0
while True:
    interation += 1
    newFloorMap = interateFloorMap(floorMap)
    print('Iteration: ', interation)
    if(floorMap == newFloorMap):
        # printFloorMap(floorMap)
        break
    else:
        # printFloorMap(floorMap)
        floorMap = deepcopy(newFloorMap)

print('There are a total of {} occupied seats.'.format(countSeats(floorMap)))
