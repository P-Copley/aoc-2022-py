import re
from functools import reduce


def solution(lines):
    rawTowers, rawMoves = lines
    towerLines = rawTowers.split('\n')
    # create towers - nested arrays
    totalTowers = int((len(towerLines[0]) + 1) / 4)
    towers = [[] for _ in range(0, totalTowers)]

    # populate initial towers
    # ignore number line with len - 2
    for i in range(len(towerLines) - 2, -1, -1):
        mult = 0
        for j in range(1, len(towerLines[i]), 4):
            letter = towerLines[i][j]
            if (letter != ' '):
                # +4 step in the string is offset by 3n -1 to line up with zero indexing
                towerIndex = j - (3 * mult) - 1
                towers[towerIndex].append(letter)
            mult += 1

    moves = rawMoves.split('\n')
    for _, move in enumerate(moves):
        moveCount, fromCol, toCol = map(
            lambda n: int(n), re.findall(r'\d+', move))
        # perform moves
        for i in range(0, moveCount):
            removedItem = towers[fromCol - 1].pop()
            towers[toCol - 1].append(removedItem)

    part1 = reduce(lambda acc, tower: acc + tower[-1], towers, '')
    return part1
