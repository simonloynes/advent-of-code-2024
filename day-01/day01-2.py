# https://adventofcode.com/2024/day/1

from loader import getSortedInputs

def instance_count(target_val, list):
  found_count = 0
  for item in list:
    if int(target_val) == int(item):
      found_count += 1
  return found_count

def main():
  similarity_total = 0
  [col1, col2] = getSortedInputs()

  for i in range(len(col1)):
    count = instance_count(col1[i], col2)
    similarity_total += col1[i] * count

  print(similarity_total)
main()
