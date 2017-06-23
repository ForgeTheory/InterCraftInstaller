import os
import urllib.request
import subprocess
import zipfile
import json
import random
import datetime

class InstallLib():

    def __init__(self):
        self.__homePath = os.path.expanduser("~")
        self.__MCpath = ""

        infoJson = urllib.request.urlopen("https://intercraftmc.com/repository/intercraft.json")
        self.__info = json.loads(infoJson.read().decode())

        self.__lastVersionID = self.__info['forge']['name']
        self.__forgeURL = 'https://intercraftmc.com/repository/forge/' + self.__info['forge']['file']

        if os.name == 'nt':
            self.__MCpath = os.path.join(self.__homePath, 'AppData/Roaming/.minecraft')
        else:
            self.__MCpath =  os.path.join(self.__homePath, '.minecraft')


    def setMCpath(self, path):
        self.__MCpath = path


    def getMCpath(self):
        return self.__MCpath


    def generateProfileKey(self):
        chars = '0123456789abcdef'
        result = ''
        for i in range(32):
            result += chars[random.randint(0, 15)]
        return result


    def removeFile(self, path):
        try:
            os.remove(path)
        except Exception as e:
            print("The file " + path + " could not be removed.")


    def installForge(self, callback):
        print(urllib.request.urlretrieve(self.__forgeURL, "forgeinstall.jar"))
        subprocess.call(['java', '-jar', 'forgeinstall.jar'])
        self.removeFile("forgeinstall.jar")
        self.removeFile("forgeinstall.jar.log")
        callback()


    def installMods(self, callback):
        print(urllib.request.urlretrieve("https://intercraftmc.com/repository/modpack.zip", "modpack.zip"))
        zipFile = zipfile.ZipFile("modpack.zip", 'r')
        zipFile.extractall(os.path.join(self.__MCpath, "InterCraft"))
        zipFile.close()
        self.removeFile("modpack.zip")
        callback()


    def installJson(self):
        files = open(os.path.join(self.__MCpath, 'launcher_profiles.json'))
        launcherProfiles = json.load(files)
        for key in list(launcherProfiles['profiles'].keys()):
            try:
                if launcherProfiles['profiles'][key]['name'] == "InterCraft":
                    del launcherProfiles['profiles'][key]
                    break
            except KeyError as e:
                pass
        launcherProfiles['profiles'][self.generateProfileKey()] = {
            "name": "InterCraft",
            "type": "custom",
            "created": datetime.datetime.now().isoformat()[:-3]+'Z',
            "lastUsed": datetime.datetime.now().isoformat()[:-3]+'Z',
            "icon": "Redstone_Ore",
            "lastVersionId": self.__lastVersionID,
            "gameDir": os.path.join(self.__MCpath, "InterCraft"),
            "javaArgs": "-Xmx2G -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -XX:-UseAdaptiveSizePolicy -Xmn128M"
        }
        files.close()

        saveFile = open(os.path.join(self.__MCpath, 'launcher_profiles.json'), 'w')
        json.dump(launcherProfiles, saveFile, indent = 4)
        saveFile.close()
