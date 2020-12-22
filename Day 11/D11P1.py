from copy import deepcopy


def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def findAdjacencies(floorMap, y ,x):
    adjacencies=[]
    #up&left adjacency
    if(y-1>=0 and x-1>=0):
        adjacencies.append(floorMap[y-1][x-1])
    #up adjacency
    if(y-1>=0):
        adjacencies.append(floorMap[y-1][x])
    #up&right adjacency
    if(y-1>=0 and x+1<len(floorMap[0])):
        adjacencies.append(floorMap[y-1][x+1])
    #left adjacency
    if(x-1>=0):
        adjacencies.append(floorMap[y][x-1])
    #right adjacency
    if(x+1<len(floorMap[0])):
        adjacencies.append(floorMap[y][x+1])
    #down&left adjacency
    if(y+1<len(floorMap) and x-1>=0):
        adjacencies.append(floorMap[y+1][x-1])
    #down adjacency
    if(y+1<len(floorMap)):
        adjacencies.append(floorMap[y+1][x])
    #down&right adjacency
    if(y+1<len(floorMap) and x+1<len(floorMap[0])):
        adjacencies.append(floorMap[y+1][x+1])
    return adjacencies


def interateFloorMap(floorMap):
    newFloorMap=deepcopy(floorMap)
    for y in range(0, len(floorMap)):
        for x in range(0, len(floorMap[0])):
            if(floorMap[y][x]!='.'):
                adjacencies=findAdjacencies(floorMap, y, x)
                if(floorMap[y][x]=='L' and adjacencies.count('#')==0):
                    newFloorMap[y][x]='#'
                if(floorMap[y][x]=='#' and adjacencies.count('#')>=4):
                    newFloorMap[y][x]='L'
    return newFloorMap


def countSeats(floorMap):
    occupiedSeats=0
    for line in floorMap:
        occupiedSeats+=line.count('#')
    return occupiedSeats


def printFloorMap(floorMap):
    for line in floorMap:
        print(line)
    print('-'*50)


floorMapRaw=readFileToList(r'input-p1.dat')
floorMap=[]
for line in floorMapRaw:
    floorMap.append(list(line))    

#printFloorMap(floorMap)
interation=0
while True:
    interation+=1
    newFloorMap=interateFloorMap(floorMap)
    print('Iteration: ',interation)
    if(floorMap==newFloorMap):
        #printFloorMap(floorMap)
        break
    else:
        #printFloorMap(floorMap)
        floorMap=deepcopy(newFloorMap)

print('There are a total of {} occupied seats.'.format(countSeats(floorMap)))