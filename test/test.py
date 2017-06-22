from tkinter import *
from tkinter.ttk import *

class TheGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Hellow, I am in trouble")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
root.geometry('{}x{}'.format(400, 300))
my_gui = TheGUI(root)
root.mainloop()
