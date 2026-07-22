from tkinter import *
import random

root = Tk()
root.title("Puzzle Rearrangement Game")

numbers = list(range(1, 9)) + [" "]
random.shuffle(numbers)

buttons = []

def swap(i):
    blank = numbers.index(" ")
    if i in [blank-1, blank+1, blank-3, blank+3]:
        numbers[blank], numbers[i] = numbers[i], numbers[blank]
        update()

def update():
    for i in range(9):
        buttons[i]["text"] = numbers[i]

for i in range(9):
    btn = Button(root, text=numbers[i], font=("Arial", 20),
                 width=5, height=3,
                 command=lambda i=i: swap(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

update()
root.mainloop()
