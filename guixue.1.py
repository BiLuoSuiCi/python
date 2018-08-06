# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
root.title("hello world")
root.geometry()

def print_item(event):
    print(lb.get(lb.curselection()))
    
var = StringVar()
lb = Listbox(root,  listvariable = var)
list_item = [1, 2, 3, 4]         #控件的内容为1 2 3 4
for item in list_item:
    lb.insert(END, item)
lb.delete(2, 4)                  #此时控件的内容为1 3

var.set(('a', 'ab', 'c', 'd'))   #重新设置了，这时控件的内容就编程var的内容了。动态调整内容
print(var.get())
lb.bind('<ButtonRelease-1>', print_item)
lb.pack()

root.mainloop()