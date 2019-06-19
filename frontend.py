#Import everything from tkinter
from tkinter import *

#Create Window object
window=Tk()
window.geometry("800x600")
window.title("ERSGUI")
window.iconbitmap(r"ersgui_icon.ico")

#define ListBox
list1=Listbox(window, height=30, width=100)
list1.grid(row=5,column=0,rowspan=2,columnspan=2)

#define buttons
b1=Label(window, relief=RAISED, text="Select Image(s)", width=16)
b1.grid(row=4,column=3)

b2=Label(window, relief=RAISED, text="Select All", width=16)
b2.grid(row=5,column=3)

b3=Label(window, relief=RAISED, text="Clear List", width=16)
b3.grid(row=7,column=3)

b4=Label(window, relief=RAISED, text="Output Folder", width=16)
b4.grid(row=9,column=3)

b2=Label(window, relief=RAISED, text="Upscale", width=16)
b2.grid(row=13,column=3)

#define scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


window.mainloop()