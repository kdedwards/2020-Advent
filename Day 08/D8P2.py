def readFileToList(fileName):
    with open(fileName) as Data:
        retData = Data.read().split('\n')
    return retData


def swapInstruction(instructions,location):
    function=instructions[location].split(' ')[0]
    operand=instructions[location].split(' ')[1]
    print('Changing instruction at index {}.'.format(location))
    if(function=='jmp'):
        newFunction='nop'
        newInstruction=newFunction+' '+operand
        instructions[location]=newInstruction
    elif(function=='nop'):
        newFunction='jmp'
        newInstruction=newFunction+' '+operand
        instructions[location]=newInstruction


def testInstructions(instructions):
    executions=[0] * len(instructions)
    accumulator=0
    instructionPointer=0
    #print(instructions)
    while True:
        if(executions[instructionPointer]>=1):
            print('Program will loop executing this instruction {} instructionPointer at {}. Accumulator value: {}'.format(instructions[instructionPointer],instructionPointer,accumulator))
            return False
        if(instructionPointer==len(instructions)-1):
            print('Program successfully terminated. Accumulator value: {}'.format(accumulator))
            return True
        function=instructions[instructionPointer].split(' ')[0]
        operand=instructions[instructionPointer].split(' ')[1]
        #print('SP: {} Fn: {} Operand: {}'.format(instructionPointer, function, operand))
        if(function=='nop'):
            executions[instructionPointer]+=1
            instructionPointer+=1
        elif(function=='acc'):
            executions[instructionPointer]+=1
            instructionPointer+=1
            accumulator+=int(operand)
        elif(function=='jmp'):
            executions[instructionPointer]+=1
            instructionPointer+=int(operand)


instructions=readFileToList(r'instructions-p2.dat')
functionSearchPointer=0
for instruction in instructions:
    function=instruction.split(' ')[0]
    operand=instruction.split(' ')[1]
    if(function=='jmp' or function=='nop'):
        instructionsCopy=instructions.copy()
        swapInstruction(instructionsCopy,functionSearchPointer)
        if(testInstructions(instructionsCopy)):
            break
    functionSearchPointer+=1