
from file_config import CreateFile
from path_config import CreateFolder

def CallCommands(obj):
    if obj == "createProj":
        nameProj = input("Digite o nome do seu projeto: ")
        NewProject(nameProj)
        
    if obj == "addNewFile":
        nameProj = input("Digite o nome do seu projeto: ")
        AddNewFile(nameProj)
        
         
def AddNewFile(nameProj):
    if CreateFolder(nameProj,True) == True:
            nameFile_add = input("Digite o nome do arquivo: ")
            nameFileCreate_add = input("Digite o nome do novo arquivo: ")
            CreateFile(nameFileCreate_add,nameProj,nameFile_add)

def NewProject(nameProj):
    if CreateFolder(nameProj,False) == True:
            nameFile = input("Digite o nome do arquivo: ")
            nameFileCreate = input("Digite o nome do novo arquivo: ")
            CreateFile(nameFileCreate,nameProj,nameFile)