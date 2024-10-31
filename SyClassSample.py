class Student:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name =name

class Teacher:
    name =""
    subject = list()

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def getName(self):
        return self.name

    def getSub(self):
        return self.subject
    
    def setName(self, name):
        self.name = name
    
    def setSub(self, sub):
        self.subject = sub

class Parent:
    def __init__(self, name, child, info):
        self.name = name
        self.child = child
        self.info = info

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getChild(self):
        return self.child

    def setChild(self, ch):
        self.child = ch

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

class LSCP:
    def __init__(self, teacherList, sList, pList):
        self.tList = teacherList
        self.sList = sList
        self.pList = pList

    def teachersInfo(self):
        for each in self.tList:
            print("Name: ", end="")
            print(each.getName(), end=" ")
            print("Subject: ", end="")
            print(each.getSub())

    def studentsInfo(self):
        for each in self.sList:
            print("Name: ", end="")
            print(each.getName(), end=" ")
            print("Age: ", end="")
            print(each.getAge())

t1 = Teacher("adam", ("statistic", "cs"))
# print(t1.getName())
# print(t1.getSub())

s1 =Student("hy", 18)
# print(s1.getAge())
# print(s1.getName())

p1 = Parent("a", s1, "01012341234")                                                                                                                                                                                                                                                                                                                                                        
# print(p1.getChild().getName())
# print(p1.getName())
# print(p1.getInfo())

t2 = Teacher("klsdjf", ("asdjklf", "sdjkf"))
# print(t1.getName())
# print(t1.getSub())

s2 =Student("jaslf", 19)
# print(s1.getAge())
# print(s1.getName())

p2 = Parent("b", s2, "01012341234")                                                                                                                                                                                                                                                                                                                                                        
# print(p1.getChild().getName())
# print(p1.getName())
# print(p1.getInfo())

tList = (t1, t2)
sList = (s1, s2)
pList = (p1, p2)

lscp = LSCP(tList, sList, pList)

lscp.teachersInfo()
lscp.studentsInfo()