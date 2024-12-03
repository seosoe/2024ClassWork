import datetime as dt

current = dt.datetime.now()
# print(current.hour)
# print(type(current.hour))

def whatT():
    ch = current.hour
    if ch > 12:
        ch = ch - 12
        print("오후 ", ch, "시 입니다")
    else:
        print("오전 ", ch, "시 입니다")

whatT()