from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
import urllib.request
from installlib.installlib import *
#from tkinter.ttk import *

class Window():

    def __init__(self, master):
        self.__master = master

        print(urllib.request.urlretrieve("https://intercraftmc.com/installer/background.png", "intercraftimage.png"))

        self.__image = ImageTk.PhotoImage(Image.open('intercraftimage.png'))

        try:
            os.remove('intercraftimage.png')
        except Exception as e:
            print("Couldn't delete the intercraft image...")

        self.__installer = InstallLib()

        self.__master.configure(background = 'white')

        self.__imageLabel = Label(self.__master, image = self.__image)
        self.__imageLabel.grid(row=0,column=0,columnspan=20,rowspan=20)

        #self.__title = Label(self.__master, text = "InterCraft Installer", font = ("Roboto", 20), background = 'white', foreground = '#292b2c')
        #self.__title.grid(row=9,column=9)

        #self.__spacer = Label(self.__master, background = 'white')
        #self.__spacer.grid(row=9,column=8)

        self.__button1 = Button(self.__master, text = "Install InterCraft", font = ("Helvetica", 20), cursor = "hand2")
        self.__button1.grid(row=10,column=10)

        self.__button2 = Button(self.__master, text = "Set Minecraft directory", font = ("Helvetica", 12), cursor = "hand2")
        self.__button2.grid(row=11,column = 10)

        #Button styling
        self.__button1.configure(foreground = 'white')
        self.__button1.configure(relief = 'flat')
        self.__button1.configure(background = '#008BFF')
        self.__button1.configure(activebackground = '#006ac2')
        self.__button1.configure(activeforeground = 'white')
        self.__button1.bind("<Enter>", self.onHover)
        self.__button1.bind("<Leave>", self.onLeave)

        self.__button2.configure(foreground = 'white')
        self.__button2.configure(relief = 'flat')
        self.__button2.configure(background = '#008BFF')
        self.__button2.configure(activebackground = '#006ac2')
        self.__button2.configure(activeforeground = 'white')
        self.__button2.bind("<Enter>", self.onHover2)
        self.__button2.bind("<Leave>", self.onLeave2)
        self.__button2.bind("<ButtonRelease-1>", self.getDirectory)


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
        if newDirectory == "":
            pass
        else:
            self.__installer.setMCpath(newDirectory)


    def install(self, event):
        print("Installing InterCraft...")
        print("Installing forge...")
        self.__installer.installForge()
        print("Installing mods...")
        self.__installer.installMods()
        print("Configuring profile...")
        self.__installer.installJson
        print("install complete.")
