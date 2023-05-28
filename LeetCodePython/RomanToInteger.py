# from FolderName.FileName import ClassName
import unittest


class RomanToInteger:
    def __init__(self) -> None:
        pass
    # end def

    def romanToInt(self, s: str) -> int:
        result = 0
        skipFlag = False

        for i in range(len(s)):
            if skipFlag:
                skipFlag = False
                continue

            if s[i:].startswith('CM'):
                result += 900
                skipFlag = True
                continue

            if s[i] == 'M':
                result += 1000
                continue

            if s[i:].startswith('CD'):
                result += 400
                skipFlag = True
                continue

            if s[i] == 'D':
                result += 500
                continue

            if s[i:].startswith('XC'):
                result += 90
                skipFlag = True
                continue

            if s[i] == 'C':
                result += 100
                continue

            if s[i:].startswith('XL'):
                result += 40
                skipFlag = True
                continue

            if s[i] == 'L':
                result += 50
                continue

            if s[i:].startswith('IX'):
                result += 9
                skipFlag = True
                continue

            if s[i] == 'X':
                result += 10
                continue

            if s[i:].startswith('IV'):
                result += 4
                skipFlag = True
                continue

            if s[i] == 'V':
                result += 5
                continue

            if s[i] == 'I':
                result += 1
                continue
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RomanToInteger()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        input = 'III'

        # act
        result = self.__solution.romanToInt(input)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        input = 'XLIV'

        # act
        result = self.__solution.romanToInt(input)

        # assert
        expect = 44
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        input = 'MCMXCIV'

        # act
        result = self.__solution.romanToInt(input)

        # assert
        expect = 1994
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        input = 'MMMCMXCIX'

        # act
        result = self.__solution.romanToInt(input)

        # assert
        expect = 3999
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
