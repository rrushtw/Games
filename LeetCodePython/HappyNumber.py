# from FolderName.FileName import ClassName
import unittest


class HappyNumber:
    def __init__(self) -> None:
        pass
    # end def

    def isHappy(self, n: int) -> bool:
        visited = set()

        while n > 1:
            if n in visited:
                return False
            # else:
            visited.add(n)

            tempSum: int = 0
            digit: int = 0
            while n > 0:
                digit = n % 10
                n = int(n / 10)
                tempSum += digit * digit
            # end loop

            n = tempSum
        # end loop

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = HappyNumber()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        n = 19

        # act
        result = self.__solution.isHappy(n)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        n = 2

        # act
        result = self.__solution.isHappy(n)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
