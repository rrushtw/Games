# from FolderName.FileName import ClassName
import unittest


class GameOfLife:
    def gameOfLife(self, board: list[list[int]]) -> None:
        tempMatrix: list[list[int]] = []
        tempRow: list[int] = None

        for y in range(0, len(board)):
            tempRow = []
            for x in range(0, len(board[0])):
                liveCount: int = 0

                if y > 0 and x > 0 and board[y - 1][x - 1] == 1:
                    liveCount += 1

                if y > 0 and board[y - 1][x] == 1:
                    liveCount += 1

                if y > 0 and x < len(board[0]) - 1 and board[y - 1][x + 1] == 1:
                    liveCount += 1

                if x > 0 and board[y][x - 1] == 1:
                    liveCount += 1

                if x < len(board[0]) - 1 and board[y][x + 1] == 1:
                    liveCount += 1

                if y < len(board) - 1 and x > 0 and board[y + 1][x - 1] == 1:
                    liveCount += 1

                if y < len(board) - 1 and board[y + 1][x] == 1:
                    liveCount += 1

                if y < len(board) - 1 and x < len(board[0]) - 1 and board[y + 1][x + 1] == 1:
                    liveCount += 1

                if board[y][x] == 1:
                    tempRow.append(
                        1 if liveCount == 2 or liveCount == 3 else 0
                    )
                    continue
                if board[y][x] == 0:
                    tempRow.append(1 if liveCount == 3 else 0)
                    continue
            # end loop
            tempMatrix.append(tempRow)
        # end loop

        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                board[y][x] = tempMatrix[y][x]
            # end loop
        # end loop
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = GameOfLife()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        matrix = [[0, 1, 0],
                  [0, 0, 1],
                  [1, 1, 1],
                  [0, 0, 0]]

        # act
        self.__solution.gameOfLife(matrix)

        # assert
        expect = [[0, 0, 0],
                  [1, 0, 1],
                  [0, 1, 1],
                  [0, 1, 0]]
        self.assertEqual(expect, matrix)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        matrix = [[1, 1],
                  [1, 0]]

        # act
        self.__solution.gameOfLife(matrix)

        # assert
        expect = [[1, 1],
                  [1, 1]]
        self.assertEqual(expect, matrix)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
