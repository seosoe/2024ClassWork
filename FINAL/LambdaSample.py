temp = ""
for each in range(65,91,1):
    temp = temp + chr(each) + " "


(lambda temp: [temp := temp + chr(x) + " " for x in range(65, 91, 1)])("")
print(temp)

[(lambda x : chr(x))(x) for x in range(65,91)]
print([(lambda x : chr(x))(x) for x in range(65,91)])

#소문자를 대문자로 대문자를 소문자로 람다로 적어오기!