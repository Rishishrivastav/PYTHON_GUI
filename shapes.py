from tkinter import*
top=Tk()
c=Canvas(top,bg="black",width=1200,height=1200)
#circle
oval=c.create_oval(300,300,100,100,fill="red")
txet=c.create_text(310,310,text="circle",fill="white",font="ariel 20 bold underline")
#rectangle
line=c.create_line(600,200,800,200,fill="white",width=5)
line=c.create_line(800,200,800,400,fill="white",width=5)
line=c.create_line(800,400,600,400,fill="white",width=5)
line=c.create_line(600,400,600,200,fill="white",width=5)
text=c.create_text(670,425,text="rectangle",font="ariel 25 bold underline",fill="white")

#triangle
line=c.create_line(400,300,600,600,fill="white",width=5)
line=c.create_line(600,600,200,600,fill="white",width=5)
line=c.create_line(200,600,400,300,fill="white",width=5)
text=c.create_text(350,625,text="triangle",font="ariel 25 bold underline",fill="white")

#arc
arc=c.create_arc(700,600,500,450,start=50,extent=60,fill="blue")
#boder
line=c.create_line(90,90,90,900,fill="blue",width=5)
line=c.create_line(90,90,900,90,fill="blue",width=5)
line=c.create_line(90,600,600,600,fill="blue",width=5)
line=c.create_line(90,90,90,900,fill="blue",width=5)
c.pack()
mainloop()
