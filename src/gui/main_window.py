from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import ttk
from threading import Thread
from urllib.request import urlretrieve
from PIL import ImageTk, Image
import math

from installlib.installlib import *


class MainWindow(Tk):

    WIDTH = 700
    HEIGHT = 419
    IMAGE_URL = "https://intercraftmc.com/installer/background.png"
    IMAGE_NAME = "intercraftbg.png"

    def __init__(self):
        super(MainWindow, self).__init__()

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        x = (screenWidth/2) - (MainWindow.WIDTH/2)
        y = (screenHeight/2) - (MainWindow.HEIGHT/2)

        self.title("InterCraft Installer")
        self.resizable(False, False)
        self.geometry('%dx%d+%d+%d' % (MainWindow.WIDTH, MainWindow.HEIGHT, x, y))

        self.preInit()
        self.initGui()

        self.setDirectoryDisplay(self.__installer.getMcPath())


    def preInit(self):

        self.tk.call('wm', 'iconphoto', self._w, utils.image('icon.ico'))
        self.__image = utils.image('background.png')
        self.__installer = InstallLib()
        self.__installErrors = {}


    def initGui(self):

        self.configure(background = 'white')

        self.__imageLabel = Label(self, image = self.__image)
        self.__imageLabel.grid(row=0, column=0, columnspan=20, rowspan=20)

        self.__finished = 0
        self.__progress = IntVar(0)
        self.__progressBar = ttk.Progressbar(self, orient='horizontal', length=300, variable=self.__progress)

        #self.__title = Label(self, text = "InterCraft Installer", font = ("Roboto", 20), background = 'white', foreground = '#292b2c')
        #self.__title.grid(row=9,column=9)

        self.__button1 = Button(self, text = "Install InterCraft", font = ("Helvetica", 20), cursor = "hand2")
        self.__button1.grid(row=10,column=10)

        self.__button2 = Button(self, text = "Change Minecraft directory", font = ("Helvetica", 12), cursor = "hand2")
        self.__button2.grid(row=11,column = 10)

        self.__directoryDisp = Label(self, background = '#111111', foreground = 'white', font = ("Helvetica", 10), width = 87, height = 2)
        self.__directoryDisp.grid(row=19,column=10)

        #Button styling
        self.__button1.configure(foreground = 'white')
        self.__button1.configure(relief = 'flat')
        self.__button1.configure(background = '#008BFF')
        self.__button1.configure(activebackground = '#006ac2')
        self.__button1.configure(activeforeground = 'white')
        self.__button1.bind("<Enter>", self.onHover)
        self.__button1.bind("<Leave>", self.onLeave)
        self.__button1.bind("<ButtonRelease-1>", self.install)

        self.__button2.configure(foreground = 'white')
        self.__button2.configure(relief = 'flat')
        self.__button2.configure(background = '#008BFF')
        self.__button2.configure(activebackground = '#006ac2')
        self.__button2.configure(activeforeground = 'white')
        self.__button2.bind("<Enter>", self.onHover2)
        self.__button2.bind("<Leave>", self.onLeave2)
        self.__button2.bind("<ButtonRelease-1>", self.getDirectory)


    def clean(self):
        self.__installer.clean()


    def onHover(self, event):
        self.__button1.configure(background = '#006ac2')


    def onLeave(self, event):
        self.__button1.configure(background = '#008BFF')


    def onHover2(self, event):
        self.__button2.configure(background = '#006ac2')


    def onLeave2(self, event):
        self.__button2.configure(background = '#008BFF')


    def getDirectory(self, event):
        newDirectory = askdirectory()
        if newDirectory != "":
            self.__installer.setMcPath(newDirectory)
            self.setDirectoryDisplay(self.__installer.getMcPath())


    def setDirectoryDisplay(self, path):
        self.__directoryDisp.configure(text = "Minecraft location: " + utils.reformatPath(path))


    def install(self, event):
        self.__finished = 0
        self.__button1.configure(state = 'disabled')
        self.__button1.configure(cursor = 'arrow')
        self.__button1.configure(background = '#222222')
        self.__button1.unbind("<ButtonRelease-1>")
        self.__button1.unbind("<Enter>")
        self.__button1.unbind("<Leave>")
        self.__button2.grid_forget()
        self.__progressBar.grid(row=11, column=10)
        print("Installing InterCraft...")
        print("Installing forge...")
        t1 = Thread(target = self.__installer.installForge, args = (self.installFinish,))
        t1.daemon = True
        t1.start()
        print("Installing mods...")
        t2 = Thread(target = self.__installer.installMods, args = (self.installFinish,))
        t2.daemon = True
        t2.start()
        print("Configuring profile...")
        self.__installer.installJson(self.installFinish)


    def installFinish(self, result, name = None, message = None):
        self.__finished += 1
        if not result:
            self.__installErrors[name] = message

        self.__progress.set(int(math.ceil(self.__finished/3.0*100)))

        if self.__finished == 3:
            print("install complete.")

            if len(self.__installErrors.keys()) == 0:
                showinfo("InterCraft Installer", "Install Complete.")
            else:
                errorString = ''
                for key, value in self.__installErrors.items():
                    errorString += '\n' + value
                showerror("InterCraft Installer - Errors occured", errorString[1:])
            self.quit()


    def quit(self):
        self.clean()
        super(MainWindow, self).quit()
