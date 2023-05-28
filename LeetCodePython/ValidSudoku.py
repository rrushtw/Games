# from FolderName.FileName import ClassName
import unittest


class ValidSudoku:
    def __init__(self) -> None:
        pass
    # end def

    def isValidSudoku(self, board: list[list[int]]) -> bool:
        tempList: list[int] = []
        cell: int = None

        # region check each row
        for i in range(0, 9):
            tempList.clear()

            for j in range(0, 9):
                cell = board[i][j]
                if cell == '.':
                    continue

                if cell in tempList:
                    return False

                tempList.append(cell)
            # end loop
        # end loop
        # endregion

        # region check each column
        for i in range(0, 9):
            tempList.clear()

            for j in range(0, 9):
                cell = board[j][i]
                if cell == '.':
                    continue

                if cell in tempList:
                    return False

                tempList.append(cell)
            # end loop
        # end loop
        # endregion

        # region check each grid
        for i in range(0, 3):
            for j in range(0, 3):
                tempList.clear()

                for m in range(0, 3):
                    for n in range(0, 3):
                        cell = board[3 * i + m][3 * j + n]
                        if cell == '.':
                            continue

                        if cell in tempList:
                            return False

                        tempList.append(cell)
                    # end loop
                # end loop
            # end loop
        # end loop
        # endregion

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = ValidSudoku()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        # act
        result = self.__solution.isValidSudoku(board)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        # act
        result = self.__solution.isValidSudoku(board)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
