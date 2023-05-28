import unittest


class SummaryRanges:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result: list[str] = []

        if len(nums) == 0:
            return result

        if len(nums) == 1:
            result.append(str(nums[0]))
            return result

        left: int = 0
        right: int = None
        for right in range(1, len(nums)):
            if nums[right - 1] + 1 == nums[right]:
                continue
            # else:
            if right - left == 1:
                result.append(str(nums[left]))
            else:
                result.append(f'{nums[left]}->{nums[right - 1]}')

            left = right
        # end loop

        if right - left == 0:
            result.append(str(nums[left]))
        else:
            result.append(f'{nums[left]}->{nums[right]}')

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = SummaryRanges()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        nums = [0, 1, 2, 4, 5, 7]

        # act
        result = self.__solution.summaryRanges(nums)

        # assert
        expect = ["0->2", "4->5", "7"]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        nums = [0, 2, 3, 4, 6, 8, 9]

        # act
        result = self.__solution.summaryRanges(nums)

        # assert
        expect = ["0", "2->4", "6", "8->9"]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
