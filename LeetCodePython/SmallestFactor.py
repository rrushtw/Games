import unittest
import math


class FindSmallestFactor:
    def findSmallestFactor(self, number: int) -> int:
        if number <= 1:
            return -1  # 沒有最小因數

        if number % 2 == 0:
            return 2  # 最小因數是2

        root: int = math.floor(math.sqrt(number))
        i: int = 3
        while i <= root:
            if number % i == 0:
                return i  # 找到最小因數
            # else:

            i += 2
        # end loop

        return number  # 本身就是質數
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = FindSmallestFactor()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        number: int = 3

        # act
        result = self.__solution.findSmallestFactor(number)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        number: int = 91

        # act
        result = self.__solution.findSmallestFactor(number)

        # assert
        expect = 7
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        number: int = 4051 * 4057

        # act
        result = self.__solution.findSmallestFactor(number)

        # assert
        expect = 4051
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == '__main__':
    unittest.main()
