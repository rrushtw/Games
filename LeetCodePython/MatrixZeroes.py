# from FolderName.FileName import ClassName
import unittest


class MatrixZeroes:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        xSkipList: list[int] = []
        ySkipList: list[int] = []
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    if x not in xSkipList:
                        xSkipList.append(x)
                    if y not in ySkipList:
                        ySkipList.append(y)
            # end loop
        # end loop

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if x in xSkipList or y in ySkipList:
                    matrix[y][x] = 0
            # end loop
        # end loop
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = MatrixZeroes()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        matrix = [[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]

        # act
        self.__solution.setZeroes(matrix)

        # assert
        expect = [[1, 0, 1],
                  [0, 0, 0],
                  [1, 0, 1]]
        self.assertEqual(expect, matrix)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        matrix = [[0, 1, 2, 0],
                  [3, 4, 5, 2],
                  [1, 3, 1, 5]]

        # act
        self.__solution.setZeroes(matrix)

        # assert
        expect = [[0, 0, 0, 0],
                  [0, 4, 5, 0],
                  [0, 3, 1, 0]]
        self.assertEqual(expect, matrix)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        matrix = [[0, 1, 1],
                  [1, 1, 1],
                  [1, 1, 0]]

        # act
        self.__solution.setZeroes(matrix)

        # assert
        expect = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
        self.assertEqual(expect, matrix)
    # end def

    def test_case4(self) -> None:
        '''test case 4'''
        # arrange
        matrix = [[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]]

        # act
        self.__solution.setZeroes(matrix)

        # assert
        expect = [[1, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.assertEqual(expect, matrix)
    # end def

    def test_case5(self) -> None:
        '''test case 5'''
        # arrange
        matrix = [[1],
                  [0]]

        # act
        self.__solution.setZeroes(matrix)

        # assert
        expect = [[0],
                  [0]]
        self.assertEqual(expect, matrix)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
