names = ["Daeju", "Richard", "Kevin", "James", "Warren", "Hwanmin", "Donghyuk", "Taehoon", "Taeyoon", "Beomkyu", "Sieon", "Devyn", "Seoyoung", "Hayoung"]
bDays = ["05_07_06", "05_12_13", "07_08_17", "06_08_25", "06_09_27", "06_05_23", "07_10_01", "06_02_01", "06_07_05", "07_06_02", "06_03_17", "05_11_17", "06_04_03", "07_07_11"]

d = dict(zip(names, bDays))
# print(d)
# for each in d.items():
#     print(each)










# Please complete the functions below

# print out the names in the dictionary 
def printNames(target : dict) -> None:
    for each in target.keys():
        print(each)
# print out their bDays in the dictionary
def printBDays(target : dict) -> None :
    for each in target.values():
        print(each)
# print out the names and their bDays
def printBoth(target : dict) -> None :
    for each in target.items():
        print(each)

######################RUN###################
# print(d)
printBoth(d)