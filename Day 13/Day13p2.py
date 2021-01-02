# This is a WIP. The approach to the problem by brute forcing is probably not realistic or will produce a solution within a reasonable amount of time.


def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def normalizeBusses(busses):
    i = 0
    normalBusses = []
    for bus in busses:
        if bus != 'x':
            normalBusses.append([i, int(bus)])
        i += 1
    return normalBusses


busSchedule = readFileToList(r'input.dat')
busses = busSchedule[1].split(',')
normBusses = normalizeBusses(busses)

foundArrivalTime = False
# i = 1
i = 14285714285714
i = 1
while not foundArrivalTime:
    bussesOnTime = 1
    startTime = i * normBusses[0][1]
    for j in range(1, len(normBusses)):
        if j == 0:
            break
        thisBusLastArrival = int(startTime / normBusses[j][1]) * normBusses[j][1]
        thisBusNextArrival = thisBusLastArrival + normBusses[j][1]
        if thisBusNextArrival == startTime + normBusses[j][0]:
            bussesOnTime += 1
        else:
            break
    if bussesOnTime == len(normBusses):
        foundArrivalTime = True
    i += 1

print('Found start time: {}'.format(startTime))
