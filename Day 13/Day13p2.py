# this is a WIP, does not work currently


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


busSchedule = readFileToList(r'input-sample.dat')
busSchedule = readFileToList(r'input.dat')
# startTime = int(busSchedule[0])
startTime = 0
busses = busSchedule[1].split(',')

normBusses = normalizeBusses(busses)

allArrivalTimes = []
for normBus in normBusses:
    start = int(startTime / normBus[1])
    arrivalTimes = set()
    for i in range(200000000):
        arrivalTimes.add(start + i * normBus[1] - normBus[0])
    allArrivalTimes.append(arrivalTimes)
# print(allArrivalTimes[0])
commonArrivals = allArrivalTimes[0] & allArrivalTimes[1]
for i in range(2, len(allArrivalTimes)):
    commonArrivals = commonArrivals & allArrivalTimes[i]

lstCommonArrivals = list(commonArrivals)
lstCommonArrivals.sort()

print(lstCommonArrivals[0])


# futureTime = startTime
# foundBus = False
# while not foundBus:
#    for bus in busses:
#        if futureTime % int(bus) == 0:
#            print('Take bus number {} at time {}. Magic number: {}'.format(bus, futureTime, int(bus) * (futureTime - startTime)))
#            foundBus = True
#    futureTime += 1
