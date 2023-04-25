# from FolderName.FileName import ClassName
import unittest


class BestTimeToBuyAndSellStock:
    def __init__(self) -> None:
        pass
    # end def

    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit: int = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        # end loop

        return profit
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = BestTimeToBuyAndSellStock()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        prices = [7, 1, 5, 3, 6, 4]

        # act
        result = self.__solution.maxProfit(prices)

        # assert
        expect = 7
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        prices = [1, 2, 3, 4, 5]

        # act
        result = self.__solution.maxProfit(prices)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        prices = [7, 6, 4, 3, 1]

        # act
        result = self.__solution.maxProfit(prices)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
