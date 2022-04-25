from tkinter import *

window = Tk()
window.title("몇 mile ??")
window.minsize(width=400, height=100)
window.config(background="white", padx=20, pady=20)

#숫자 입력창
input_num = Entry(bg="orange", width=10)
input_num.grid(row=1, column=1)
input_num.focus()

#from 라벨
from_label = Label(text="miles", bg="white")
from_label.grid(row=1, column=2)

#is equal to 라벨
equal_label = Label(text="를 바꾸면", bg="white")
equal_label.grid(row=2, column=0)

#result 보여주는 라벨
result_label = Label(text="0", bg="white")
result_label.grid(row=2, column=1)

#to 라벨
to_label = Label(text="km", bg="white")
to_label.grid(row=2, column=2)


#from to 바꾸기 기능
def change_measure():
    origin_from = from_label.cget("text")
    origin_to = to_label.cget("text")
    from_label.config(text=origin_to)
    to_label.config(text=origin_from)

#from to 바꾸기 버튼
change_btn = Button(text="단위바꾸기", command=change_measure)
change_btn.grid(row=2, column=3)


#계산기능
def calcul():
    from_measure = float(input_num.get())
    if from_label.cget("text") == "miles":
        result_label.config(text=round(from_measure * 1.609344, 2))
    else:
        result_label.config(text=round(from_measure * 0.621371, 2))
        
#계산 버튼
cal_button = Button(text="계산", command=calcul)
cal_button.config(padx=3, pady=3)
cal_button.grid(row=4, column=2)















window.mainloop()