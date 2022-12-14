import lib.utils
from main import solution


def test_solves_simple_case():
    testLines = lib.utils.readInput(True)
    result = solution(testLines)
    expected = 140
    assert result == expected
    print(result)


def test_solves_input_case():
    testLines = lib.utils.readInput(False)
    result = solution(testLines)
    print(result)
