import lib.utils
from main import solution


def test_solves_simple_case():
    testLines = lib.utils.readInput(True)
    result = solution(testLines)
    expected = 13
    assert result == expected
    print(result)


def xtest_solves_input_case():
    testLines = lib.utils.readInput(False)
    result = solution(testLines)
    print(result)
