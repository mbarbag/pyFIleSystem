import os
def list(source):
    return os.listdir(source)

def removeFile(source):
    return os.remove(source)

def removeDirs(source):
    return os.removedirs(source)

def createFile(file_name):
    file = open(file_name, "w+")
    return file.close()

def createDirs(source):
    return os.makedirs(source)


print(list('/home/user'))