import sys
from gui.gui import *

def main(argv):
    root = Tk()
    root.title("InterCraft Installer")

    w = 700
    h = 423

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    my_gui = Window(root)
    root.resizable(False, False)
    root.mainloop()

    return 0

if __name__ == '__main__':
    main(sys.argv)
