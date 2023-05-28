# from FolderName.FileName import ClassName
import unittest


class LongestSubstringWithoutRepeat:
    def __init__(self) -> None:
        pass
    # end def

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        subString: str = ''
        nextPosition: int = -1
        left: int = 0
        right: int = 0

        while right < len(s):
            index = s.rfind(s[right], left, right)
            # extend right if possible
            if left > nextPosition and index == -1:
                subString += s[right]

                right += 1
                continue
            # set next postition if the incoming char is duplicated
            if index != -1:
                nextPosition = max(nextPosition, index)

            # shift the sub string
            subString = subString[1:] + s[right]

            left += 1
            right += 1
        # end loop

        # here is no need to plus 1 because there is a plus 1 before breaking the loop
        return right - left
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = LongestSubstringWithoutRepeat()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        s = "abcabcbb"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        s = "bbbbb"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        s = "pwwkew"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        s = "dvdf"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        s = "ab"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        s = "eeydgwdykpv"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 7
        self.assertEqual(expect, result)
    # end def

    def test_case7(self):
        '''test case7'''
        # arrange
        s = "ruowzgiooobpple"

        # act
        result = self.__solution.lengthOfLongestSubstring(s)

        # assert
        expect = 7
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
