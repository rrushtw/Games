# from FolderName.FileName import ClassName
import sys
import unittest


class StringToInteger:
    def __init__(self) -> None:
        pass
    # end def

    def myAtio(self, s: str) -> int:
        # trim spaces
        s = s.strip()

        isPositive = True

        if s.startswith('-') or s.startswith('+'):
            isPositive = s[0] == '+'
            s = s[1:]  # trim the first negative character

        s = s.lstrip('0')  # trim zero

        tempString = ''

        for c in s:
            if not c.isdigit():
                break

            tempString += c
        # end loop

        if tempString == '':
            return 0
        else:
            # giving negative char if is negative
            tempString = tempString if isPositive else '-' + tempString

        upperLimit = 2147483647
        lowerLimit = -2147483648

        try:
            intResult = int(tempString)

            if intResult > upperLimit:
                return upperLimit
            if intResult < lowerLimit:
                return lowerLimit

            return int(tempString)
        except ValueError:
            return upperLimit if isPositive else lowerLimit
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = StringToInteger()

        self.__upperLimit = 2147483647
        self.__lowerLimit = -2147483648
    # end def

    def test_case1(self):
        '''test case1: normal positive'''
        # arrange
        input = '2147483646  '

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = 2147483646
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2: spaces and negative'''
        # arrange
        input = '  -2147483646'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = -2147483646
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3: number with characters'''
        # arrange
        input = '4193 with words'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = 4193
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4: double minus char'''
        # arrange
        input = '--1'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5: just upper limit'''
        # arrange
        input = str(self.__upperLimit)

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = self.__upperLimit
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6: just lower limit'''
        # arrange
        input = str(self.__lowerLimit)

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = self.__lowerLimit
        self.assertEqual(expect, result)
    # end def

    def test_case7(self):
        '''test case7: characters then numbers'''
        # arrange
        input = 'words and 987'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case8(self):
        '''test case8: bigger than upper limit'''
        # arrange
        input = '2147483648'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = 2147483647
        self.assertEqual(expect, result)
    # end def

    def test_case9(self):
        '''test case9: smaller than lower limit'''
        # arrange
        input = '-2147483649'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = -2147483648
        self.assertEqual(expect, result)
    # end def

    def test_case10(self):
        '''test case10: a character between numbers'''
        # arrange
        input = '1095502006p8'

        # act
        result = self.__solution.myAtio(input)

        # assert
        expect = 1095502006
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
