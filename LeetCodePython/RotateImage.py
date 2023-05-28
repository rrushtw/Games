# from FolderName.FileName import ClassName
import unittest


class RotateImage:
    def __init__(self) -> None:
        pass
    # end def

    def rotate(self, matrix: list[list[int]]) -> None:
        xLength = len(matrix[0])
        yLength = len(matrix)
        xLimit: int = int(xLength / 2)
        if xLength % 2 != 0:
            xLimit += 1
        yLimit: int = int(yLength / 2)
        temp: int = None

        for y in range(0, yLimit):
            for x in range(0, xLimit):
                temp = matrix[y][x]
                matrix[y][x] = matrix[yLength - 1 - x][y]
                matrix[yLength - 1 - x][y] = matrix[yLength - 1 - y][xLength - 1 - x]
                matrix[yLength - 1 - y][xLength - 1 - x] = matrix[x][yLength - 1 - y]
                matrix[x][yLength - 1 - y] = temp
            # end loop
        # end loop
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RotateImage()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        # act
        self.__solution.rotate(matrix)

        # assert
        expect = [[7, 4, 1],
                  [8, 5, 2],
                  [9, 6, 3]]

        self.assertEqual(expect, matrix)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        matrix = [[5, 1, 9, 11],
                  [2, 4, 8, 10],
                  [13, 3, 6, 7],
                  [15, 14, 12, 16]]

        # act
        self.__solution.rotate(matrix)

        # assert
        expect = [[15, 13, 2, 5],
                  [14, 3, 4, 1],
                  [12, 6, 8, 9],
                  [16, 7, 10, 11]]

        self.assertEqual(expect, matrix)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        matrix = [[1]]

        # act
        self.__solution.rotate(matrix)

        # assert
        expect = [[1]]

        self.assertEqual(expect, matrix)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        matrix = [[1, 2],
                  [3, 4]]

        # act
        self.__solution.rotate(matrix)

        # assert
        expect = [[3, 1],
                  [4, 2]]

        self.assertEqual(expect, matrix)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
