import lib.utils
from main import solution


def xtest_solves_simple_case():
    testLines = [
        '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3''',

        '''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
    ]
    result = solution(testLines)
    expected = 4
    assert result == expected
    print(result)


def test_solves_input_case():
    testLines = lib.utils.readInput()
    result = solution(testLines)
    print(result)
