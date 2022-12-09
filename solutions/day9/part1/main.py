

class Knot:
    def __init__(self, name) -> None:
        self.x = 0
        self.y = 0
        self.name = name
        self.visited = set(['0,0'])

    def getVisitCount(self):
        return len(self.visited)

    def move(self, direction, distance):
        if (direction == 'R'):
            self.x += distance
        if (direction == 'L'):
            self.x -= distance
        if (direction == 'D'):
            self.y += distance
        if (direction == 'U'):
            self.y -= distance
        self.visited.add(f'{self.y},{self.x}')

    def moveDirectlyToJailDoNotPassGoDoNotCollectTwoHundredDollars(self, newPos):
        self.x = newPos.x
        self.y = newPos.y

    def follow(self, knotToFollow, direction):
        # distanceAway = knotToFollow.x - self.x + knotToFollow.y - self.y
        # if distanceAway > 1
        # print(f'{self.y},{self.x}', f'{knotToFollow.y},{knotToFollow.x}')

        if direction == 'U' and self.x != knotToFollow.x and (knotToFollow.y - self.y) < -1:
            self.x = knotToFollow.x
        if direction == 'D' and self.x != knotToFollow.x and (knotToFollow.y - self.y) > 1:
            self.x = knotToFollow.x
        if direction == 'R' and self.y != knotToFollow.y and (knotToFollow.x - self.x) > 1:
            self.y = knotToFollow.y
        if direction == 'L' and self.y != knotToFollow.y and (knotToFollow.x - self.x) < -1:
            self.y = knotToFollow.y

        if knotToFollow.x - self.x > 1:
            self.move('R', 1)
        if knotToFollow.x - self.x < -1:
            self.move('L', 1)
        if knotToFollow.y - self.y > 1:
            self.move('D', 1)
        if knotToFollow.y - self.y < -1:
            self.move('U', 1)


def solution(lines):
    head = Knot('head')
    tail = Knot('tail')
    for _, line in enumerate(lines):
        direction, distance = line.split(' ')
        distance = int(distance)
        fallInLineCount = 0
        while distance > 0:
            head.move(direction, 1)
            # print(head.visited)
            tail.follow(head, direction)
            distance -= 1
            fallInLineCount += 1

        # print(tail.getVisitCount(), tail.visited)
    return tail.getVisitCount()
