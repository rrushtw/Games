# from FolderName.FileName import ClassName
import unittest


class ValidAnagrame:
    def __init__(self) -> None:
        pass
    # end def

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)
        return dic.values()
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = ValidAnagrame()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

        # act
        result = self.__solution.groupAnagrams(strs)

        # assert
        expect = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        for i in range(len(result)):
            result[i] = sorted(result[i])
        # end loop
        for i in range(len(expect)):
            expect[i] = sorted(expect[i])
        # end loop
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        strs = [""]

        # act
        result = self.__solution.groupAnagrams(strs)

        # assert
        expect = [[""]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        strs = ["a"]

        # act
        result = self.__solution.groupAnagrams(strs)

        # assert
        expect = [["a"]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case4(self) -> None:
        '''test case4'''
        # arrange
        strs = ["ddddddddddg", "dgggggggggg"]

        # act
        result = self.__solution.groupAnagrams(strs)

        # assert
        expect = [["dgggggggggg"], ["ddddddddddg"]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
