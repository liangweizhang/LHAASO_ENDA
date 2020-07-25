import os
def readNT(FileName):
    fp=open(FileName,mode='r')
    fileData=fp.name
    line=fp.readline()
    SumNum=0;
    MAS_NUM=[0,0,0,0,0]
    while line:
        blankChar = 0
        MAS=0;
        for i in line:
            if(blankChar == 5):
                MAS=i
                break
            if (i==" "):
                blankChar+=1
        if(MAS=='0'):
            MAS_NUM[0]+=1
        elif(MAS=='1'):
             MAS_NUM[1]+=1
        elif(MAS=='3'):
            MAS_NUM[2]+=1
        elif(MAS=='5'):
            MAS_NUM[3]+=1
        elif(MAS=='7'):
            MAS_NUM[4]+=1
        SumNum+=1
        line=fp.readline()
    fp.close()
    print("事例时间:",fp.name)
    print(MAS_NUM,SumNum)
    if((SumNum-MAS_NUM[0])>0):
        print("M1事例比例： {:.2%}'".format(MAS_NUM[1]/(SumNum-MAS_NUM[0])))
        print("M3事例比例： {:.2%}'".format(MAS_NUM[2]/(SumNum-MAS_NUM[0])))
        print("M5事例比例： {:.2%}'".format(MAS_NUM[3]/(SumNum-MAS_NUM[0])))
        print("M7事例比例： {:.2%}'".format(MAS_NUM[4]/(SumNum-MAS_NUM[0])))
path=r"G:\MyPython\LHAASO_ENDA\ReadData"
for i in os.walk(path):
    path_tuple=i
for name in path_tuple[2]:
    txtpath=".\ReadData"+"\\"+name
    readNT(txtpath)
    