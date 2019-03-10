import os
def list(source):
    return os.listdir(source)

def removeFile(source):
    return os.remove(source)

def removeDirs(source):
    return os.removedirs(source)

def createFile(source):
    file = open(source, "w+")
    return file.close()

def createDirs(source):
    return os.makedirs(source)


createFile("/home/augusto/Desktop/manuAugus.txt")

print(list('/home/augusto/Desktop'))