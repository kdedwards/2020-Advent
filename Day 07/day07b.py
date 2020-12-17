# Have yet to solve this one.

import re

def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData

def normalizeBagData(bagData):
    bagContents=[]
    for bagDef in bagData:
        #print(bagDef)
        bagContent={'outerBag':[],'innerBags':{}}
        bagContent['outerBag']=bagDef.split(' bags')[0]
        innerBags=bagDef.split(' bags contain ')[1]
        print(innerBags)
        innerBags=re.sub(r'no\ other','0 other',innerBags)
        innerBags=re.sub(r'\ bags\.{0,1}','',innerBags)
        innerBags=re.sub(r'\ bag\.{0,1}','',innerBags)
        innerBags=innerBags.split(', ')
        for innerBag in innerBags:
            innerBagCount=int(innerBag.split(' ')[0])
            innerBagName=re.sub(r'\d+\ ','',innerBag)
            bagContent['innerBags'][innerBagName]=int(innerBagCount)
        bagContents.append(bagContent)
    return bagContents

def lookInBagFor(outerBags, findBag):
    bagsInsideCount=0
    for outerBag in outerBags:
        if(outerBag['outerBag']==findBag):
                print('Looking in: {}'.format(outerBag['outerBag']))
                innerBags=outerBag['innerBags']
                for key, value in innerBags.items():
                    if(value==0):
                        return 1
                    innerBagCount=lookInBagFor(outerBags, key)
                    bagsInsideCount+=value*innerBagCount
    return bagsInsideCount


bagInfo=readFileToList(r'C:\Users\dedwards\projects\2020-Advent\Day 07\day07b-example.dat')
bagInfo=normalizeBagData(bagInfo)
for bag in bagInfo:
    print(bag)
lookForBag='shiny gold'
totalBagCount=0
print(lookInBagFor(bagInfo, lookForBag))
