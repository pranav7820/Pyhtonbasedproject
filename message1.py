from tkinter import Button, Checkbutton, Entry, Frame, Label, Listbox, NoDefaultRoot, Radiobutton,messagebox, StringVar, Tk,ttk,IntVar
from tkinter.constants import ACTIVE, ANCHOR, END
win=Tk()
win.title("whatsup")
win.iconbitmap("icon.ico")
win.minsize(width=600,height=300)
win.maxsize(width=600,height=300)

def fun():
    if var.get()=="":
        messagebox.showwarning("warning","Empty Box!")
    else:
        messagebox.askquestion("congo","Do you want to exit!")  


#label:
lbl=Label(win,text="Username",bg="green",fg="white",width=10,bd=5)
lbl.place(x=20,y=10)

var=StringVar()

ent=Entry(win,bg="green",fg="white",width=20,bd=5,font="vana",textvariable=var)
ent.place(x=120,y=10)

#button:
btn=Button(win,text="submit",bg="red",fg="white",bd=5,command=fun)
btn.place(x=40,y=50)
win.mainloop()

win.mainloop()