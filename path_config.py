import os
from os import path

def CreateFolder(NameProject,ProjAdd):
    if path.exists(NameProject) == False and ProjAdd == False:
        os.mkdir(NameProject)
        print("Pasta criada com suceso")
        return True
    else:
        if ProjAdd == True:
            if path.exists(NameProject) == True:
                return True
        print("Pasta já existe, escolha outro nome")
        return False