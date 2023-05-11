import os
import platform


class myrentry() :
    def __init__(self) :
        self.OS = platform.system()
        if self.OS == "Windows" : # For Windows

            self.Sep = '\\' # Separator

        elif self.OS == "Linux" : # For Linux

            self.Sep = '/' # Separator
    
    
    def GetFromRentry(self,MyLink,Path,FileName,Lang,ext) :
        
        file = open(Path+self.Sep+"Get.sh",'w')
        file.write("rentry raw -u " +  MyLink + " > " + '"' + Path + self.Sep +'Temp.txt"')
        file.close()
        os.system("bash " + Path + self.Sep + "Get.sh")

        os.remove(Path + self.Sep + "Get.sh")

        with open(Path+self.Sep+"Temp.txt") as f:
            ScriptList = f.read().splitlines()
        f.close()
            
        StartIndex=[idx for idx,item in enumerate(ScriptList) if item == '``` '+Lang.lower()]
        # print(StartIndex[0]+1)
        EndIndex=[idx for idx,item in enumerate(ScriptList) if item == '```']
        # print(EndIndex[0]-1)

        SharedCodes = ScriptList[StartIndex[0]+1:EndIndex[0]]

        file = open(Path + self.Sep + FileName + ext,'w')
        for I,Text in enumerate(SharedCodes):
            file.write(SharedCodes[I]+'\n')
        file.close()
            
        os.remove(Path + self.Sep + "Temp.txt")
            
        return SharedCodes

    def SendToRentry(self,MyLink,PW,Path,FileName,Lang,ext,HeaderList=['# Your Header']) :
        HeaderList.reverse()

        with open(Path + self.Sep + FileName + ext) as f:
            ScriptList = f.read().splitlines()
        f.close()

        ScriptList = ScriptList[0:len(ScriptList)-2]

        ScriptList.insert(0, '``` '+Lang.lower())
        ScriptList.append('```')

        for (i,Head) in enumerate(HeaderList) :
            ScriptList.insert(0, Head)

        file = open(Path + self.Sep + "Temp.txt",'w')
        for I,Text in enumerate(ScriptList):
            file.write(Text+'\n')
        file.close()

        file = open(Path+self.Sep+"Set.sh",'w')
        if self.OS == "Windows" :
            Path_ = Path.replace('\\','/')
            file.write("cat " + Path_ + "/" + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
        elif self.OS == 'Linux' :
            file.write("cat " + Path + self.Sep  + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
        file.close()

        os.system("bash " + Path + self.Sep + "Set.sh")

        os.remove(Path + self.Sep + "Set.sh")    
        os.remove(Path + self.Sep + "Temp.txt")    


