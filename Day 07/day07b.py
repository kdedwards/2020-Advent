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
        #innerBags=re.sub(r'\d+\ ','',innerBags)
        innerBags=re.sub(r'no\ other','0 other',innerBags)
        innerBags=re.sub(r'\ bags\.{0,1}','',innerBags)
        innerBags=re.sub(r'\ bag\.{0,1}','',innerBags)
        innerBags=innerBags.split(', ')
        for innerBag in innerBags:
            dictInnerBags={}
            innerBagCount=int(innerBag.split(' ')[0])
            innerBagName=re.sub(r'\d+\ ','',innerBag)
            dictInnerBags[innerBagName]=innerBagCount
            bagContent['innerBags'].append(dictInnerBags)
        #print(bagContent)
        bagContents.append(bagContent)
    return bagContents

def lookInBagFor(outerBags, findBag):
    bagsInsideCount=0
    for outerBag in outerBags:
        print('Looking in: {}'.format(outerBag['outerBag']))
        if(outerBag['outerBag']==findBag):
                innerBags=outerBag['innerBags']
                for innerBag in innerBags:
                    print(innerBag)
                    #innerInnerBags=lookInBagFor(outerBags, findBag)
    #return bagsInsideCount


bagInfo=readFileToList(r'C:\Users\kdedw\projects\2020-Advent\Day 07\day07b-example.dat')
bagInfo=normalizeBagData(bagInfo)
#for bag in bagInfo:
#    print(bag)
lookForBag='shiny gold'
totalBagCount=0
#for outerBag in bagInfo:
    #print(lookInBagFor(bagInfo,outerBag['outerBag'],lookForBag))
lookInBagFor(bagInfo, lookForBag)
#    if(outerBagCanHold==True):
#        #print('Bag {} can eventually hold {}.'.format(outerBag['outerBag'], lookForBag))
#        outerBagsCan+=1
#print('{} bags can eventually contain {} bag.'.format(outerBagsCan, lookForBag))
