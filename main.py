import greeting
import calculation
import reverse
import validation
import conversion
import deleteNumber
import value

greeting.Start()
loop=True
while loop==True:
    a=False
    while a==False:
        firstNumber,secondNumber=value.Input()
        b=True
        while b==True:
            if firstNumber+secondNumber>255: #checking if the sum is 9-bit or not 
                print("The binary sum of entered number will be more than 8-bits!! Please enter values again!")
                firstNumber,secondNumber=value.Input()
            elif firstNumber+secondNumber==0: 
                print("The sum of two given number is zero!! Please enter another values!")
                firstNumber,secondNumber=value.Input()
            else:
                break
        break

    #converting decimal number into binary        
    num1=conversion.DecimalToBinary(firstNumber) 
    num2=conversion.DecimalToBinary(secondNumber)

    #reversing binary number
    num3=reverse.Reverse(num1)
    num4=reverse.Reverse(num2)

    #adding two reversed binary number        
    addition=calculation.Addition(num3,num4)
    sum1=deleteNumber.DeleteNumber(addition)
    sum2=conversion.StringConversion(sum1)
    
    print("\n")
    print("Binary number of first decimal number (",firstNumber,") is: ",num3)
    print("Binary number of second decimal number (",secondNumber,") is: ",num4)
    print("\n")
    print("Sum of binary number is: ",sum2)
    print("\n")

    continueLoop=input("Do you want to continue this application?? (Yes/No) ").upper()
    if continueLoop=="NO": 
        break
greeting.End()

