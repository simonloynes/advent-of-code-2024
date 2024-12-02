# https://adventofcode.com/2024/day/2
from loader import getReports
from collections import Counter

def change_direction(a, b) -> str:
  if a > b:
    return "↓"
  if b > a:
    return "↑"
  
  return "↔︎"

def change_limit(a, b) -> bool:
  if a == b:
    return False
  if abs(a - b) > 3:
    return False
  if abs(b - a) > 3:
    return False
  if abs(a - b) == 0:
    return False
  return True

def main():
  reports = getReports()
  evaluated_reports = []
  for report in reports:
    safety_value_set = False # Flag to indicate a safety value has been identified, fast fail to skip loops
    direction = change_direction(report[0], report[1]) # set expected change direction with first two values
    for i in range(len(report)-1):
      if safety_value_set:
        continue
      if change_direction(report[i], report[i + 1]) != direction:
        safety_value_set = True
        evaluated_reports.append("unsafe")
        continue
      if not change_limit(report[i], report[i + 1]):
        safety_value_set = True
        evaluated_reports.append("unsafe")
        continue

    if safety_value_set:
      continue
    
    evaluated_reports.append("safe")
  

  distinct_counts = Counter(evaluated_reports)

  print(distinct_counts)

main()