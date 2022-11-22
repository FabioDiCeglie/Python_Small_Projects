import math
import pandas

#Defining the function with 3 parameters
def calculator(excel_path, price_index):
    #Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel(excel_path)

    #The value of x
    x = float(df["Price"][price_index])

    #The value of y
    y = float(input("Enter the value of y: "))

    #The final result
    result = round(math.pow(x / y, 2))

    #Returning the result
    return result


#End of program
