import tkinter

root = tkinter.Tk()

root.title('ces')
root.geometry('300x270+550+230')


label = tkinter.Label(root,text='事实上')
label.grid()

entry = tkinter.Entry(root)

entry.grid(row=0,column=1)

text = tkinter.Listbox(root,width=40,height=10)

text.grid(row=1,columnspan=2)

button = tkinter.Button(root,text='ss')
button.grid(row=2,column=0,sticky=tkinter.W)

button = tkinter.Button(root,text='www')
button.grid(row=2,column=1,sticky=tkinter.E)



root.mainloop()

