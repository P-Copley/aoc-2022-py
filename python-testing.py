name = 'Paul'

GREETING = f'hello {name}'

print(GREETING)

multi = '''
  SELECT *
  FROM multi_line
'''

# print(multi)
list = ['fellowship', 'the two towers']
list.append('return of the king')

print(list)
fellowship, towers, *otherShitIDontCareAboutButHaveToDefine = list;
print(fellowship, towers)

tuple = (1, 2, 3)
one, two, three = tuple

print(one, two, three)

setOfPrimes = {2, 3, 5}
setOfPrimes.add(7)

secondPrimeSet = {11, 13}

setOfPrimes.update(secondPrimeSet)

print(setOfPrimes)

me = {
  'name': 'Paul',
  'age': 36
}

print(me)

from lib.utils import readInput

# lib.utils.readInput()
input = readInput()
print(input)