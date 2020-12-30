import re


def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def normalizeInstructions(rawInstructions):
    instructions = []
    for rawInstruction in rawInstructions:
        instruction = []
        regOperation = re.match(r'^(\w{3,4}).+$', rawInstruction)
        if regOperation.groups()[0] == 'mask':
            operation = 'mask'
            bitMask = re.match(r'^mask\ =\ (.+)$', rawInstruction).groups()[0]
            instruction = [operation, bitMask]
            instructions.append(instruction)
        elif regOperation.groups()[0] == 'mem':
            operation = 'mem'
            address = int(re.match(r'^mem\[(\d+)\]\ =\ (\d+)$', rawInstruction).groups()[0])
            value = int(re.match(r'^mem\[(\d+)\]\ =\ (\d+)$', rawInstruction).groups()[1])
            instruction = [operation, address, value]
            instructions.append(instruction)
    return instructions


def getResultantValue(value, mask):
    bitValue = bin(value).replace('0b', '')
    bitValue = '0' * (36 - len(bitValue)) + bitValue
    resultantBitValue = ''
    for i in range(0, len(mask)):
        if mask[i] != 'X':
            resultantBitValue += mask[i]
        else:
            resultantBitValue += bitValue[i]
    decValue = int(resultantBitValue, 2)
    return decValue


rawProgram = readFileToList(r'input.dat')
program = normalizeInstructions(rawProgram)

memoryMap = {}
for instruction in program:
    if instruction[0] == 'mask':
        bitMask = instruction[1]
    elif instruction[0] == 'mem':
        memoryMap[instruction[1]] = getResultantValue(instruction[2], bitMask)

memorySum = 0
for key, val in memoryMap.items():
    memorySum += val
    # print('Memory Address: {} Value: {}'.format(key, val))
# print(memoryMap)
print('Sum of all non-zero memory: {}.'.format(memorySum))
