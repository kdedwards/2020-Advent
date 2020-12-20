def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData

def findOutlier(data,window):
    startIndex=0
    while startIndex+window<len(data):
        testList=data[startIndex:startIndex+window]
        testSum=data[startIndex+window]
        #print('Looking in list: {} for {}'.format(testList,testSum))
        foundAddends=False
        for i in range(0, window-1):
            for j in range(i+1, window):
                #print('Does {} == {}?'.format(int(testList[i])+int(testList[j]),testSum))
                if(int(testList[i])+int(testList[j])==int(testSum)):
                    foundAddends=True
                    break
            if foundAddends:
                break
        if foundAddends==False:
            #print('Unable to find addends for {}'.format(testSum))
            return testSum
        startIndex+=1


def findContiguousAddends(data,findSum):
    for windowSize in range(2, len(data)+1):
        startIndex=0
        while startIndex+windowSize<len(data):
            windowSlice=data[startIndex:startIndex+windowSize]
            for i in range(0, len(windowSlice)):
                windowSlice[i] = int(windowSlice[i])
            testSum=sum(windowSlice)
            #print('Sum: {} Slice: {}'.format(testSum, windowSlice))
            if(int(testSum)==int(findSum)):
                print('Found it, window size: {} slice: {}'.format(windowSize,windowSlice))
                return windowSlice
            startIndex+=1

XMASdata=readFileToList(r'input.dat')
findSum=findOutlier(XMASdata,25)
print('Unable to find addends for: {}'.format(findSum))
addends=findContiguousAddends(XMASdata,findSum)
sumOfMinMax=int(min(addends))+int(max(addends))
print('Sum of min/max addends: {}'.format(sumOfMinMax))
