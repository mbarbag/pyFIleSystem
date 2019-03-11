import os, shutil, stat
def list(src):
    return os.listdir(src)

def removeFile(src):
    return os.remove(src)

def removeDir(src):
    return os.rmdir(src)

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

def chmod(src, mode):
    """ 1. Read by owner
    2. Write by owner
    3. Execute by owner
    4. Read, Write and Execute by owner
    5. Read by group
    6. Write by group
    7. Execute by group
    8. Read, Write and Execute by group
    9. Read by others
    10. Write by others
    11. Execute by others
    12. Read, Write and Execute by others"""
    if(mode == "1"):
        return os.chmod(src,stat.S_IRUSR)
    elif(mode == "2"):
        return os.chmod(src,stat.S_IWUSR)
    elif(mode == "3"):
        return os.chmod(src,stat.S_IXUSR)
    elif(mode == "4"):
        return os.chmod(src,stat.S_IRWXU)
    elif(mode == "5"):
        return os.chmod(src,stat.S_IRGRP)
    elif(mode == "6"):
        return os.chmod(src,stat.S_IWGRP)
    elif(mode == "7"):
        return os.chmod(src,stat.S_IXGRP)
    elif(mode == "8"):
        return os.chmod(src,stat.S_IRWXG)
    elif(mode == "9"):
        return os.chmod(src,stat.S_IROTH)
    elif(mode == "10"):
        return os.chmod(src,stat.S_IWOTH)
    elif(mode == "11"):
        return os.chmod(src,stat.S_IXOTH)
    elif(mode == "12"):
        return os.chmod(src,stat.S_IRWXO)
