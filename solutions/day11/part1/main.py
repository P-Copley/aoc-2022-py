import functools
import math
import re


class Monkey:
    def __init__(self, monkeyStr) -> None:
        inputLines = monkeyStr.split('\n')
        self.id = int(re.findall(r'\d+', inputLines[0])[0])
        self.items = [int(n) for n in re.findall(r'\d+', inputLines[1])]
        self.operators = re.findall(r'[\+\-\*\/]|\d+|old', inputLines[2])
        self.testDenominator = int(re.findall(r'\d+', inputLines[3])[0])
        self.trueTarget = int(re.findall(r'\d+', inputLines[4])[0])
        self.falseTarget = int(re.findall(r'\d+', inputLines[5])[0])
        self.inspectCount = 0
        pass

    def inspectItems(self):
        targets = []
        for i, _item in enumerate(self.items):
            self.items[i] = self.calcNewWorry(self.items[i])
            self.items[i] = self.decreaseWorry(self.items[i])
            passesTest = self.testItem(self.items[i])
            targets.append(
                [self.trueTarget if passesTest else self.falseTarget, self.items[i]])
            self.inspectCount += 1
        self.items = []
        return targets

    def calcNewWorry(self, item):
        old = item
        start, operator, value = self.operators
        return eval(f'{start} {operator} {value}', {}, {'old': old})

    def decreaseWorry(self, item):
        return math.floor(item / 3)

    def testItem(self, item):
        return item % self.testDenominator == 0

    def catch(self, item):
        self.items.append(item)

    def __str__(self):
        return f'''
        id: {self.id}
        items: {self.items}
        operation: {self.operators}
        divideBy: {self.testDenominator}
        trueTarget: {self.trueTarget}
        falseTarget: {self.falseTarget}
        '''


def solution(lines):
    monkeys = []
    for _, line in enumerate(lines):
        monkeys.append(Monkey(line))

    for round in range(0, 20):
        for i, monkey in enumerate(monkeys):
            targetMoneys = monkey.inspectItems()
            for _, target in enumerate(targetMoneys):
                targetId, item = target
                monkeys[targetId].catch(item)

    sortedMonkeys = sorted(monkeys, key=functools.cmp_to_key(
        lambda m, n: n.inspectCount - m.inspectCount))
    inspectCounts = [m.inspectCount for m in sortedMonkeys]
    return inspectCounts[0] * inspectCounts[1]
