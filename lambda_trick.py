from tkinter import *
import string
alphabets = string.ascii_uppercase
def callback(x):
	label.configure(text='Button {} clicked'.format(alphabets[x]))
root = Tk()
label = Label()
label.grid(row=1, column=0, columnspan=26)
buttons = [0]*26
for i in range(26):
	buttons[i] = Button(text=alphabets[i], command = lambda x = i: callback(x))
	buttons[i].grid(row=0, column=i)
mainloop()