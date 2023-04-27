# from FolderName.FileName import ClassName
import unittest


class HIndex:
    def __init__(self) -> None:
        pass
    # end def

    def hIndex(self, citations: list[int]) -> int:
        dict = {}

        for i in sorted(citations):
            if i not in dict:
                dict[i] = 0

            for key in dict.keys():
                if key <= i:
                    dict[key] += 1
            # end loop
        # end loop

        result: int = 0
        for key, value in dict.items():
            result = max(result, min(key, value))
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = HIndex()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        citations = [3, 0, 6, 1, 5]

        # act
        result = self.__solution.hIndex(citations)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        citations = [1, 3, 1]

        # act
        result = self.__solution.hIndex(citations)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        citations = [100]

        # act
        result = self.__solution.hIndex(citations)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        citations = [99, 99, 99]

        # act
        result = self.__solution.hIndex(citations)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
