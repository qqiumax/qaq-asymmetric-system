from tkinter import *
from tkinter import messagebox
import hashlib
import random

window = Tk()
window.geometry('700x300+450+100')
window.title('verify')

def click():
    s1 = (s1_enter.get())
    s2 = s2_enter.get()
    h = h_enter.get()
    p = p_enter.get()
    k = k_enter.get()
    p = int(hashlib.sha1(p.encode("utf-8")).hexdigest(),16)
    pwo = open("key.pwd", "r", encoding = "utf-8")
    pwd = int(pwo.read())
    pwo.close()
    if p == pwd:
        pass
s1_label = Label(window,text = ('signature 1 file name'),font = ('宋体',20),fg = 'black')
s1_label.grid(row = 0, column = 1)

s1_enter = Entry(window,font = ('宋体',20),fg = 'black')
s1_enter.grid(row = 0,column = 2)


s2_label = Label(window,text = ('signature2 file name'),font = ('宋体',20),fg = 'black')
s2_label.grid(row = 1, column = 1)

s2_enter = Entry(window,font = ('宋体',20),fg = 'black')
s2_enter.grid(row = 1,column = 2)

h_label = Label(window,text = ('message file name'),font = ('宋体',20),fg = 'black')
h_label.grid(row = 2, column = 1)

h_enter = Entry(window,font = ('宋体',20),fg = 'black')
h_enter.grid(row = 2,column = 2)


p_label = Label(window,text = ('public key file name'),font = ('宋体',20),fg = 'black')
p_label.grid(row = 3, column = 1)

p_enter = Entry(window,font = ('宋体',20),fg = 'black')
p_enter.grid(row = 3,column = 2)

k_label = Label(window,text = ('Password'),font = ('宋体',20),fg = 'black')
k_label.grid(row = 4, column = 1)

k_enter = Entry(window,font = ('宋体',20),fg = 'black')
k_enter.grid(row = 4,column = 2)



sub_button = Button(window,text = ('Submit'),font = ('宋体',20),fg = 'black')
sub_button.grid(row = 6,column = 2)
sub_button.config(command = click)


window.mainloop()
