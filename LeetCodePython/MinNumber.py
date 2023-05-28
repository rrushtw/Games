import unittest


class MinimumNumberOfArrowsToBurstBalloons:
    def findMinArrowsShots(self, points: list[list[int]]) -> int:
        # ORDER BY begin ASC, end DESC
        points = sorted(points, key=lambda i: (i[0], -i[-1]))

        count: int = 1
        overlapBegin: int = points[0][0]
        overlapEnd: int = points[0][-1]

        for balloonBegin, balloonEnd in points:
            if not ((balloonBegin < overlapBegin and balloonEnd < overlapBegin)
                    or (overlapEnd < balloonBegin and overlapEnd < balloonEnd)):
                overlapBegin = max(overlapBegin, balloonBegin)
                overlapEnd = min(overlapEnd, balloonEnd)
                continue
            # else:
            count += 1
            overlapBegin = balloonBegin
            overlapEnd = balloonEnd
        # end loop

        return count
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = MinimumNumberOfArrowsToBurstBalloons()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case 4'''
        # arrange
        points = [[1, 2], [1, 2], [1, 2], [3, 4], [5, 6]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case 5'''
        # arrange
        points = [[1, 4], [2, 7], [3, 8], [5, 9], [6, 10]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case6(self) -> None:
        '''test case 6'''
        # arrange
        points = [[1, 2], [4, 5], [1, 5]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case7(self) -> None:
        '''test case 7'''
        # arrange
        points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]

        # act
        result = self.__solution.findMinArrowsShots(points)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
