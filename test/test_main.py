import lib.utils
from main import solution


def test_solves_simple_case():
    testLines = [
        'R 4',
        'U 4',
        'L 3',
        'D 1',
        'R 4',
        'D 1',
        'L 5',
        'R 2',
    ]
    result = solution(testLines)
    expected = 13
    assert result == expected
    print(result)


def xtest_solves_input_case():
    testLines = lib.utils.readInput()
    result = solution(testLines)
    print(result)
