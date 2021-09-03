from tkinter import *
from tkinter import Button, Checkbutton, Entry, Frame, Label, NoDefaultRoot, Radiobutton, StringVar, Tk,ttk,IntVar,messagebox
win=Tk()
win.title("whatsup")
win.iconbitmap("icon.ico")
win.minsize(width=600,height=300)
win.maxsize(width=600,height=300)
def oye():
    if var.get()=="":
        messagebox.showwarning("Warniong","Empty Box")
    elif var.get=="ram":
        messagebox.showinfo("ram","Its harm")    
    elif var.get=="hii":
        messagebox.askretrycancel("hii","Do you want to exit!")    
    elif var.get=="pnna":
        messagebox.askquestion("pnna","Do you want to exit!")    
    elif var.get=="jay":
        messagebox.askyesno("jay","Do you want to exit!")    
    elif var.get=="vijay":
        messagebox.showerror("vijay","Do you want to exit!")  
    else:
        messagebox.askokcancel("all","Do you want to cancle!")      
var=StringVar()
#entry:
ent=Entry(win,width=29,bd=5,textvariable=var)
ent.pack()

#btn:
btn=Button(win,text="Click me",command=oye)
btn.pack()


win.mainloop()