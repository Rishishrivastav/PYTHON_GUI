from tkinter import *
rishi=Tk()
rishi.geometry("500x500")
rishi.title("program by rishi")
title=Label(rishi,text="Addmision form :",font="ariel 20 bold",bg="red")
title.pack(fill="both")

l1=Label(rishi,text="enter the radius:",bg="green",fg="red")
l1.place(x=100,y=100)
e1=Entry(rishi,bg="yellow")
e1.place(x=200,y=100)

l2=Label(rishi,text="roll no:",bg="green",fg="red")
l2.place(x=100,y=150)
e2=Entry(rishi,bg="yellow")
e2.place(x=200,y=150)

l3=Label(rishi,text="class",bg="green",fg="red")
l3.place(x=100,y=200)
e3=Entry(rishi,bg="yellow")
e3.place(x=200,y=200)

b=Button(rishi,text="result",bg="green",fg="red")
b.place(x=250,y=250)

