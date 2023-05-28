# from FolderName.FileName import ClassName
import unittest


class LengthOfLastWord:
    def __init__(self) -> None:
        pass
    # end def

    def lengthOfLastWord(self, s: str) -> int:
        count: int = 0

        i = len(s) - 1
        while i >= 0:
            if count == 0 and s[i] == ' ':
                i -= 1
                continue

            if count > 0 and s[i] == ' ':
                break

            if s[i] != ' ':
                count += 1

            i -= 1
        # end loop

        return count
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = LengthOfLastWord()
    # end def

    def test_case1(self):
        '''test case 1'''
        # arrange
        s = "Hello World"

        # act
        result = self.__solution.lengthOfLastWord(s)

        # assert
        expect = 5
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case 2'''
        # arrange
        s = "   fly me   to   the moon  "

        # act
        result = self.__solution.lengthOfLastWord(s)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case 3'''
        # arrange
        s = "luffy is still joyboy"

        # act
        result = self.__solution.lengthOfLastWord(s)

        # assert
        expect = 6
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
