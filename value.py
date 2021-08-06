import validation

def Input():
    a=False
    while a==False:
        try:
            print("\n")
            firstNumber=int(input("Enter first decimal number: "))
            firstNumber=validation.ValidationFirst(firstNumber)
            a=True
        except:
            print("Invalid Input!! Please enter an integer")
    b=False
    while b==False:
        try:
            secondNumber=int(input("Enter second decimal number: "))
            secondNumber=validation.ValidationSecond(secondNumber)
            b=True
        except:
            print("Invalid Input!! Please enter an integer")

    return firstNumber,secondNumber
