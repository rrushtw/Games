# from FolderName.FileName import ClassName
import unittest


class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = ''.join(sorted(ransomNote))
        magazine = ''.join(sorted(magazine))

        index: int = None

        for char in ransomNote:
            index = magazine.find(char)

            if index == -1:
                return False

            magazine = magazine[index + 1:]
        # end loop

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = RansomNote()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        ransomNote = "a"
        magazine = "b"

        # act
        result = self.__solution.canConstruct(ransomNote, magazine)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        ransomNote = "aa"
        magazine = "ab"

        # act
        result = self.__solution.canConstruct(ransomNote, magazine)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        ransomNote = "aa"
        magazine = "aab"

        # act
        result = self.__solution.canConstruct(ransomNote, magazine)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case4'''
        # arrange
        ransomNote = "ab"
        magazine = "acb"

        # act
        result = self.__solution.canConstruct(ransomNote, magazine)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case4'''
        # arrange
        ransomNote = "ab"
        magazine = "ba"

        # act
        result = self.__solution.canConstruct(ransomNote, magazine)

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
