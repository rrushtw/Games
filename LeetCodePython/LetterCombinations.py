# from FolderName.FileName import ClassName
import unittest


class LetterCombinations:
    def __init__(self) -> None:
        self.__numberToAlpha = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    # end def

    def letterCombinations(self, digits: str) -> list[str]:
        result: list[str] = []

        if len(digits) == 0:
            return result

        if len(digits) == 1:
            return self.__numberToAlpha[digits]

        # len(digits) > 1
        tempResult = self.letterCombinations(digits[1:])

        for i in self.__numberToAlpha[digits[0]]:
            for j in tempResult:
                result.append(i + j)
            # end loop
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = LetterCombinations()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        digits = "23"

        # act
        result = self.__solution.letterCombinations(digits)

        # assert
        expect = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        digits = ""

        # act
        result = self.__solution.letterCombinations(digits)

        # assert
        expect = []
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        digits = "2"

        # act
        result = self.__solution.letterCombinations(digits)

        # assert
        expect = ["a", "b", "c"]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
