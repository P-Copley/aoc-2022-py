def solution(lines):
    register = 1
    cycleNum = 1
    instructionIndex = 0
    instruction = lines[instructionIndex]
    pendingOperations = {}
    crt = ['']
    crtIndex = 0
    offset = 0
    while cycleNum < 241:
        if register == cycleNum - 1 - offset or register == cycleNum - offset or register == cycleNum - 2 - offset:
            crt[crtIndex] += '#'
        else:
            crt[crtIndex] += '.'
        if cycleNum % 40 == 0:
            crt.append('')
            crtIndex += 1
            offset += 40
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
                if instructionIndex < len(lines):
                    instruction = lines[instructionIndex]

        cycleNum += 1
    print('\n')
    print("\n".join(crt))
    return
