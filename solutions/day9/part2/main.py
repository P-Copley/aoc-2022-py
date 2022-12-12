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

    def moveDirectlyToJailDoNotPassGoDoNotCollectTwoHundredDollars(self, newX, newY):
        self.x = newX
        self.y = newY
        self.visited.add(f'{self.y},{self.x}')

    def follow(self, knotToFollow):
        dx = knotToFollow.x - self.x
        dy = knotToFollow.y - self.y
        distance = abs(dx) + abs(dy)
        xChange = 0
        yChange = 0
        if (distance == 2):
            xChange = 1 if dx > 1 else -1 if dx < -1 else 0
            yChange = 1 if dy > 1 else -1 if dy < -1 else 0
        if (distance > 2):
            xChange = 1 if dx > 0 else -1
            yChange = 1 if dy > 0 else -1

        self.moveDirectlyToJailDoNotPassGoDoNotCollectTwoHundredDollars(
            self.x + xChange, self.y + yChange)


def solution(lines):
    knots = []
    for i in range(0, 10):
        knots.append(Knot(i))

    for _, line in enumerate(lines):
        direction, distance = line.split(' ')
        distance = int(distance)
        while distance > 0:
            for i, knot in enumerate(knots):
                if i == 0:
                    knot.move(direction, 1)
                else:
                    knot.follow(knots[i - 1])
            distance -= 1

    return knots[9].getVisitCount()
