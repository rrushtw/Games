# from FolderName.FileName import ClassName
import unittest


class JumpGame:
    def __init__(self) -> None:
        pass
    # end def

    def canJump(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True

        slow: int = 0
        fast: int = nums[slow]

        while fast < len(nums) - 1:
            fast = max(fast, slow + nums[slow])

            if slow == fast:
                return False
            # else:
            slow += 1
        # end loop

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = JumpGame()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [2, 3, 1, 1, 4]

        # act
        result = self.__solution.canJump(nums)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [3, 2, 1, 0, 4]

        # act
        result = self.__solution.canJump(nums)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        nums = [2, 3, 0, 0, 0]

        # act
        result = self.__solution.canJump(nums)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        nums = [1, 0]

        # act
        result = self.__solution.canJump(nums)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
