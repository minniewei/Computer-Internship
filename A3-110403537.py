def CreatePyramid(totalNumber):
    pathOut = 'output.txt'
    fo = open(pathOut, 'w')
    nowNumber = 1
    for i in range(0,totalNumber):
        for k in range(totalNumber - i -1, 0, -1):
            fo.write(" ")
        for j in range(2*i+1):
            if nowNumber ==1:
                fo.write("1")
            elif isPrime(nowNumber)==True:
                fo.write("Y")
            else:
                fo.write("N")
            nowNumber+=1
        fo.write("\n")
    fo.close()

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True  

path = 'input.txt'
f = open(path, 'r')
CreatePyramid(int(f.read()))
f.close()  