def ValidationFirst(number):
    while number<0 or number>255:
        print("Invalid Input!! Please input number from 0 to 255")
        number=int(input("Please reenter first decimal number: "))
    return number

def ValidationSecond(number):
    while number<0 or number>255:
        print("Invalid Input!! Please input number from 0 to 255")
        number=int(input("Please reenter second decimal number: "))
    return number
