from tkinter import *
from PIL import ImageTk,Image
import urllib.request
from installlib.installlib import *
#from tkinter.ttk import *

class Window():

    def __init__(self, master):
        self.__master = master

        print(urllib.request.urlretrieve("https://intercraftmc.com/installer/background.png", "intercraftimage.png"))

        self.__image = ImageTk.PhotoImage(Image.open('intercraftimage.png'))
        
        self.__master.configure(background = 'white')

        self.__imageLabel = Label(self.__master, image = self.__image)
        self.__imageLabel.grid(row=0,column=0,columnspan=20,rowspan=20)

        #self.__title = Label(self.__master, text = "InterCraft Installer", font = ("Roboto", 20), background = 'white', foreground = '#292b2c')
        #self.__title.grid(row=9,column=9)

        #self.__spacer = Label(self.__master, background = 'white')
        #self.__spacer.grid(row=9,column=8)

        self.__button = Button(self.__master, text = "Install InterCraft", font = ("Helvetica", 16), command = self.install)
        self.__button.grid(row=11,column=10)
        #Button styling
        self.__button.configure(foreground = 'white')
        self.__button.configure(relief = 'flat')
        self.__button.configure(background = '#008BFF')
        self.__button.configure(highlightbackground = '#006ac2')
        self.__button.configure(activebackground = '#006ac2')
        self.__button.configure(activeforeground = 'white')
        self.__button.configure(highlightcolor = '#006ac2')
        self.__button.configure(overrelief = 'groove')

    def install(self):
        print("Installing InterCraft...")
        installer = InstallLib()
        print("Installing forge...")
        installer.installForge()
        print("Installing mods...")
        installer.installMods()
        print("Configuring profile...")
        installer.installJson
        print("install complete.")
