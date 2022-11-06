import math

while True:
    print("\n Choose the math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n9 - Sine\n10 - Cosine\n11 - Tangent\n")

    oper = input("\nYour option from the menu: ")

    #Addition
    if oper == "0":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Subtraction
    elif oper == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Multiplication
    elif oper == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Division
    elif oper == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        if val2 == 0:
            print("\n You can't divide by 0")
            val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Modulo
    elif oper == "4":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Raising to a power
    elif oper == "5":
        val1 = float(input("\nEnter the base: "))
        val2 = float(input("\nEnter the power: "))

        print("\nThe result is: " + str(math.pow(val1,val2)) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Square root
    elif oper == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Logarithm
    elif oper == "7":
        val1 = float(input("\nEnter the value for calculation the logarithm to base two: "))

        print("\nThe result is: " + str(math.log(val1, 2)) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Sine
    elif oper == "8":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break

    #Tangent
    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")
        back = input("\nGo back to the main menu? (y/n)")

        if back == 'y':
            continue
        else:
            break
