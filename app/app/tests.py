""" Sample test cases for the app module. """

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ Test cases for the calc module. """
    
    def test_add_numbers(self):
        """ Test that two numbers are added together. """
        res = calc.add(3, 8)
        self.assertEqual(res, 11) #self.assertEqual(res, 11) là hàm kiểm tra kết quả trả về từ hàm add() có đúng là 11 hay không

    def test_subtract_numbers(self):
        """ Test that values are subtracted and returned. """
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6) #self.assertEqual(res, 6) là hàm kiểm tra kết quả trả về từ hàm subtract() có đúng là 6 hay không