temp = ["05_07_06", "05_12_13", "07_08_17", "06_08_25", "06_09_27", "06_05_23", "07_10_01", "06_02_01", "06_07_05", "07_06_02", "06_03_17", "05_11_17", "06_04_03", "07_07_11"]

for each in temp:
    print(each)
    result = list()
    for e in each.split("_"):
        result.append(int(e))
    print(result)