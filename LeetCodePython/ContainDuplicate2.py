# from FolderName.FileName import ClassName
import unittest


class ContainDuplicate2:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dictionary = {}

        for i in range(0, len(nums)):
            if nums[i] in dictionary and i - dictionary[nums[i]] <= k:
                return True
            # else:
            dictionary[nums[i]] = i
        # end loop

        return False
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = ContainDuplicate2()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        nums = [1, 2, 3, 1]
        k = 3

        # act
        result = self.__solution.containsNearbyDuplicate(nums, k)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        nums = [1, 0, 1, 1]
        k = 1

        # act
        result = self.__solution.containsNearbyDuplicate(nums, k)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        nums = [1, 2, 3, 1, 2, 3]
        k = 2

        # act
        result = self.__solution.containsNearbyDuplicate(nums, k)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case4'''
        # arrange
        nums = [1, 1]
        k = 3

        # act
        result = self.__solution.containsNearbyDuplicate(nums, k)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
