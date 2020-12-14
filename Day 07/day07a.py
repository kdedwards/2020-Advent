import re

def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData

def normalizeBagData(bagData):
    bagContents=[]
    for bagDef in bagData:
        #print(bagDef)
        bagContent={'outerBag':[],'innerBags':[]}
        bagContent['outerBag']=bagDef.split(' bags')[0]
        innerBags=bagDef.split(' bags contain ')[1]
        #print(innerBags)
        innerBags=re.sub(r'\d+\ ','',innerBags)
        innerBags=re.sub(r'\ bags\.{0,1}','',innerBags)
        innerBags=innerBags.split(', ')
        #print(innerBags)
        bagContent['innerBags']=innerBags
        print(bagContent)
        bagContents.append(bagContent)
    return bagContents

def lookInBagFor(outerBags, outerBag, findBag):
    foundOne=False
    outerBag=outerBags[outerBag]
    innerBags=outerBag['innerBags']
    for innerBag in innerBags:
        foundOne=lookInBagFor(outerBags, innerBag, findBag)
        if(innerBag==findBag):
            foundOne=True
    return foundOne

bagInfo=readFileToList('C:\\Users\\kdedw\\projects\\2020-Advent\\Day 07\\bagdata.dat')
bagInfo=normalizeBagData(bagInfo)
#print(bagInfo)

#lookInBagFor(bagInfo,'bright olive','dotted white')


#for outerBag in bagInfo['outerBag']:
#    lookInBagFor(outerBag, 'shiny gold')