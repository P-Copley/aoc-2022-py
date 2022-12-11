def solution(lines):
    register = 1
    cycleNum = 1
    instructionIndex = 0
    instruction = lines[instructionIndex]
    pendingOperations = {}
    signalStrengths = []
    while cycleNum < 221:
        # print(cycleNum, pendingOperations, register)
        if (cycleNum - 20) % 40 == 0:
            signalStrengths.append(cycleNum * register)
            print(cycleNum, register)
        if len(pendingOperations) == 1:
            if cycleNum in pendingOperations:
                register += pendingOperations[cycleNum]
                pendingOperations.pop(cycleNum)
                instructionIndex += 1
                if instructionIndex < len(lines):
                    instruction = lines[instructionIndex]
        else:
            if instruction[0:4] == 'addx':
                value = int(instruction.split(' ')[1])
                pendingOperations[cycleNum + 1] = value
            else:
                instructionIndex += 1
                instruction = lines[instructionIndex]

        cycleNum += 1
    print(signalStrengths)
    return sum(signalStrengths)
