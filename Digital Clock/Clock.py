from tkinter import *
from tkinter.ttk import *

from time import strftime


def time():
    strTime = strftime('%I:%M:%S %p')
    label.config(text=strTime)
    label.after(1000, time)


root = Tk()

root.title("Digital Clock")  # Title of windows form.

root.resizable(0, 0)  # fixed size

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() - (windowWidth * 2))
positionDown = int(root.winfo_screenheight() - windowHeight)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))


strTime = strftime("%I:%M:%S %p")
label = Label(root, font=("ds-digital", 55), text=strTime,
              background="black", foreground="cyan")
label.pack()
time()
root.mainloop()
