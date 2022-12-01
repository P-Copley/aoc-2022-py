import lib.utils
from main import solution


def xtest_solves_simple_case():
  testLines = ['1000',
'2000',
'3000',
'',
'4000',
'',
'5000',
'6000',
'',
'7000',
'8000',
'9000',
'',
'',
'',
'10000',
'']
  result = solution(testLines);
  expected = 25000
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