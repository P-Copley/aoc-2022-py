import lib.utils
from main import solution;

def test_solves_simple_case():
  testLines = ['a', 'b']
  result = solution(testLines);
  expected = None
  assert result == expected

def xtest_solves_example_case():
  testLines = ['a', 'b']
  result = solution(testLines);
  expected = None
  assert result == expected

def xtest_solves_input_case():
  testLines = lib.utils.readInput()
  result = solution(testLines);
  print(result)