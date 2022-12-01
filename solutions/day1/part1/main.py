def solution(lines):
  elfNum = 1;
  elfTotal = 0;
  maxTotal = 0;
  maxElfNum = 1;

  for i, weight in enumerate(lines):
      # print(currElfNum, weight, elfTotal, maxTotal)
      if weight == '':
        if elfTotal > maxTotal:
          maxTotal = elfTotal
        elfNum += 1;
        elfTotal = 0;
      else:
        elfTotal += int(weight)

      if i == len(lines) - 1:
        if elfTotal > maxTotal:
          maxTotal = elfTotal
  
  return maxTotal

