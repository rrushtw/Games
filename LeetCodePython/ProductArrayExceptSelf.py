# from FolderName.FileName import ClassName
import unittest


class ProductArrayExceptSelf:
    def __init__(self) -> None:
        pass
    # end def

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result: list[int] = [1] # give the initial element: 1

        for i in range(1, len(nums)):
            result.append(nums[i - 1] * result[i - 1])
        # end loop

        temp: int = 1

        for i in range(0, len(nums)):
            j = len(nums) - 1 - i

            result[j] *= temp
            temp *= nums[j]
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = ProductArrayExceptSelf()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [1, 2, 3, 4]

        # act
        result = self.__solution.productExceptSelf(nums)

        # assert
        expect = [24, 12, 8, 6]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [-1, 1, 0, -3, 3]

        # act
        result = self.__solution.productExceptSelf(nums)

        # assert
        expect = [0, 0, 9, 0, 0]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        nums = [30, 30, 30, 30, 30]

        # act
        result = self.__solution.productExceptSelf(nums)

        # assert
        expect = [810000, 810000, 810000, 810000, 810000]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        nums = [0, 0]

        # act
        result = self.__solution.productExceptSelf(nums)

        # assert
        expect = [0, 0]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
