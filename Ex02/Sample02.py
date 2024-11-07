l1 = [1,2,3,4,5,66,77,88,99]
l2 = [-1, -2, -3, 5,6,7,99]



'''
return a sum of all elements in the given list
'''
def finder(givenList : list) -> int:
    temp = 0
    for each in givenList:
        temp = temp + each

    return temp


######################RUN#################
print(finder(l1))
print(finder(l2))
