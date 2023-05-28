# from FolderName.FileName import ClassName
import unittest


class GasStation:
    def __init__(self) -> None:
        pass
    # end def

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totalGas: int = 0
        totalCost: int = 0
        tank: int = 0
        position: int = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]

            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                position = i + 1
                continue
        # end loop

        return -1 if totalGas < totalCost else position
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = GasStation()
    # end def

    def test_case1(self):
        '''test case 1'''
        # arrange
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]

        # act
        result = self.__solution.canCompleteCircuit(gas, cost)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case 2'''
        # arrange
        gas = [2, 3, 4]
        cost = [3, 4, 3]

        # act
        result = self.__solution.canCompleteCircuit(gas, cost)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case 3'''
        # arrange
        gas = [0]
        cost = [0]

        # act
        result = self.__solution.canCompleteCircuit(gas, cost)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case 4'''
        # arrange
        gas = [0]
        cost = [1]

        # act
        result = self.__solution.canCompleteCircuit(gas, cost)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case 5'''
        # arrange
        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]

        # act
        result = self.__solution.canCompleteCircuit(gas, cost)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case 6'''
        # arrange
        gas = [3, 1, 1]
        cost = [1, 2, 2]

        # act
        result = self.__solution.canCompleteCircuit(gas, cost)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
