import os
import platform
import json

class myrentry() :

    def __init__(self) :

        self.OS = platform.system()
        if self.OS == "Windows" : # For Windows

            self.Sep = '\\' # Separator

        elif self.OS == "Linux" : # For Linux

            self.Sep = '/' # Separator


    def DictDataMaker(self,ListString) :

        Count = []
        Delim = []
        Size = []
        Heada = []
        Flag = False
        Cook = []
        DicCook = {}
        for i,String in enumerate(ListString) :
            Count.append(String.count("|"))
            Listim = String.split("|")
            Logical = []
            for Elem in Listim:
                if '-' in Elem :         
                    Logical.append(True)
                else :
                    Logical.append(False)
            Check = all(Logical)
            if Check is True:
                Delim.append(i)
                Size.append(Count[-1])
                if Count[-2] == Count[-1] :
                    Heada.append(i-1)
                Flag = True

            if Flag == True :
                if Count[-1] == Size[-1] :
                    Flag = True
                else :
                    Flag = False
                    DicCook["Cook{0}".format(len(Size)-1)] = Cook
                    Cook = []

            if Flag == True :
                Cook.append(i)

        # So,
        for i,h in enumerate(Heada) :
            DicCook["Cook"+str(i)][0] = h

        # Then
        FullData = []
        for i,goo in enumerate(DicCook) :
            Dicti = {}
            for j,foo in enumerate(DicCook[goo]) :
                if j == 0 :
                    Dicti["Headers"] = ListString[foo].split("|")
                else :
                    Dicti["r"+str(j)] = ListString[foo].split("|")
            
            FullData.append(Dicti)

        return(FullData)
    

    def CreateRentry(self,LinkName,PW,Path,StartText='This page was created with rentrylab.'):
        file = open(Path + self.Sep + "Create.sh",'w')
        file.write("rentry new -p " + PW + " -u https://rentry.co/" + LinkName + " " + '"' + StartText + '"')
        file.close()
        
        try :
            os.system("bash " + Path + self.Sep + "Create.sh")
        except :
            print("ٔError: Not Created")

        os.remove(Path + self.Sep + "Create.sh") 
    
    
    def GetFromRentry(self,MyLink,Path,FileName,Lang,ext) :
        
        file = open(Path+self.Sep+"Get.sh",'w')
        file.write("rentry raw -u " +  MyLink + " > " + '"' + Path + self.Sep +'Temp.txt"')
        file.close()
        os.system("bash " + Path + self.Sep + "Get.sh")

        os.remove(Path + self.Sep + "Get.sh")

        with open(Path+self.Sep+"Temp.txt") as f:
            ScriptList = f.read().splitlines()
        f.close()

        ScriptList = [s for s in ScriptList if s != '']
       
        StartIndex=[idx for idx,item in enumerate(ScriptList) if item == '``` '+Lang.lower()]
        # print(StartIndex[0]+1)
        EndIndex=[idx for idx,item in enumerate(ScriptList) if item == '```']
        # print(EndIndex[0]-1)

        SharedCodes = []
        for i,Sta in enumerate(StartIndex):
            # SharedCodes.append(["# Part "+str(i+1)])
            SharedCodes.append(ScriptList[Sta+1:EndIndex[i]])

        file = open(Path + self.Sep + FileName + ext,'w')
        for ie , Lista in enumerate(SharedCodes) :
            for I,Text in enumerate(Lista):
                file.write(Text+'\n')
            file.write('\n')
            file.write('\n')
        file.close()
     
        os.remove(Path + self.Sep + "Temp.txt")


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


    def GetDataFromRentry(self,MyLink,Path,*args) :
        try :
            file = open(Path+self.Sep+"GetData.sh",'w')
            file.write("rentry raw -u " +  MyLink + " > " + '"' + Path + self.Sep +'Temp.txt"')
            file.close()
            os.system("bash " + Path + self.Sep + "GetData.sh")

            os.remove(Path + self.Sep + "GetData.sh")

            with open(Path+self.Sep+"Temp.txt") as f:
                ScriptList = f.read().splitlines()
            f.close()

            os.remove(Path + self.Sep + "Temp.txt")

            ScriptList = [s for s in ScriptList if s != '']

            Dictlist = self.DictDataMaker(ScriptList)

            if len(args) == 0 :
                return Dictlist
            elif len(args) != 0 and list(args)[0].lower() == 'json'  :
                with open(Path + self.Sep + "GottenData.json", "w") as Vari:
                    json.dump(Dictlist, Vari,indent=4)
        
        except Exception as e:
            print(e)



    def SendDataToRentry(self,MyLink,PW,Path,Dict,HeaderList=['# Data1']):
        HeaderList.reverse()

        ScriptList = []
        for (i,Head) in enumerate(HeaderList) :
            ScriptList.insert(0, Head)
        

        for i,Elem in enumerate(Dict) :

            Row = list(Dict.keys())[i]
            String = '|'.join(map(str, Dict[Row]))
            ScriptList.append(String)
            if i == 0 : # Header
                Delim = '{}'.format('|'.join('-' for _ in range(len(Dict[Row]))))
                ScriptList.append(Delim)
            else :
                pass
        ScriptList.append('\n'+'***')


        file = open(Path + self.Sep + "Temp.txt",'w')
        for I,Text in enumerate(ScriptList):
            file.write(Text+'\n')
        file.close()

        file = open(Path+self.Sep+"SetData.sh",'w')
        if self.OS == "Windows" :
            Path_ = Path.replace('\\','/')
            file.write("cat " + Path_ + "/" + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
        elif self.OS == 'Linux' :
            file.write("cat " + Path + self.Sep  + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
        file.close()

        os.system("bash " + Path + self.Sep + "SetData.sh")

        os.remove(Path + self.Sep + "SetData.sh")    
        os.remove(Path + self.Sep + "Temp.txt")

  
    def AppendToRentry(self,MyLink,PW,Path,FileName,Lang,ext,Loc,HeaderList=['# Append With RentryLab']):
        
        file = open(Path+self.Sep+"GetToAppend.sh",'w')
        file.write("rentry raw -u " +  MyLink + " > " + '"' + Path + self.Sep +'Temp.txt"')
        file.close()
        os.system("bash " + Path + self.Sep + "GetToAppend.sh")

        os.remove(Path + self.Sep + "GetToAppend.sh")

        with open(Path+self.Sep+"Temp.txt") as f:
            ScriptList = f.read().splitlines()
        f.close()

        ScriptList = [s for s in ScriptList if s != '']

        HeaderList.reverse()

        with open(Path + self.Sep + FileName + ext) as f:
            ScriptList1 = f.read().splitlines()
        f.close()

        ScriptList1 = ScriptList1[0:len(ScriptList1)-2]

        ScriptList1.insert(0, '``` '+Lang.lower())
        ScriptList1.append('```')

        for (i,Head) in enumerate(HeaderList) :
            ScriptList1.insert(0, Head)
        
        if Loc.lower() == 'down':
            GeneList = ScriptList + ScriptList1
        elif Loc.lower() == 'top':
            GeneList = ScriptList1 + ScriptList
        
        file = open(Path + self.Sep + "Temp.txt",'w')
        for I,Text in enumerate(GeneList):
            file.write(Text+'\n')
        file.close()

        file = open(Path+self.Sep+"SetToAppend.sh",'w')
        if self.OS == "Windows" :
            Path_ = Path.replace('\\','/')
            file.write("cat " + Path_ + "/" + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
        elif self.OS == 'Linux' :
            file.write("cat " + Path + self.Sep  + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
        file.close()

        os.system("bash " + Path + self.Sep + "SetToAppend.sh")

        os.remove(Path + self.Sep + "SetToAppend.sh")    
        os.remove(Path + self.Sep + "Temp.txt")



    def AppendDataToRenty(self,MyLink,PW,Path,Dict,Loc,HeaderList=['# Data Append']):
        try :
            file = open(Path+self.Sep+"GetDataAppend.sh",'w')
            file.write("rentry raw -u " +  MyLink + " > " + '"' + Path + self.Sep +'Temp.txt"')
            file.close()
            os.system("bash " + Path + self.Sep + "GetDataAppend.sh")

            os.remove(Path + self.Sep + "GetDataAppend.sh")

            with open(Path+self.Sep+"Temp.txt") as f:
                ScriptList = f.read().splitlines()
            f.close()

            ScriptList = [s for s in ScriptList if s != '']

            U = tuple(ScriptList)
            P = list(U)
            r = 0
            for i,Elem in enumerate(U) :
                if Elem == '***' :
                    P[i+r:i+r] = ['\n']
                    r += 1
            
            ScriptList = P

            HeaderList.reverse()

            ScriptList1 = []
            for (i,Head) in enumerate(HeaderList) :
                ScriptList1.insert(0, Head)
            
            for i,Elem in enumerate(Dict) :

                Row = list(Dict.keys())[i]
                String = '|'.join(map(str, Dict[Row]))
                ScriptList1.append(String)
                if i == 0 : # Header
                    Delim = '{}'.format('|'.join('-' for _ in range(len(Dict[Row]))))
                    ScriptList1.append(Delim)
                else :
                    pass
            
            ScriptList1.append('\n'+'***')
            
            if Loc.lower() == 'down':
                GeneList = ScriptList + ScriptList1
            elif Loc.lower() == 'top':
                GeneList = ScriptList1 + ScriptList


            file = open(Path + self.Sep + "Temp.txt",'w')
            for I,Text in enumerate(GeneList):
                file.write(Text+'\n')
            file.write('\n')
            file.close()

            file = open(Path+self.Sep+"SetDataAppend.sh",'w')
            if self.OS == "Windows" :
                Path_ = Path.replace('\\','/')
                file.write("cat " + Path_ + "/" + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
            elif self.OS == 'Linux' :
                file.write("cat " + Path + self.Sep  + "Temp.txt" + " | rentry edit -p " + PW + " -u " + MyLink)
            file.close()

            os.system("bash " + Path + self.Sep + "SetDataAppend.sh")

            os.remove(Path + self.Sep + "SetDataAppend.sh")    
            os.remove(Path + self.Sep + "Temp.txt")

        except Exception as e:
            print(e)


################### 

