'''
Check if it is a triangle or not
Print out the results and return nothing
ex)
True
True
False
False
True
True

'''
triangleList = [(7,7,2),(2,2,3), (3,3,3), (3,4,5), (5,6,1), (4,5,9), (9,3,1), (3,5,8)]

def biggest(givenT):
    result = -99
    for each in givenT:
        if each > result:
            result = each
    return result

def eqT(tup):
    return tup[0] == tup[1] == tup[2]

def isosT(tup):
    return tup[0] == tup[1] or tup[1] == tup[2] or tup[0] == tup[2]

def isosChecker(tup):
    a, b, c = tup
    if a+b>c and b+c>a and a+c>b:
        return True
    return False

def checker(givenList: list) -> None:
    
    for tup in givenList:
        if eqT(tup):
            print(True)
        elif eqT(tup) != True and isosT(tup):
            print(isosChecker(tup))
        else:
            first = biggest(tup)
            sum = 0
            for num in tup:
                if num != first:
                    sum = sum + num
        
            if first < sum:
                print(True)
            else:
                print(False)
        


        



# print(biggest((2,4,7)))
# tfinder((2,4,8))
 
checker(triangleList)