# from FolderName.FileName import ClassName
import unittest


class FourSum:
    def __init__(self) -> None:
        pass
    # end def

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                m = j + 1
                n = len(nums) - 1

                while m < n:
                    sum = nums[i] + nums[j] + nums[m] + nums[n]
                    tuple = [nums[i], nums[j], nums[m], nums[n]]

                    if sum == target:
                        if tuple not in result:
                            result.append(tuple)

                        m += 1
                        while m < n and nums[m - 1] == nums[m]:
                            m += 1
                        # end loop

                        n -= 1
                        while m < n and nums[n + 1] == nums[n]:
                            n -= 1
                        # end loop

                        continue

                    if sum < target:
                        m += 1
                        continue

                    if sum > target:
                        n -= 1
                        continue
                # end loop
            # end loop
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = FourSum()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [1, 0, -1, 0, -2, 2]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [2, 2, 2, 2, 2]
        target = 8

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[2, 2, 2, 2]]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3: double postive solution'''
        # arrange
        nums = [0, 0, 1, 2, 3, 4]
        target = 5

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[0, 0, 1, 4], [0, 0, 2, 3]]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        nums = [-3, -1, 0, 2, 4, 5]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-3, -1, 0, 4]]
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        nums = [-2, -1, -1, 1, 1, 2, 2]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-2, -1, 1, 2], [-1, -1, 1, 1]]
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        nums = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-5, -4, 4, 5], [-5, -3, 3, 5], [-5, -2, 2, 5], [-5, -2, 3, 4], [-5, -1, 1, 5], [-5, -1, 2, 4], [-5, 0, 0, 5], [-5, 0, 1, 4], [-5, 0, 2, 3], [-4, -3, 2, 5], [-4, -3, 3, 4], [-4, -2, 1, 5], [-4, -2, 2, 4], [-4, -1, 0, 5],
                  [-4, -1, 1, 4], [-4, -1, 2, 3], [-4, 0, 0, 4], [-4, 0, 1, 3], [-3, -2, 0, 5], [-3, -2, 1, 4], [-3, -2, 2, 3], [-3, -1, 0, 4], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case7(self):
        '''test case7'''
        # arrange
        nums = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-4, -3, 3, 4], [-4, -2, 2, 4], [-4, -1, 1, 4], [-4, -1, 2, 3], [-4, 0, 0, 4], [-4, 0, 1, 3], [-3, -2, 1, 4],
                  [-3, -2, 2, 3], [-3, -1, 0, 4], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case8(self):
        '''test case8'''
        # arrange
        nums = [-9, -2, 7, 6, -8, 5, 8, 3, -10, -7, 8, -8, 0, 0, 1, -8, 7]
        target = 4

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-10, -2, 8, 8], [-10, 0, 6, 8], [-10, 0, 7, 7], [-10, 1, 5, 8], [-10, 1, 6, 7], [-10, 3, 5, 6], [-9, -2, 7, 8], [-9, 0, 5, 8], [-9, 0, 6, 7],
                  [-9, 1, 5, 7], [-8, -2, 6, 8], [-8, -2, 7, 7], [-8, 0, 5, 7], [-8, 1, 3, 8], [-8, 1, 5, 6], [-7, -2, 5, 8], [-7, -2, 6, 7], [-7, 0, 3, 8], [-7, 0, 5, 6], [-7, 1, 3, 7], [-2, 0, 0, 6], [-2, 0, 1, 5], [0, 0, 1, 3]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case9(self):
        '''test case9'''
        # arrange
        nums = [-6, -6, -2, 8, 1, -3, 0, -4, -2, -4, 0, -5, -6, 6, 9, 3, 9, 0]
        target = -14

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-6, -6, -5, 3], [-6, -6, -3, 1], [-6, -6, -2, 0], [-6, -5, -4, 1],
                  [-6, -5, -3, 0], [-6, -4, -4, 0], [-6, -4, -2, -2], [-5, -4, -3, -2]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case10(self):
        '''test case10'''
        # arrange
        nums = [0, -7, -2, 8, -7, 8, 3, -8, 7, 5, -7, 3, 6, -8, 8, -2, 4]
        target = 19

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-2, 5, 8, 8], [-2, 6, 7, 8], [0, 3, 8, 8], [0, 4, 7, 8],
                  [0, 5, 6, 8], [3, 3, 5, 8], [3, 3, 6, 7], [3, 4, 5, 7]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
