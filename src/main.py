import sys
from main_window import *

def main(argv):

    # Create the main window
    mainWindow = MainWindow()

    # Run the main loop
    mainWindow.mainloop()

    # Return the exit code
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
