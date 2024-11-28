import Sample02 as s02

'''
make a sufficient number of test functions to assure the completeness of the functions you made.
If you can find some failing cases while your code does its work, you will earn an extra point. 
'''

def test_str2num():
    assert s02.str2num("Daeju") == 157

def test_str2num_caps():
    assert s02.str2num("DAEjU") == 157

def test_findBiggest():
    ss = s02
    assert ss.findBiggest(ss.names) == "taeyoon"

def test_findSmallest():
    ss = s02
    assert ss.findSmallest(ss.names) == "hwanmin"
