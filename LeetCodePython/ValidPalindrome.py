# from FolderName.FileName import ClassName
import unittest


class ValidPalindrome:
    def __init__(self) -> None:
        pass
    # end def

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left: int = 0
        right: int = len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            # else:
            left += 1
            right -= 1
        # end loop

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = ValidPalindrome()
    # end def

    def test_case1(self):
        '''test case 1'''
        # arrange
        s = "A man, a plan, a canal: Panama"

        # act
        result = self.__solution.isPalindrome(s)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case 2'''
        # arrange
        s = "race a car"

        # act
        result = self.__solution.isPalindrome(s)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case 3'''
        # arrange
        s = "121"

        # act
        result = self.__solution.isPalindrome(s)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case 4'''
        # arrange
        s = "121a"

        # act
        result = self.__solution.isPalindrome(s)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case 5'''
        # arrange
        s = "121@"

        # act
        result = self.__solution.isPalindrome(s)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
