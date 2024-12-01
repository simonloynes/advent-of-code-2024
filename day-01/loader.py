import array as arr

def getSortedInputs():
    file = open("./input.txt", "r")
    col1 = arr.array('i', [])
    col2 = arr.array('i', [])
    for line in file.readlines():
      items = line.split(" ")
      col1.append(int(items[0]))
      col2.append(int(items[3]))

    file.close()

    return [sorted(col1), sorted(col2)]