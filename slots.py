
import tkinter 
from tkinter import *
from tkinter import filedialog
import random

root = Tk()
root.title('Slot Machine')
root.geometry("800x600")
root.configure(background= 'teal')

items = ['cherry', 'lemon', 'strawberry', 'diamond', 'seven']
roll1 = None
roll2 = None
roll3 = None
bank = 100
'''
def moneyinp():
    inp = inputtxt.get(1.0, "end-12c")
    lbl.config(text= 'Balance: ' +inp)

inputtxt = Tk.Text()
inputtxt.place(x=0, y=500)
'''

balance = Text(root, height =1, width =5, font = ('Arial', 20))
balance.place(x=0, y=500)
button1 = Button(text = 'Submit', width = 10, bd = 3)
button1.place(x=0, y=550)

button2 = Button(text = 'BET 1x', width = 20, bd = 2)
button2.place(x=125, y=550)

button3 = Button(text = 'BET 2x', width = 20, bd = 2)
button3.place(x=330, y=550)

button4 = Button(text = 'BET 5x', width = 20, bd = 2)
button4.place(x=550, y=550)

def askPlayer():
    global bank

def play():
    global roll1, roll2, roll3
    askPlay = askPlayer()
    roll1 = spins()
    roll2 = spins()
    roll3 = spins()

def spins():
    randomnum= random.randint(0,4)
    return items[randomnum]

root.mainloop()
