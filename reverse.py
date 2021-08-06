def Reverse(numList):
    binaryNumber=[]
    for i in range(len(numList)-1,-1,-1):
        binaryNumber.append(numList[i])
    return binaryNumber
