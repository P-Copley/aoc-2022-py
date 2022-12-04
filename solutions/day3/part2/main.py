def solution(lines):
    total = 0
    for i in range(0, len(lines), 3):
        firstBag = set(lines[i])
        secondBag = set(lines[i + 1])
        thirdBag = set(lines[i + 2])
        commonLetter = firstBag.intersection(secondBag).intersection(thirdBag)
        for letter in commonLetter:
            offset = 96 if letter.islower() else 38
            total += ord(letter) - offset
    return total
