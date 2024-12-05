import datetime as dt

def whatT():
    
    current = dt.datetime.now()
    ch = current.hour
    
    if ch > 12:
        # ch = ch - 12
        print("오후 ", ch, "시 입니다")
    else:
        print("오전 ", ch, "시 입니다")

whatT()