import lib.utils
from main import solution


def xtest_solves_simple_case():
    testLines = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']
    result = solution(testLines)
    expected = 157
    assert result == expected
    print(result)


def test_solves_input_case():
    testLines = lib.utils.readInput()
    result = solution(testLines)
    print(result)
