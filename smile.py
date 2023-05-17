from tkinter import *
top=Tk()
top.geometry("1000x1000")
c= Canvas(top)
arc=c.create_arc(300,300,100,100,start=0,extent=360,fill="red")
top.mainlop()