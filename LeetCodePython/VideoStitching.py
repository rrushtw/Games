# from FolderName.FileName import ClassName
import unittest


class VideoStitching:
    def __init__(self) -> None:
        pass
    # end def

    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        # sort
        clips = sorted(clips)  # order by 1 asc, 2 asc

        previousTime = -1
        currentTime = 0
        result = 0

        for segment in clips:
            begin = segment[0]
            end = segment[1]

            if currentTime >= time or begin > currentTime:
                break

            if previousTime < begin and begin <= currentTime:
                previousTime = currentTime
                result += 1

            currentTime = max(currentTime, end)
        # end loop

        return result if currentTime >= time else -1
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = VideoStitching()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
        time = 10

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        clips = [[0, 1], [1, 2]]
        time = 5

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [
            1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]]
        time = 9

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4: a clip over time'''
        # arrange
        clips = [[0, 10], [5, 8]]
        time = 9

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = 1
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        clips = [[0, 1], [2, 3]]
        time = 3

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = -1
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        clips = [[0, 4], [2, 8]]
        time = 5

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case7(self):
        '''test case7: time limit test'''
        # arrange
        clips = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [
            25, 30], [26, 31], [27, 32], [28, 33], [29, 34], [30, 35], [31, 36], [32, 37], [33, 38], [34, 39], [35, 40], [36, 41], [37, 42], [38, 43], [39, 44], [40, 45], [41, 46], [42, 47], [43, 48], [44, 49], [45, 50], [46, 51], [47, 52], [48, 53], [49, 54]]
        time = 50

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = 10
        self.assertEqual(expect, result)
    # end def

    def test_case8(self):
        '''test case8'''
        # arrange
        clips = [[0, 2], [0, 3], [2, 4], [3, 6],
                 [4, 10], [6, 9], [9, 10], [10, 15]]
        time = 15

        # act
        result = self.__solution.videoStitching(clips, time)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
