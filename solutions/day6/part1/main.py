def solution(lines):
    signal = lines[0][4:]
    prevSeq = [*lines[0][0:4]]
    for i, letter in enumerate(signal):
        print(letter, prevSeq)
        if len(set(prevSeq)) == 4:
            return i + 4
        prevSeq.append(letter)
        prevSeq.pop(0)
    return 0
