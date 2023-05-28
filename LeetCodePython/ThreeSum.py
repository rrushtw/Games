# from FolderName.FileName import ClassName
import unittest


class ThreeSum:
    def __init__(self) -> None:
        pass
    # end def

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        negatives = []
        zeros = []
        positives = []

        for i in nums:
            if i < 0:
                negatives.append(i)
            elif i > 0:
                positives.append(i)
            else:  # i == 0
                zeros.append(i)
        # end loop

        negatives = sorted(negatives)
        positives = sorted(positives)

        uniqueNegatives = set(negatives)
        uniquePositives = set(positives)

        tempList = []

        # 3 zero
        if len(zeros) >= 3:
            tempList.append([0, 0, 0])

        # region 2 negative, 1 positive
        if len(negatives) >= 2 and len(uniquePositives) >= 1:
            for i in range(len(negatives)-1):
                for j in range(i + 1, len(negatives)):
                    sum2 = negatives[i] + negatives[j]

                    if -sum2 in uniquePositives:
                        tempList.append([negatives[i], negatives[j], -sum2])
                # end loop
            # end loop
        # endregion

        # region 1 negative, 1 zero, 1 positive
        if len(uniqueNegatives) > 0 and len(zeros) > 0 and len(uniquePositives) > 0:
            for i in uniqueNegatives:
                if -i in uniquePositives:
                    tempList.append([i, 0, -i])
            # end loop
        # endregion

        # region 1 negative, 2 positive
        if len(uniqueNegatives) >= 1 and len(positives) >= 2:
            for i in range(len(positives) - 1):
                for j in range(i+1, len(positives)):
                    sum2 = positives[i] + positives[j]

                    if -sum2 in uniqueNegatives:
                        tempList.append([-sum2, positives[i], positives[j]])
                # end loop
            # end loop
        # endregion

        result = []
        for i in tempList:
            if i not in result:
                result.append(i)
        # end loop

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = ThreeSum()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        input = [-1, 0, 1, 2, -1, -4]

        # act
        result = self.__solution.threeSum(input)

        # assert
        expect = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        input = [0, 1, 1]

        # act
        result = self.__solution.threeSum(input)

        # assert
        expect = []
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        input = [0, 0, 0]

        # act
        result = self.__solution.threeSum(input)

        # assert
        expect = [[0, 0, 0]]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4: 4 zeros'''
        # arrange
        input = [0, 0, 0, 0]

        # act
        result = self.__solution.threeSum(input)

        # assert
        expect = [[0, 0, 0]]
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

        # act
        result = self.__solution.threeSum(input)

        # assert
        expect = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
        self.assertEqual(expect, sorted(result, key=lambda i: (i[0], i[1])))
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
