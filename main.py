from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
window = Tk()
window.geometry('300x300')
window.title('Welcome')
style = ttk.Style()
style.configure('BW.TLabel', foreground='black', background='white')


def show_message():
    messagebox.showinfo('Message for you, sir', 'It\'s me again, Margaret')


label1 = ttk.Label(text='Default Text', style='BW.TLabel')
label1.grid(row=1, column=1)
button1 = ttk.Button(window, text='Push Me!', command=show_message())
button1.grid(row=2, column=2)

window.mainloop()
