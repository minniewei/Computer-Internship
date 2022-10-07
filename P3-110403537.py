"""
Practice 3
Name:楊薇蓉
Student Number:110403537
Course: 2022-CE1003-A
"""
def CreatePyramid(totalNumber):
    pathOut = 'output.txt'
    fo = open(pathOut, 'w')
    nowNumber = 1
    for i in range(0,totalNumber):
        for k in range(totalNumber - i -1, 0, -1):
            fo.write(" ")
        for j in range(2*i+1):
            fo.write("*")
        if(i != totalNumber -1):
            fo.write("\n")
    fo.close()

path = 'input.txt'
f = open(path, 'r')
CreatePyramid(int(f.read()))
f.close()  