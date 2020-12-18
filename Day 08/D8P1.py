def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData

instructions=readFileToList(r'instructions-p1.dat')
executions=[0] * len(instructions)
accumulator=0
instructionPointer=0
print(instructions)
while True:
    if(executions[instructionPointer]>=1):
        print('Program will loop executing this instruction {} instructionPointer at {}. Accumulator value: {}'.format(instructions[instructionPointer],instructionPointer,accumulator))
        break
    instruction=instructions[instructionPointer].split(' ')[0]
    arg=instructions[instructionPointer].split(' ')[1]
    print('SP: {} Op: {} Arg: {}'.format(instructionPointer, instruction, arg))
    if(instruction=='nop'):
        executions[instructionPointer]+=1
        instructionPointer+=1
    elif(instruction=='acc'):
        executions[instructionPointer]+=1
        instructionPointer+=1
        accumulator+=int(arg)
    elif(instruction=='jmp'):
        executions[instructionPointer]+=1
        instructionPointer+=int(arg)
