

def solution(lines):
    visibleTrees = 0
    forest = [list(map(lambda char: int(char), list(line))) for line in lines]

    def isVisible(x, y, xChange, yChange, treeHeight):
        if (y < 0 or x < 0 or y >= len(forest) or x >= len(forest[0])):
            return 0
        if forest[y][x] >= treeHeight:
            return 1
        return isVisible(x + xChange, y + yChange, xChange, yChange, treeHeight) + 1

    maxScenicScore = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for y, row in enumerate(forest):
        for x, tree in enumerate(row):
            scenicScore = 1
            for _, direction in enumerate(directions):
                yChange, xChange = direction
                treeCount = isVisible(
                    x + xChange, y + yChange, xChange, yChange, tree)
                scenicScore *= treeCount
                # print(tree, treeCount)

            if scenicScore > maxScenicScore:
                maxScenicScore = scenicScore

    return maxScenicScore
