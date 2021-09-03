from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('500x300')
root.title('LogIn Form')
frame = Frame(root)
frame.pack()

def message():
    tkinter.messagebox.showinfo("Submited","Thank For Register")

nlab = Label(frame , text="Log In Form",justify = CENTER,font=('Oswald',20)).grid(row=1,columnspan=4,ipady=30)

lab1 = Label(frame,text='Enter Your Name',relief=FLAT,bd=2).grid(row=2,column=1,ipady=20)
en1 = Entry(frame).grid(row=2,column=2)

lab2 = Label(frame,text='Enter Your Password',relief=FLAT,bd=2).grid(row=3,column=1)
en2 = Entry(frame).grid(row=3,column=2)

bu = Button(frame,text="Submit" , command=message).grid(row=4,columnspan=4,pady=(15,0))

root.mainloop()