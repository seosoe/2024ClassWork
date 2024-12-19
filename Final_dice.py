from tkinter import *
from random import *


window = Tk()  # creating obj

window.title("Roll A Dice")  # window name
window.geometry("2000x2000")  # size

# 처음 이미지를 위한 Label 생성
photo = PhotoImage(file="./FINAL/9590096.png")
pp = Label(window, image=photo)

pp.pack()

# 랜덤 이미지를 변경하는 함수
def randomInt():
    
    # randomImage = PhotoImage(file="~/Documents/2024ClassWork/FINAL/dice-152174_640.png")
    randomImage = PhotoImage(file="./FINAL/" + str(randint(1, 6)) + ".png")
    pp.config(image=randomImage)
    pp.image = randomImage  # 이미지를 유지하기 위해 필요


# 버튼을 클릭하면 randomInt() 함수 실행
button = Button(window, text="ROLL", width="30", height="1", command=randomInt)
button.pack()

window.mainloop()  # 이벤트 처리

