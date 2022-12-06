def solution(lines):
    signal = lines[0][14:]
    prevSeq = [*lines[0][0:14]]
    for i, letter in enumerate(signal):
        print(letter, prevSeq)
        if len(set(prevSeq)) == 14:
            return i + 14
        prevSeq.append(letter)
        prevSeq.pop(0)
    return 0
