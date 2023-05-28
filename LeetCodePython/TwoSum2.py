# from FolderName.FileName import ClassName
import unittest


class TwoSum:
    def __init__(self) -> None:
        pass
    # end def

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]

            if sum < target:
                left += 1
                continue

            if sum > target:
                right -= 1
                continue
        # end loop

        return None
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = TwoSum()
    # end def

    def test_case1(self):
        '''test case 1'''
        # arrange
        numbers = [2, 7, 11, 15]
        target = 9

        # act
        result = self.__solution.twoSum(numbers, target)

        # assert
        expect = [1, 2]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case 2'''
        # arrange
        numbers = [2, 3, 4]
        target = 6

        # act
        result = self.__solution.twoSum(numbers, target)

        # assert
        expect = [1, 3]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case 3'''
        # arrange
        numbers = [-1, 0]
        target = -1

        # act
        result = self.__solution.twoSum(numbers, target)

        # assert
        expect = [1, 2]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
