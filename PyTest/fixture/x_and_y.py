#A software test fixture sets up the system for the testing process by providing it with all the necessary code to initialize it, thereby satisfying whatever preconditions there may be.
#(source: https://en.wikipedia.org/wiki/Test_fixture#Software)

import pandas
import pytest
import math
from unittest import mock

#Defining the function with 3 parameters
@pytest.fixture
def xyfunc():
    #Loading the Excel
    df = pandas.read_excel("../testing_calculator/values.xlsx")

    #The value of x
    x = float(df["Price"][0])

    #The value of y
    with mock.patch('builtins.input', return_value = 10):
        y = float(input("Enter the value of y: "))

    return math.pow(x / y, 2)

def test_result(xyfunc):
    result = round(xyfunc)
    assert result == 894
