names = ["Daeju", "Richard", "Kevin", "James", "Warren", "Hwanmin", "Donghyuk", "Taehoon", "Taeyoon", "Beomkyu", "Sieon", "Devyn", "Seoyoung", "Hayoung"]
bDays = ["05_07_06", "05_12_13", "07_08_17", "06_08_25", "06_09_27", "06_05_23", "07_10_01", "06_02_01", "06_07_05", "07_06_02", "06_03_17", "05_11_17", "06_04_03", "07_07_11"]

d = dict(zip(names, bDays))
# print(d)

def numerify(target : dict):
    result = list()
    for each in target.values():
        r = each.split("_")
        rr = ""
        for e in r:
            rr = rr + e
        result.append(int(rr))
    
    return result

# numerify(d)

# find the oldest kid. Return his/her name
def finder01(target : dict) -> str:
    ageL = numerify(target)
    result = min(ageL)

    resultList = list(target.keys())
    for each in range(0, len(ageL)):
        if result == ageL[each]:
            r = resultList[each]
    return r + ": " +target[r]


print(finder01(d))

# find the youngeset kid. Return his/her name
def finder02(target : dict) -> str:
    ageL = numerify(target)
    result = max(ageL)

    resultList = list(target.keys())
    for each in range(0, len(ageL)):
        if result == ageL[each]:
            r = resultList[each]
    return r + ": " +target[r]

        
print(finder02(d))