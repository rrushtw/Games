# from FolderName.FileName import ClassName
import unittest


class MergeSortedArray:
    def __init__(self) -> None:
        pass
    # end def

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        tempList = nums1[:m]
        tempList.extend(nums2[:n])
        tempList = sorted(tempList)

        for i in range(len(nums1)):
            nums1[i] = tempList[i]
        # end loop
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = MergeSortedArray()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        # act
        self.__solution.merge(nums1, m, nums2, n)

        # assert
        expect = [1, 2, 2, 3, 5, 6]
        self.assertEqual(expect, nums1)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0

        # act
        self.__solution.merge(nums1, m, nums2, n)

        # assert
        expect = [1]
        self.assertEqual(expect, nums1)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1

        # act
        self.__solution.merge(nums1, m, nums2, n)

        # assert
        expect = [1]
        self.assertEqual(expect, nums1)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
