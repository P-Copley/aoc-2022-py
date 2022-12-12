import lib.utils
from main import solution


def test_solves_simple_case():
    testLines = [
        'Sabqponm',
        'abcryxxl',
        'accszExk',
        'acctuvwj',
        'abdefghi',
    ]
    result = solution(testLines)
    expected = 31
    assert result == expected
    print(result)


def test_solves_input_case():
    testLines = lib.utils.readInput()
    result = solution(testLines)
    print(result)
