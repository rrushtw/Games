# from FolderName.FileName import ClassName
import unittest


class JumpGame:
    def __init__(self) -> None:
        pass
    # end def

    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumpCount: int = 0
        slow: int = 0
        fast: int = nums[slow]

        for i in range(len(nums)):
            if slow < i and i <= fast:
                slow = fast
                jumpCount += 1

            fast = max(fast, i + nums[i])
        # end loop

        return jumpCount
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
        result = self.__solution.jump(nums)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [2, 3, 0, 1, 4]

        # act
        result = self.__solution.jump(nums)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        nums = [2, 3, 0, 0, 0]

        # act
        result = self.__solution.jump(nums)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        nums = [1, 0]

        # act
        result = self.__solution.jump(nums)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        nums = [0]

        # act
        result = self.__solution.jump(nums)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]

        # act
        result = self.__solution.jump(nums)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
