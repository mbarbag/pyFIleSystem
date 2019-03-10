import os, shutil
def list(src):
    return os.listdir(src)

def removeFile(src):
    return os.remove(src)

def removeDirs(src):
    return os.removedirs(src)

def createFile(src):
    file = open(src, "w+")
    return file.close()

def createDirs(src):
    return os.makedirs(src)

#Renombra directorios y archivos
def rename(src, dst):
    return os.rename(src,dst)

def cut(src, dst):
    return os.rename(src,dst)
    
def copy(src, dst):
    return shutil.copy(src,dst)

copy("/home/augusto/Desktop/augusManu.txt", "/home/augusto/Desktop/CopiaaugusManu.txt")
print(list('/home/augusto/Desktop'))