import pandas
import pytest
import math
from unittest import mock

#Defining the function with 3 parameters
@pytest.fixture(scope = "module", params = [0, 1, 2, 3, 4])
def xyfunc(request):
    #Loading the Excel (D:\\testing\\values.xlsx) values into a Pandas DataFrame
    df = pandas.read_excel("D:\\testing\\values.xlsx")

    #The value of x
    x = float(df["Price"][request.param])

    #The value of y
    with mock.patch('builtins.input', return_value = 10):
        y = float(input("Enter the value of y: "))

    return math.pow(x / y, 2)
