# generate a similarity score
# for all ints in col1 count matching instances in col2
# multiply the col1 one value by the number of found instances in col2
# sum the calculated vales
from loader import loadFile

def instance_count(target_val, list):
  found_count = 0
  for item in list:
    if int(target_val) == int(item):
      found_count += 1
  return found_count

def main():
  similarity_total = 0
  [col1, col2] = loadFile()

  for i in range(len(col1)):
    count = instance_count(col1[i], col2)
    similarity_total += col1[i] * count

  print(similarity_total)
main()
