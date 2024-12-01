# https://adventofcode.com/2024/day/1
from loader import getSortedInputs

def main():
  [col1, col2] = getSortedInputs()
  distance_total = 0
  for i in range(len(col1)):
    greater = 0
    lesser = 0
    if col1[i] > col2[i]:
      greater = col1[i]
      lesser = col2[i]
    else:
      greater = col2[i]
      lesser = col1[i]

    distance_total += greater - lesser

  print(distance_total)

main()