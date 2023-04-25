# from FolderName.FileName import ClassName
import unittest


class RemoveElement:
    def __init__(self) -> None:
        pass
    # end def

    def removeElement(self, nums: list[int], val: int) -> int:
        count: int = len(nums)
        tempList: list[int] = []

        for i in nums:
            if i == val:
                count -= 1
                i = 51
            else:
                tempList.append(i)
        # end loop

        for i in range(len(tempList)):
            nums[i] = tempList[i]
        # end loop

        return count
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RemoveElement()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [3, 2, 2, 3]
        val = 3

        # act
        result = self.__solution.removeElement(nums, val)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2

        # act
        result = self.__solution.removeElement(nums, val)

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
