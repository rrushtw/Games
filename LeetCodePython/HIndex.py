# from FolderName.FileName import ClassName
import unittest


class HIndex:
    def __init__(self) -> None:
        pass
    # end def

    def hIndex(self, citations: list[int]) -> int:
        citations = sorted(citations)

        count: int = len(citations)
        left: int = 0
        right: int = count - 1

        while left <= right:
            mid: int = int(left + (right - left) / 2)

            if citations[mid] == count - mid:
                return citations[mid]

            if citations[mid] < count - mid:
                left = mid + 1
                continue

            if citations[mid] > count - mid:
                right = mid - 1
                # continue
        # end loop

        return count - left
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

    def test_case5(self):
        '''test case5'''
        # arrange
        citations = [0]

        # act
        result = self.__solution.hIndex(citations)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        citations = [0, 0]

        # act
        result = self.__solution.hIndex(citations)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case7(self):
        '''test case7'''
        # arrange
        citations = [1, 4, 7, 9]

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
