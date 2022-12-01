def solution(lines):
  elfNum = 1;
  elfTotal = 0;
  top3Elves = [0, 0, 0]

  for i, weight in enumerate(lines):
      if weight == '' or i == len(lines) - 1:
        addToTop3(top3Elves, elfTotal)
        elfNum += 1;
        elfTotal = 0;
      else:
        elfTotal += int(weight)
        
  return sum(top3Elves)

def addToTop3(list, valueToInsert, index = 2):
  if index < 0: return None;
  if list[index] < valueToInsert:
    nextValue = list[index]
    list[index] = valueToInsert
    return addToTop3(list, nextValue, index - 1);
  return addToTop3(list, valueToInsert, index - 1)