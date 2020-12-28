import re


def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def normalizeBagData(bagData):
    bagContents = []
    for bagDef in bagData:
        # print(bagDef)
        bagContent = {'outerBag': [], 'innerBags': []}
        bagContent['outerBag'] = bagDef.split(' bags')[0]
        innerBags = bagDef.split(' bags contain ')[1]
        # print(innerBags)
        innerBags = re.sub(r'\d+\ ', '', innerBags)
        innerBags = re.sub(r'\ bags\.{0,1}', '', innerBags)
        innerBags = re.sub(r'\ bag\.{0,1}', '', innerBags)
        innerBags = innerBags.split(', ')
        # print(innerBags)
        bagContent['innerBags'] = innerBags
        # print(bagContent)
        bagContents.append(bagContent)
    return bagContents


def lookInBagFor(outerBags, selectedOuterBag, findBag):
    foundOne = False
    for outerBag in outerBags:
        # print('Looking in: {}'.format(outerBag['outerBag']))
        if outerBag['outerBag'] == selectedOuterBag:
            innerBags = outerBag['innerBags']
            for innerBag in innerBags:
                foundInInnerBag = lookInBagFor(outerBags, innerBag, findBag)
                if innerBag == findBag or foundInInnerBag:
                    foundOne = True
    return foundOne


bagInfo = readFileToList('day07.dat')
bagInfo = normalizeBagData(bagInfo)
# print(bagInfo)
lookForBag = 'shiny gold'
outerBagsCan = 0
for outerBag in bagInfo:
    # print(lookInBagFor(bagInfo,outerBag['outerBag'],lookForBag))
    outerBagCanHold = lookInBagFor(bagInfo, outerBag['outerBag'], lookForBag)
    if outerBagCanHold is True:
        # print('Bag {} can eventually hold {}.'.format(outerBag['outerBag'], lookForBag))
        outerBagsCan += 1
print('{} bags can eventually contain {} bag.'.format(outerBagsCan, lookForBag))

# 235 bags
