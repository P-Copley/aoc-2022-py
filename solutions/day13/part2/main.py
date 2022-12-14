from functools import cmp_to_key


def comparePackets(packet1, packet2):
    for i, item1 in enumerate(packet1):
        if i >= len(packet2):
            return 1
        item2 = packet2[i]
        if type(item1) == int and type(item2) == list:
            item1 = [item1]
        if type(item1) == list and type(item2) == int:
            item2 = [item2]

        if type(item1) == int and type(item2) == int:
            if item1 > item2:
                return 1
            if item1 < item2:
                return -1
        if type(item1) == list and type(item2) == list:
            result = comparePackets(item1, item2)
            if result == 1 or result == -1:
                return result

    if len(packet1) < len(packet2):
        return -1
    if len(packet1) > len(packet2):
        return 1
    return 0


def solution(lines):
    packets = [[2], [6]]
    for i, line in enumerate(lines):
        pair1Str, pair2Str = line.split('\n')
        packet1 = eval(pair1Str)
        packet2 = eval(pair2Str)
        packets.append(packet1)
        packets.append(packet2)

    packets.sort(key=cmp_to_key(comparePackets))
    return (packets.index([2]) + 1) * (packets.index([6]) + 1)
