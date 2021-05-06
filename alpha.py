from tkinter import *

alpha = 0
def activate():
  global alpha
  alpha = alpha + 1
  print(alpha)
root = Tk()
root.geometry('400x400')

btn = Button(root, text = "test system", bd = 5, command = activate)

btn.pack(side = 'top')

root.mainloop()