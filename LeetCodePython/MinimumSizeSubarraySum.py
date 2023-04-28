# from FolderName.FileName import ClassName
import unittest


class MinimumSizeSubarraySum:
    def __init__(self) -> None:
        pass
    # end def

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0

        sumOfArray: int = 0
        left: int = 0
        right: int = 0

        # shift right to reach the target
        for right in range(len(nums)):
            sumOfArray += nums[right]

            if sumOfArray >= target:
                break
        # end loop

        # shift window and left
        while left < len(nums) and right < len(nums) and left <= right:
            if sumOfArray - nums[left] >= target:
                sumOfArray -= nums[left]
                left += 1
                continue

            if right + 1 >= len(nums):
                break
            # else:
            right += 1
            sumOfArray += -nums[left] + nums[right]
            left += 1
        # end loop

        return right - left + 1
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = MinimumSizeSubarraySum()
    # end def

    def test_case1(self):
        '''test case 1'''
        # arrange
        target = 7
        nums = [2, 3, 1, 2, 4, 3]

        # act
        result = self.__solution.minSubArrayLen(target, nums)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case 2'''
        # arrange
        target = 4
        nums = [1, 4, 4]

        # act
        result = self.__solution.minSubArrayLen(target, nums)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case 3'''
        # arrange
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]

        # act
        result = self.__solution.minSubArrayLen(target, nums)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case 4'''
        # arrange
        target = 213
        nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]

        # act
        result = self.__solution.minSubArrayLen(target, nums)

        # assert
        expect = 8
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case 5'''
        # arrange
        target = 213
        nums = [83, 28, 26, 25, 25, 25, 25, 25, 12, 12, 4, 2]

        # act
        result = self.__solution.minSubArrayLen(target, nums)

        # assert
        expect = 7
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case 6'''
        # arrange
        target = 6
        nums = [3, 1, 1, 3]

        # act
        result = self.__solution.minSubArrayLen(target, nums)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
