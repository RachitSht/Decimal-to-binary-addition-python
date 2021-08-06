def DecimalToBinary(decimalNumber):
    c=[]
    d=0
    while d!=8:
        remainder=decimalNumber%2
        c.append(remainder)
        decimalNumber=decimalNumber//2
        d=d+1
    return c

def StringConversion(a):
    #converting the list into string
    binaryNumber = ""

    for i in range(len(a)) :
        binaryNumber = binaryNumber + str(a[i])
        
    return binaryNumber
