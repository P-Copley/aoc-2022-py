
class Node:
    def __init__(self, name, parent, type, value) -> None:
        self.name = name
        self.parent = parent
        self.value = value
        self.type = type
        self.size = 0
        self.children = []

    def addChild(self, childNode):
        self.children.append(childNode)
        if (childNode.type == 'file'):
            self.size += int(childNode.value)
            parent = self.parent
            while (parent != None):
                parent.size += int(childNode.value)
                parent = parent.parent

    def getChild(self, childName):
        if childName == '..':
            return self.parent
        for i, child in enumerate(self.children):
            if child.name == childName:
                return child

    def traverseDirs(self, cb):
        cb(self)
        for i, child in enumerate(self.children):
            if child.type == 'dir':
                child.traverseDirs(cb)

    def __str__(self):
        return f'{self.name} - {self.value} - {len(self.children)} - {self.size}'
        return f'{self.name} - {self.value} - {len(self.children)} - {[str(child) for child in self.children]}'


def solution(lines):
    root = Node('/', None, 'dir', None)
    cwd = root
    for _, line in enumerate(lines[1:]):

        if (line[0: 2] != '$ '):
            sizeOrType, name = line.split(' ')
            type = 'dir' if sizeOrType == 'dir' else 'file'
            size = 0 if sizeOrType == 'dir' else sizeOrType
            cwd.addChild(Node(name, cwd, type, size))

        if (line[0: 4] == '$ cd'):
            cwd = cwd.getChild(line[5:])

    diskSize = 70000000
    requiredSpace = 30000000
    freeSpace = diskSize - root.size

    potentialDirsToDelete = []

    def collectDeleteOptions(dir):
        nonlocal potentialDirsToDelete
        if dir.size + freeSpace > requiredSpace:
            potentialDirsToDelete.append(dir)

    root.traverseDirs(collectDeleteOptions)

    return min([dir.size for dir in potentialDirsToDelete])
