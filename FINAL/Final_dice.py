from tkinter import *
from random import *


window = Tk() # creating obj

# oneToSix = [1,2,3,4,5,6]

window.title("Roll A Dice") # window name
window.geometry("800x800") # size


photo = PhotoImage(file="9590096.png")
pp = Label(window, image=photo)
pp.pack()

def randomInt():
    button.config(text=randint(1,7))

button = Button(window, text="ROLL", width="30", height="1", command=randomInt)
button.pack()



# btn2 = Button(window,)
# btn2.pack()

window.mainloop() # 이벤트 처리
#윈도우 띄워짐



