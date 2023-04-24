# from FolderName.FileName import ClassName
import unittest


class BinarySearch:
    def __init__(self) -> None:
        pass
    # end def

    def search(self, nums: list[int], target: int) -> int:
        if target < min(nums) or target > max(nums):
            return -1

        left: int = 0
        right: int = len(nums) - 1

        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right

        while left <= right:
            mid: int = int((left + right) / 2) 

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
                continue

            if nums[mid] > target:
                right = mid - 1
        # end loop

        return -1
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = BinarySearch()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9

        # act
        result = self.__solution.search(nums, target)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2

        # act
        result = self.__solution.search(nums, target)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        nums = [1, 3, 5, 7]
        target = 7

        # act
        result = self.__solution.search(nums, target)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        nums = [1, 3, 5, 7]
        target = 1

        # act
        result = self.__solution.search(nums, target)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        nums = [1, 3, 5, 7]
        target = 4

        # act
        result = self.__solution.search(nums, target)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
