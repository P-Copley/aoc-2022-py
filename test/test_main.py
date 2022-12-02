import lib.utils
from main import solution


def xtest_solves_simple_case():
  testLines = [
'A Y',
'B X',
'C Z',
]
  result = solution(testLines);
  expected = 15
  assert result == expected
  print(result)

def xtest_solves_example_case():
  testLines = ['a', 'b']
  result = solution(testLines);
  expected = None
  assert result == expected

def test_solves_input_case():
  testLines = lib.utils.readInput()
  result = solution(testLines);
  print(result)