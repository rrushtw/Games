# from FolderName.FileName import ClassName
import unittest


class RotateArray:
    def __init__(self) -> None:
        pass
    # end def

    def rotate(self, nums: list[int], k: int) -> None:
        position = len(nums) - k if k < len(nums) else len(nums) - (k % len(nums))

        tempList: list[int] = nums[position:]
        tempList.extend(nums[:position])

        for i in range(len(nums)):
            nums[i] = tempList[i]
        # end loop

        return None
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RotateArray()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        # act
        self.__solution.rotate(nums, k)

        # assert
        expect = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(expect, nums)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [-1, -100, 3, 99]
        k = 2

        # act
        self.__solution.rotate(nums, k)

        # assert
        expect = [3, 99, -1, -100]
        self.assertEqual(expect, nums)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        nums = [1, 2]
        k = 5

        # act
        self.__solution.rotate(nums, k)

        # assert
        expect = [2, 1]
        self.assertEqual(expect, nums)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
