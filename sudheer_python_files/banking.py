from tkinter import *

window=Tk()
window.title("Account details")
window.geometry("250x150")

l1=Label(window,text="Enter Acc/no :")
e1=Entry(window)
b1=Button(window,text="GetBalance")
l2=Label(window,text="Acc Balance  :")
e2=Entry(window)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
b1.grid(row=1,column=1)
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
