import re


def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def normalizeInput(fileInput):
    rules = []
    myTicket = []
    nearbyTickets = []
    nextLineMyTicket = False
    nextNearbyTicket = False
    for line in input:
        ruleMatches = re.match(r'(.+)\:\ (\d+\-\d+)\ or\ (\d+-\d+)', line)
        if ruleMatches:
            rule = [ruleMatches.groups()[0]]
            subRule = [int(ruleMatches.groups()[1].split('-')[0]), int(ruleMatches.groups()[1].split('-')[1])]
            rule.append(subRule)
            subRule = [int(ruleMatches.groups()[2].split('-')[0]), int(ruleMatches.groups()[2].split('-')[1])]
            rule.append(subRule)
            rules.append(rule)
        if nextLineMyTicket:
            for item in line.split(','):
                myTicket.append(int(item))
            nextLineMyTicket = False
        if nextNearbyTicket:
            nearbyTicket = []
            for item in line.split(','):
                nearbyTicket.append(int(item))
            nearbyTickets.append(nearbyTicket)
        if line == 'your ticket:':
            nextLineMyTicket = True
        if line == 'nearby tickets:':
            nextNearbyTicket = True
    return rules, myTicket, nearbyTickets


def checkTickets(rules, myTicket, nearbyTickets):
    errorScanningRate = 0
    for ticket in nearbyTickets:
        for field in ticket:
            valid = False
            for rule in rules:
                if (field >= rule[1][0] and field <= rule[1][1]) or (field >= rule[2][0] and field <= rule[2][1]):
                    valid = True
            if not valid:
                errorScanningRate += field
    return errorScanningRate


input = readFileToList(r'input.dat')
rules, myTicket, nearbyTickets = normalizeInput(input)
# print(f'Rules: {rules}')
# print(f'My ticket: {myTicket}')
# print(f'Nearby tickets: {nearbyTickets}')
errorScanningRate = checkTickets(rules, myTicket, nearbyTickets)
print(f'Error scanning rate: {errorScanningRate}')
