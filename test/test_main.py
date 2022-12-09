import lib.utils
from main import solution


def test_solves_simple_case():
    testLines = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]
    result = solution(testLines)
    expected = 8
    assert result == expected
    print(result)


def xtest_solves_input_case():
    testLines = lib.utils.readInput()
    result = solution(testLines)
    print(result)
