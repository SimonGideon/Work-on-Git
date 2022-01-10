from tkinter import *
def callback():
	global num_clicks
	num_clicks = num_clicks
	label.configure(text='Clicked {} times.'.format(num_clicks))
num_clicks = 0
root = Tk()
label = Label(text='Not Clicked')
button = Button(text='Click me', command=callback)
label.grid(row=0, column=0)
button.grid(row=1, column=0)
mainloop()