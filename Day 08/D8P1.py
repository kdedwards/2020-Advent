def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData

instructions=readFileToList(r'instructions-p1.dat')
executions=[0] * len(instructions)
accumulator=0
stackPointer=0
print(instructions)
while True:
    if(executions[stackPointer]>=1):
        print('Program will loop executing this instruction {} stackPointer at {}. Accumulator value: {}'.format(instructions[stackPointer],stackPointer,accumulator))
        break
    instruction=instructions[stackPointer].split(' ')[0]
    arg=instructions[stackPointer].split(' ')[1]
    print('SP: {} Op: {} Arg: {}'.format(stackPointer, instruction, arg))
    if(instruction=='nop'):
        executions[stackPointer]+=1
        stackPointer+=1
    elif(instruction=='acc'):
        executions[stackPointer]+=1
        stackPointer+=1
        accumulator+=int(arg)
    elif(instruction=='jmp'):
        executions[stackPointer]+=1
        stackPointer+=int(arg)
