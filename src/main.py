import sys
from gui.gui import *

def main(argv):
    root = Tk()
    root.title("InterCraft Installer")
    root.geometry('{}x{}'.format(330, 174))
    my_gui = Window(root)
    root.mainloop()

    return 0

if __name__ == '__main__':
    main(sys.argv)
