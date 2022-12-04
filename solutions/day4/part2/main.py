def solution(lines):
    total = 0
    for _, line in enumerate(lines):
        elf1, elf2 = line.split(',')
        start1, end1 = elf1.split('-')
        start2, end2 = elf2.split('-')

        elf1Range = set(range(int(start1), int(end1) + 1))
        elf2Range = set(range(int(start2), int(end2) + 1))

        overlappingIds = elf1Range.intersection(elf2Range)
        if len(overlappingIds) > 0:
            total += 1
    return total
