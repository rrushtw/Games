# from FolderName.FileName import ClassName
import unittest


class LongestConsecutiveSequence:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxLength: int = 0
        slow: int = 0
        fast: int = 0
        nums = sorted(set(nums))

        while fast < len(nums):
            if nums[fast] - nums[fast - 1] > 1:
                maxLength = max(maxLength, fast - slow)
                slow = fast
            # else:
            fast += 1
        # end loop

        return max(maxLength, fast - slow)
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = LongestConsecutiveSequence()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        nums = [100, 4, 200, 1, 3, 2]

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 9
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        nums = []

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case4'''
        # arrange
        nums = [0]

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case5'''
        # arrange
        nums = [1, 2, 0, 1]

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case6(self) -> None:
        '''test case6'''
        # arrange
        nums = [0, 0]

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case7(self) -> None:
        '''test case7'''
        # arrange
        nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

        # act
        result = self.__solution.longestConsecutive(nums)

        # assert
        expect = 7
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
