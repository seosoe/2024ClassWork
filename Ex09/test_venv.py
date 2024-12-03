import os

def test_currentDirectory():
    absPath = os.getcwd()
    pathName = absPath.split('/')[-1]

    assert pathName == 'Ex09'


def test_venvDicretory():
    dirList = os.listdir()
    result = False
    if 'lscp_venv' in dirList:
        result = not result
    
    assert result


def test_moduleChecker():
    os.system('pip list > pipList')
    f = open("./pipList", "r")
    target = f.read()
    targetList = target.split("\n")[2:]
    result = False
    
    if 'beautifulsoup4 4.12.3' in targetList:
        result = not result

    assert result