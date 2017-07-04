import datetime
import json
import os
import random
import subprocess
import sys
import urllib.request
import zipfile

import utils


class InstallLib():

    FORGE_URL = 'https://intercraftmc.com/repository/forge/'
    FORGE_NAME = 'forge.jar'

    MODPACK_URL = 'https://intercraftmc.com/repository/modpack.zip'
    MODPACK_NAME = 'modpack.zip'

    REPO_URL = 'https://intercraftmc.com/repository/intercraft.json'


    def __init__(self):
        self.__mcPath = utils.minecraftPath()

        infoJson = urllib.request.urlopen(InstallLib.REPO_URL)
        self.__info = json.loads(infoJson.read().decode())

        self.__lastVersionID = self.__info['forge']['name']
        self.__forgeURL = InstallLib.FORGE_URL + self.__info['forge']['file']        


    def clean(self):

        utils.removeFile(utils.tempPath(InstallLib.FORGE_NAME))
        utils.removeFile(InstallLib.FORGE_NAME + ".log")
        utils.removeFile(utils.tempPath(InstallLib.MODPACK_NAME))


    def getMcPath(self):
        return self.__mcPath


    def setMcPath(self, path):
        self.__mcPath = path


    def generateProfileKey(self):
        chars = '0123456789abcdef'
        result = ''
        for i in range(32):
            result += chars[random.randint(0, 15)]
        return result


    def installForge(self, callback):
        print(urllib.request.urlretrieve(self.__forgeURL, utils.tempPath(InstallLib.FORGE_NAME)))
        try:
            subprocess.check_output(['java', '-jar', utils.tempPath(InstallLib.FORGE_NAME)])
        except Exception as e:
            print("Failed to install Forge\n", e)
            return callback(False, 'forge', 'Failed to install Forge, check your Java installation')
        callback(True)


    def installMods(self, callback):
        try:
            print(urllib.request.urlretrieve(InstallLib.MODPACK_URL, utils.tempPath(InstallLib.MODPACK_NAME)))
            zipFile = zipfile.ZipFile(utils.tempPath(InstallLib.MODPACK_NAME), 'r')
            zipFile.extractall(os.path.join(self.__mcPath, "InterCraft"))
            zipFile.close()
        except Exception as e:
            print("Failed to install modpack\n", e)
            return callback(False, 'mods', 'Failed to install modpack')
        callback(True)


    def installJson(self, callback):

        try:
            files = open(os.path.join(self.__mcPath, 'launcher_profiles.json'))
            launcherProfiles = json.load(files)
            files.close()
        except Exception as e:
            print("Failed to open launcher_profiles.json\n", e)
            return callback(False, 'launcher', 'Failed to open Minecraft launcher profiles')

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
            "gameDir": os.path.join(self.__mcPath, "InterCraft"),
            "javaArgs": "-Xmx3G -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -XX:-UseAdaptiveSizePolicy -Xmn128M"
        }

        print("Adding 'InterCraft' launcher profile...")

        try:
            saveFile = open(os.path.join(self.__mcPath, 'launcher_profiles.json'), 'w')
            json.dump(launcherProfiles, saveFile, indent=4)
            saveFile.close()
        except Exception as e:
            print("Failed installing launcher profile\n", e)
            return callback(False, 'launcher', 'Failed to save Minecraft launcher profiles')

        callback(True)
