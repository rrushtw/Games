# from FolderName.FileName import ClassName
import unittest


class SpiralMatrix:
    def __init__(self) -> None:
        self.__stopMoving: int = 0
        self.__goingLeft: int = -1
        self.__goingRight: int = 1
        self.__goingUp: int = -1
        self.__goingDown: int = 1
    # end def

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        leftOrRight: int = self.__goingRight
        upOrDown: int = self.__stopMoving

        left: int = 0
        right: int = len(matrix[0]) - 1
        up: int = 0
        down: int = len(matrix) - 1

        x: int = 0
        y: int = 0

        result: list[int] = []
        while len(result) < len(matrix) * len(matrix[0]):
            result.append(matrix[y][x])

            if leftOrRight == self.__goingRight and upOrDown == self.__stopMoving:
                if x == right:
                    leftOrRight = self.__stopMoving
                    upOrDown = self.__goingDown
                    up += 1
                    y += 1
                else:
                    x += 1
            elif leftOrRight == self.__stopMoving and upOrDown == self.__goingDown:
                if y == down:
                    leftOrRight = self.__goingLeft
                    upOrDown = self.__stopMoving
                    right -= 1
                    x -= 1
                else:
                    y += 1
            elif leftOrRight == self.__goingLeft and upOrDown == self.__stopMoving:
                if x == left:
                    leftOrRight = self.__stopMoving
                    upOrDown = self.__goingUp
                    down -= 1
                    y -= 1
                else:
                    x -= 1
            elif leftOrRight == self.__stopMoving and upOrDown == self.__goingUp:
                if y == up:
                    leftOrRight = self.__goingRight
                    upOrDown = self.__stopMoving
                    left += 1
                    x += 1
                else:
                    y -= 1
            else:
                return None
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = SpiralMatrix()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        # act
        result = self.__solution.spiralOrder(matrix)

        # assert
        expect = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]]

        # act
        result = self.__solution.spiralOrder(matrix)

        # assert
        expect = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        matrix = [[1]]

        # act
        result = self.__solution.spiralOrder(matrix)

        # assert
        expect = [1]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        matrix = [[1, 2],
                  [3, 4]]

        # act
        result = self.__solution.spiralOrder(matrix)

        # assert
        expect = [1, 2, 4, 3]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
