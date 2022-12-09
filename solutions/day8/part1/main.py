

def solution(lines):
    visibleTrees = 0
    forest = [list(map(lambda char: int(char), list(line))) for line in lines]

    def isVisible(x, y, xChange, yChange, treeHeight):
        if (y < 0 or x < 0 or y >= len(forest) or x >= len(forest[0])):
            return True
        if forest[y][x] >= treeHeight:
            return False
        return isVisible(x + xChange, y + yChange, xChange, yChange, treeHeight)

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for y, row in enumerate(forest):
        for x, tree in enumerate(row):
            for _, direction in enumerate(directions):
                yChange, xChange = direction
                if isVisible(x + xChange, y + yChange, xChange, yChange, tree):
                    visibleTrees += 1
                    break

    return visibleTrees
