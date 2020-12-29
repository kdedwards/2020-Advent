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


busSchedule = readFileToList(r'C:\Users\dedwards\projects\2020-Advent\Day 13\input.dat')
busses = busSchedule[1].split(',')
normBusses = normalizeBusses(busses)
# print(normBusses)
arrivalStart = 4347826086956
arrivalWindowSize = 1000000
arrivalStartFound = False
while not arrivalStartFound:
    allArrivalTimes = []
    print('Searching times: {} - {}'.format(arrivalStart, arrivalStart + arrivalWindowSize))
    for normBus in normBusses:
        arrivalTimes = set()
        for i in range(1, arrivalWindowSize):
            arrivalTimes.add(arrivalStart + i * normBus[1] - normBus[0] + normBusses[0][1])
        allArrivalTimes.append(arrivalTimes)
    commonArrivals = allArrivalTimes[0] & allArrivalTimes[1]
    for i in range(2, len(allArrivalTimes)):
        commonArrivals = commonArrivals & allArrivalTimes[i]
    if len(commonArrivals) != 0:
        lstCommonArrivals = list(commonArrivals)
        lstCommonArrivals.sort()
        print(lstCommonArrivals[0])
        arrivalStartFound = True
    arrivalStart = arrivalStart + arrivalWindowSize
