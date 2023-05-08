import unittest


class InsertInterval:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result: list[list[int]] = list()
        previousLeft: int = -1
        previousRight: int = -1

        intervals.append(newInterval)
        for left, right in sorted(intervals, key=lambda x: (x[0], x[-1])):
            if previousLeft == -1 and previousRight == -1:
                previousLeft = left
                previousRight = right
                continue

            if right <= previousRight:
                continue

            if previousRight >= left:
                previousRight = right
                continue
            # else:
            result.append([previousLeft, previousRight])
            previousLeft = left
            previousRight = right
        # end loop

        if previousLeft is not None and previousRight is not None:
            result.append([previousLeft, previousRight])

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = InsertInterval()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[1, 5], [6, 9]]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        intervals = []
        newInterval = [5, 7]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[5, 7]]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case 4'''
        # arrange
        intervals = [[1, 5]]
        newInterval = [5, 7]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[1, 7]]
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case 5'''
        # arrange
        intervals = [[1, 5]]
        newInterval = [6, 8]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[1, 5], [6, 8]]
        self.assertEqual(expect, result)
    # end def

    def test_case6(self) -> None:
        '''test case 6'''
        # arrange
        intervals = [[1, 5]]
        newInterval = [0, 0]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[0, 0], [1, 5]]
        self.assertEqual(expect, result)
    # end def

    def test_case7(self) -> None:
        '''test case 7'''
        # arrange
        intervals = [[0, 5], [9, 12]]
        newInterval = [7, 16]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[0, 5], [7, 16]]
        self.assertEqual(expect, result)
    # end def

    def test_case8(self) -> None:
        '''test case 8'''
        # arrange
        intervals = [[3, 5], [12, 15]]
        newInterval = [6, 6]

        # act
        result = self.__solution.insert(intervals, newInterval)

        # assert
        expect = [[3, 5], [6, 6], [12, 15]]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
