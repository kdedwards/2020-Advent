#from collections import Counter


def readFileToIntList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
        for i in range(0, len(retData)):
            retData[i]=int(retData[i])
    return retData


def findDifferences(adapters):
    differences=[]
    for i in range(0, len(adapters)-1):
        differences.append(adapters[i+1]-adapters[i])
    return differences


adapters=readFileToIntList(r'input.dat')
# Add in the outlet as the first 'adapter'
adapters.append(0)
adapters.sort()
# Add in the device adatper as the last 'adapter'
adapters.append(adapters[len(adapters)-1]+3)
differences=findDifferences(adapters)
print('Differences of 1: {} 2: {} 3: {}'.format(differences.count(1),differences.count(2),differences.count(3)))
print('Number of 1-jolt differences * number of 3-jolt differences: {}'.format(differences.count(1)*differences.count(3)))
