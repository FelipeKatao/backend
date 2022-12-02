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
