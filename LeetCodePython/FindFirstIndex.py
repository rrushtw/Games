# from FolderName.FileName import ClassName
import unittest


class FindFirstIndex:
    def __init__(self) -> None:
        pass
    # end def

    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        return len(haystack.split(needle)[0])
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = FindFirstIndex()
    # end def

    def test_case1(self):
        '''test case 1'''
        # arrange
        haystack = "sadbutsad"
        needle = "sad"

        # act
        result = self.__solution.strStr(haystack, needle)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case 2'''
        # arrange
        haystack = "leetcode"
        needle = "leeto"

        # act
        result = self.__solution.strStr(haystack, needle)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
