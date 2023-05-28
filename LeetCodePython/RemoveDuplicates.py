# from FolderName.FileName import ClassName
import unittest


class RemoveDuplicates:
    def __init__(self) -> None:
        pass
    # end def

    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 1

        slow: int = 0
        fast: int = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
                continue
            # else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
        # end loop

        return slow + 1
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RemoveDuplicates()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [1, 1, 2]

        # act
        result = self.__solution.removeDuplicates(nums)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        # act
        result = self.__solution.removeDuplicates(nums)

        # assert
        expect = 5
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
