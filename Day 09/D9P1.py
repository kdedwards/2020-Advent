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


XMASdata=readFileToList(r'input.dat')
print('Unable to find addends for: {}'.format(findOutlier(XMASdata,25)))
