# from FolderName.FileName import ClassName
import unittest


class BestTimeToBuyAndSellStock:
    def __init__(self) -> None:
        pass
    # end def

    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        slow: int = 0
        fast: int = 1
        profit: int = 0
        while fast < len(prices):
            if prices[slow] > prices[fast]:
                slow = fast

            if prices[fast] - prices[slow] > profit:
                profit = prices[fast] - prices[slow]
            
            fast += 1
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
        expect = 5
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
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
