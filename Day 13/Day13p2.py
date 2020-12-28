

def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


busSchedule = readFileToList(r'C:\Users\dedwards\projects\2020-Advent\Day 13\input-sample.dat')
startTime = int(busSchedule[0])
busses = list(filter(('x').__ne__, busSchedule[1].split(',')))

futureTime = startTime
foundBus = False
while not foundBus:
    for bus in busses:
        if futureTime % int(bus) == 0:
            print('Take bus number {} at time {}. Magic number: {}'.format(bus, futureTime, int(bus) * (futureTime - startTime)))
            foundBus = True
    futureTime += 1
