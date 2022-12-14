def comparePackets(packet1, packet2, sillyNumCompare=False):
    for i, item1 in enumerate(packet1):
        if i >= len(packet2):
            return False
        item2 = packet2[i]
        if type(item1) == int and type(item2) == list:
            item1 = [item1]
        if type(item1) == list and type(item2) == int:
            item2 = [item2]

        if type(item1) == int and type(item2) == int:
            if item1 > item2:
                return False
            if item1 < item2:
                return True
        if type(item1) == list and type(item2) == list:
            result = comparePackets(item1, item2)
            if result == False or result == True:
                return result

    if len(packet1) < len(packet2):
        return True
    if len(packet1) > len(packet2):
        return False
    return None


def solution(lines):
    orderedSum = 0
    for i, line in enumerate(lines):
        pair1Str, pair2Str = line.split('\n')
        packet1 = eval(pair1Str)
        packet2 = eval(pair2Str)
        isOrdered = comparePackets(packet1, packet2)

        print(packet1, packet2, isOrdered)
        if isOrdered:
            orderedSum += i + 1
    return orderedSum
