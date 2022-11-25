from os import path
import os.path
        
def main():
    obj = input('Digite seu comando: ')
    print(obj)
    if obj == "createProj":
        nameProj = input("Digite o nome do seu projeto: ")
        if CreateFolder(nameProj,False) == True:
            nameFile = input("Digite o nome do arquivo: ")
            nameFileCreate = input("Digite o nome do novo arquivo: ")
            CreateFile(nameFileCreate,nameProj,nameFile)
    if obj == "addNewFile":
        nameProj = input("Digite o nome do seu projeto: ")
        if CreateFolder(nameProj,True) == True:
            nameFile_add = input("Digite o nome do arquivo: ")
            nameFileCreate_add = input("Digite o nome do novo arquivo: ")
            CreateFile(nameFileCreate_add,nameProj,nameFile_add)
         
    if obj != "stop":
        main()
    
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

def CreateFile(nameFile,Nameproj,NameBase):
    file = open(NameBase,'r')
    contentfile = []
    for lineFile in file.readlines():
        contentfile.append(lineFile)
    file.close()
    fileProj = open(Nameproj+'/'+nameFile,'w')
    fileProj.write("<html><head><title>"+Nameproj+"</title><head><body>")
    fileProj.write("<h1>"+Nameproj+"</h1>")
    for newfile in contentfile:
        fileProj.write(newfile)
    fileProj.write("</body>")
    fileProj.write("</html>")

main()