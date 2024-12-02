def getReports(type = "data"):
    paths = {
      "data": "./input.txt",
      "test": "./test_input.txt"
    }
    file = open(paths[type], "r")
    reports = []
    for line in file.readlines():
      items = [int(x) for x in line.split()]
      reports.append(items)

    file.close()

    return  reports