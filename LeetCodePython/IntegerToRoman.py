# from FolderName.FileName import ClassName
import unittest


class IntegerToRoman:
    def __init__(self) -> None:
        pass
    # end def

    def intToRoman(self, num: int) -> str:
        if num >= 1000:
            return "M" + self.intToRoman(num - 1000)
        elif num >= 900:
            return "CM" + self.intToRoman(num - 900)
        elif num >= 500:
            return "D" + self.intToRoman(num - 500)
        elif num >= 400:
            return "CD" + self.intToRoman(num - 400)
        elif num >= 100:
            return "C" + self.intToRoman(num - 100)
        elif num >= 90:
            return "XC" + self.intToRoman(num - 90)
        elif num >= 50:
            return "L" + self.intToRoman(num - 50)
        elif num >= 40:
            return "XL" + self.intToRoman(num - 40)
        elif num >= 10:
            return "X" + self.intToRoman(num - 10)
        elif num >= 9:
            return "IX" + self.intToRoman(num - 9)
        elif num >= 5:
            return "V" + self.intToRoman(num - 5)
        elif num >= 4:
            return "IV" + self.intToRoman(num - 4)
        elif num >= 1:
            return "I" + self.intToRoman(num - 1)
        else:
            return ""
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = IntegerToRoman()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        input = 3

        # act
        result = self.__solution.intToRoman(input)

        # assert
        expect = 'III'
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        input = 58

        # act
        result = self.__solution.intToRoman(input)

        # assert
        expect = 'LVIII'
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        input = 1994

        # act
        result = self.__solution.intToRoman(input)

        # assert
        expect = 'MCMXCIV'
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        input = 3999

        # act
        result = self.__solution.intToRoman(input)

        # assert
        expect = 'MMMCMXCIX'
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
