'''
LSCP wants to make a name-calculator which finds vowel(s) in the word and returns 
the sum calculated by using the data set, {'a': 66, 'e': 72, 'i': 89, 'o': 73, 'u': 19}.
'''

vowels = {'a': 66, 'e': 72, 'i': 89, 'o': 73, 'u': 19}
names = ["daeju", "seoyoung", "taeyoon", "hwanmin", "beomkyu", "sieon"]


def str2num(word:str) -> int:
    '''
    return the sum of the values for the vowels corresponding to the data set.
    For instance, 'daeju' has three vowels and its sum is 157. 
    '''
    result = 0
    for ele in word:
        if ele in vowels:
            result = result + vowels[ele]
        elif chr(ord(ele) + 32) in vowels:
            result = result + vowels[chr(ord(ele) + 32)]

    return result

print(chr(ord('A') + 32))

def findBiggest(temp:list) -> str:
    '''
    return the word which has the biggest value in the list, vowels.
    '''
    result = -9999999999
    r2 = ""
    for each in temp:
        n = str2num(each)
        if  n > result:
            result = n
            r2 = each
    
    return r2


def findSmallest(temp:list) -> str:
    '''
    reutrn the word which has the smallest value in the list, vowels.
    '''
    result = 9999999999
    r2 = ""
    for each in temp:
        n = str2num(each)
        if  n < result:
            result = n
            r2 = each
    
    return r2


print(findSmallest(names))
print(findBiggest(names))