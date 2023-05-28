# from FolderName.FileName import ClassName
import unittest


class PalindromeNumber:
    def __init__(self) -> None:
        pass
    # end def

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        stringForward = str(x)
        stringBackward = stringForward[::-1]

        return stringForward == stringBackward
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = PalindromeNumber()

        self.__upperLimit = 2147483647
        self.__lowerLimit = -2147483648
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        input = 121

        # act
        result = self.__solution.isPalindrome(input)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        input = -121

        # act
        result = self.__solution.isPalindrome(input)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        input = 10

        # act
        result = self.__solution.isPalindrome(input)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4: even length'''
        # arrange
        input = 1221

        # act
        result = self.__solution.isPalindrome(input)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5: upper limit'''
        # arrange
        input = 2147447412

        # act
        result = self.__solution.isPalindrome(input)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
