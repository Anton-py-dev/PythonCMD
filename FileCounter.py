import os
import platform
import time


class FileCounter:
    def __init__(self, startPath="C:\\"):
        self.startPath = startPath
        self.currDir = startPath

    def osInfo(self):
        return platform.uname()

    def dirTravel(self, name):
        return os.walk(name, topdown=True)

    def printCurrDir(self):
        print(self.currDir, '>', end=" ")

    def ls(self):
        print("\n\tDirectory of", self.currDir, end='\n\n')
        for file in os.listdir(self.currDir):
            filepath = os.path.join(self.currDir, file)
            print(time.ctime(os.path.getctime(filepath)), '\t',
                  str(round(os.path.getsize(filepath) / 1024, 2)) + " KB" if os.path.isfile(filepath) else "<DIR>",
                  '\t',
                  file)

    def mkdir(self, name):
        try:
            os.mkdir(path=os.path.join(self.currDir, name))
        except FileExistsError:
            print("Cannot create a file when that file already exists!")

    def cd(self, name):
        try:
            self.currDir = os.path.join(self.currDir, name)
        except:
            print("Incorrect directory(")

    def delete(self, name):
        pathname = os.path.join(self.currDir, name)
        try:
            os.rmdir(pathname) if os.path.isdir else os.remove(pathname)
        except FileNotFoundError:
            print("The system cannot find the file specified: ", pathname)
