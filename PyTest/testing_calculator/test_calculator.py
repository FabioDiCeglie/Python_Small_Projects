#These tests are meant for checking the results of performing the calculations using each value in the DataFrame ("Price" column) and the same y value (10)
import sys
import pytest
from unittest import mock
from calculator import calculator

#Marking test functions
class TestClass(object):
    @pytest.mark.skip(reason = "Skipping test with index 0")
    def test_index0(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 0) == 894

    @pytest.mark.skipif(sys.version_info >= (3,7,2), reason = "Requires Python 3.7.2 or lower")
    def test_index1(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 1) == 3648

    @pytest.mark.skipif(sys.platform == 'win32', reason = "Test designed for non-Windows platforms")
    def test_index2(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 2) == 207

    # @pytest.mark.skipif(sys.getwindowsversion().build >= 16299, reason = "Test designed for Windows builds below 16299")
    # def test_index3(self):
    #     with mock.patch('builtins.input', return_value = 10):
    #         assert calculator("./values.xlsx", 3) == 497

    def test_index4(self):
        need = pytest.importorskip("Django")
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 4) == 2025

    @pytest.mark.xfail(reason = "Expected fail", raises = AssertionError)
    def test_index5(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("./values.xlsx", 4) == 100000

#run with: pytest -vrs --disable-warning test_calculation.py
