# from FolderName.FileName import ClassName
import unittest


class LongestCommonPrefix:
    def __init__(self) -> None:
        pass
    # end def

    def longestCommonPrefix(self, strs: list[str]) -> str:
        result: str = ''
        firstVocabulary = strs[0]

        if len(strs) == 1:
            return firstVocabulary

        shortestVocabulary = min(strs, key=lambda i: len(i))
        for i in range(len(shortestVocabulary)):
            if any(vocabulary[i] != firstVocabulary[i] for vocabulary in strs):
                break
            # else:

            result += firstVocabulary[i]
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = LongestCommonPrefix()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        strs = ["flower", "flow", "flight"]

        # act
        result = self.__solution.longestCommonPrefix(strs)

        # assert
        expect = "fl"
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        strs = ["dog", "racecar", "car"]

        # act
        result = self.__solution.longestCommonPrefix(strs)

        # assert
        expect = ""
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3: 200 the same vocabulary'''
        # arrange
        strs: list[str] = []

        for i in range(200):
            strs.append('a' * 200)
        # end loop

        # act
        result = self.__solution.longestCommonPrefix(strs)

        # assert
        expect = 'a' * 200
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
