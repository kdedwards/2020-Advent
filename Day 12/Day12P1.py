

def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def turnFerry(currentDirection, turnDirection, degrees):
    numTurns = int(degrees) / 90
    cardinals = ['N', 'E', 'S', 'W']
    if turnDirection == 'L':
        newDirection = cardinals[(int(cardinals.index(currentDirection) - 1 * numTurns) % 4)]
    elif turnDirection == 'R':
        newDirection = cardinals[(int(cardinals.index(currentDirection) + 1 * numTurns % 4) % 4)]
    return newDirection


def moveFerry(currentDirection, currentPosition, moveDirection, units):
    if moveDirection == 'F':
        moveDirection = currentDirection
    ferryPositionDelta = {'X': 0, 'Y': 0}
    if moveDirection == 'N':
        ferryPositionDelta['Y'] = units
    elif moveDirection == 'S':
        ferryPositionDelta['Y'] = -1 * units
    elif moveDirection == 'E':
        ferryPositionDelta['X'] = units
    elif moveDirection == 'W':
        ferryPositionDelta['X'] = -1 * units
    currentPosition['X'] = currentPosition['X'] + ferryPositionDelta['X']
    currentPosition['Y'] = currentPosition['Y'] + ferryPositionDelta['Y']
    return currentPosition


navInstructions = readFileToList(r'C:\Users\dedwards\projects\2020-Advent\Day 12\input.dat')
ferryDirection = 'E'
ferryPosition = {'X': 0, 'Y': 0}
print('* Starting Ferry Position: {} Ferry direction: {}'.format(ferryPosition, ferryDirection))

for instruction in navInstructions:
    action = instruction[0:1]
    units = int(instruction[1:len(instruction)])
    # print('** Navigation Action: {} Units: {}'.format(action, units))
    if action == 'L' or action == 'R':
        ferryDirection = turnFerry(ferryDirection, action, units)
    else:
        ferryPosition = moveFerry(ferryDirection, ferryPosition, action, units)
    # print('* Ending Ferry Position: {} Ferry direction: {}'.format(ferryPosition, ferryDirection))
print('* Ending Ferry Position: {} Ferry direction: {}'.format(ferryPosition, ferryDirection))
manhattanDistance = abs(ferryPosition['X']) + abs(ferryPosition['Y'])
print('Manhattan distance of ferry from origin: {}'.format(manhattanDistance))
