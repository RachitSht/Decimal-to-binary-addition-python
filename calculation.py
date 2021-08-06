import reverse
def AndGate(a,b):
    return a&b
def OrGate(a,b):
    return a|b
def XorGate(a,b):
    return a^b

def Addition(num1,num2):
    array1=[]
    cIn=0
    for i in range(len(num1)-1,-1,-1):
        a=int(num1[i])
        b=int(num2[i])
        sum1=XorGate(a,b)
        finalSum=XorGate(sum1,cIn)
        cOut1=AndGate(cIn,sum1)
        cOut2=AndGate(a,b)
        finalcOut=OrGate(cOut1,cOut2)
        cIn=finalcOut
        array1.append(finalSum)
        
    array2=reverse.Reverse(array1)
    return array2


            
