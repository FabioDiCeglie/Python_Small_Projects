#These tests are meant for checking the results of performing the calculations using each value in the DataFrame ("Price" column) and the same y value (10)
from unittest import mock
from calculator import calculator

class TestClass(object):
    def test_index0(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 0) == 894

    def test_index1(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 1) == 3648

    def test_index2(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 2) == 207

    def test_index3(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 3) == 497

    def test_index4(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 4) == 2025


