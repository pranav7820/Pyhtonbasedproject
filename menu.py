from tkinter import Checkbutton, ttk,Entry, Frame, Label, Listbox, NoDefaultRoot, Radiobutton,messagebox, StringVar, Tk,ttk,IntVar
from tkinter.constants import ACTIVE, ANCHOR, END, HORIZONTAL, LEFT, RIGHT
from tkinter import  *
win=Tk()
win.title("whatsup")
win.iconbitmap("icon.ico")
win.minsize(width=600,height=300)
win.maxsize(width=600,height=300)

def demo():
    pass
main_menu=Menu(win)
win.config(menu=main_menu)
file_menu1=Menu(main_menu)
main_menu.add_cascade(label="File",menu=file_menu1)
file_menu1.add_cascade(label="New Windows")
file_menu1.add_cascade(label="open")
file_menu1.add_cascade(label="Cut")
file_menu2=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=file_menu2)
file_menu2.add_cascade(label="Save")
file_menu2.add_cascade(label="Undo")
file_menu2.add_cascade(label="Cut")
file_menu2.add_cascade(label="Paste")

file_menu3=Menu(main_menu)
main_menu.add_cascade(label="Format",menu=file_menu3)
file_menu3.add_cascade(label="Back")
file_menu3.add_cascade(label="location")
file_menu3.add_cascade(label="Welcome")
file_menu3.add_cascade(label="help")

file_menu4=Menu(main_menu)
main_menu.add_cascade(label="View",menu=file_menu4)
win.mainloop()