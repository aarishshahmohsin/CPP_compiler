import os
from os.path import exists
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

cpp_file = sys.argv[1]

if not cpp_file.endswith(".cpp"):
    cpp_file += ".cpp"

win = Tk()
win.title("CPP Compiler")

height = 700
width = 350 

win.geometry("{}x{}".format(width, height))

text = scrolledtext.ScrolledText(win, wrap=tk.WORD,  height=10, font=("Calibri", 15))
text.grid(column=0, row=2, pady=10, padx=10)
text.pack()

# clearing the input 
def delete():
   text.delete("1.0","end")

b1= Button(win, text= "Delete",command= delete)
b1.pack(pady=10)

def show(ans):
    to_be_opened = ''

    if ans == 1:
        to_be_opened = 'out'
    else:
        to_be_opened = 'err'

    f = open(to_be_opened)
    content = f.read()
    f.close()

    newlabel.config(text=""+content)


def put_in_input():
    string = text.get(1.0, "end-1c")
    f = open('in', 'w')
    f.truncate(0)
    f.write(string)
    f.close()


# showing the output
def run_file():

    put_in_input()

    if not os.system('g++ ' + cpp_file + ' -o a') == 0:
        os.system("g++ " + cpp_file + ' -o a 2> err')
        show(0)
        return

    os.system('g++ ' + cpp_file + ' -o a -Wall')
    os.system("./a < in > out")
    show(1)

b2=ttk.Button(win, text="Compile", command=run_file)
b2.pack(pady=10)
b2.pack

newlabel = Label(win, text="")
newlabel.pack()

win.mainloop()

ar = ['in', 'out', 'err', 'a']
for i in ar:
    if exists(i):
        os.system("rm {}".format(i))
