from tkinter import * 

window = Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label

my_label = Label(text="나는 Label", font=("Arial", 24, "bold"))
#가운데 정렬
# my_label.pack(expand=True)
#왼쪽, 오른쪽, top, bottom 가능
#my_label.place(x=5, y=115)
my_label.grid(row=0, column=0)
my_label.config(padx=10, pady=10)
new_button = Button(text="hi Click me")
new_button.grid(row=0, column=2)

my_button = Button(text="hello world")
my_button.grid(row=1, column=1)

my_entry = Entry(width=20, bg="skyblue")
my_entry.grid(row=2, column=4)



window.mainloop()