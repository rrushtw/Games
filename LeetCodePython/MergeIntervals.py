import unittest


class MergeIntervals:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result: list[list[int]] = list()
        previousLeft: int = None
        previousRight: int = None

        for i in sorted(intervals, key=lambda x: (x[0], x[-1])):
            if previousLeft is None and previousRight is None:
                previousLeft = i[0]
                previousRight = i[-1]
                continue

            left = i[0]
            right = i[-1]

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
        self.__solution = MergeIntervals()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

        # act
        result = self.__solution.merge(intervals)

        # assert
        expect = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        intervals = [[1, 4], [4, 5]]

        # act
        result = self.__solution.merge(intervals)

        # assert
        expect = [[1, 5]]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        intervals = [[1, 4], [0, 4]]

        # act
        result = self.__solution.merge(intervals)

        # assert
        expect = [[0, 4]]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case 4'''
        # arrange
        intervals = [[1, 4], [2, 3]]

        # act
        result = self.__solution.merge(intervals)

        # assert
        expect = [[1, 4]]
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case 5'''
        # arrange
        intervals = [[1, 2], [3, 4], [5, 6], [2, 5]]

        # act
        result = self.__solution.merge(intervals)

        # assert
        expect = [[1, 6]]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
