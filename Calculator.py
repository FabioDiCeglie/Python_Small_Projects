import math

while True:
    print("\n Choose the math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 -Square root\n7 - Logarithm\n9 - Sine\n10 - Cosine\n11 - Tangent\n")

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
