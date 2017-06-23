import sys
from gui.gui import *

def main(argv):
    root = Tk()
    root.title("InterCraft Installer")

    w = 330
    h = 173

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    my_gui = Window(root)
    root.mainloop()

    return 0

if __name__ == '__main__':
    main(sys.argv)
