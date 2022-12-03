def solution(lines):
    total = 0
    for _, bag in enumerate(lines):
        firstCompartment = set(bag[0: len(bag) // 2])
        secondCompartment = set(bag[len(bag) // 2::])
        misplacedLetters = firstCompartment.intersection(secondCompartment)
        for letter in misplacedLetters:
            offset = 96 if letter.islower() else 38
            total += ord(letter) - offset
    return total
