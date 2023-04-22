# from FolderName.FileName import ClassName
import unittest


class FourSum:
    def __init__(self) -> None:
        pass
    # end def

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        positives: list[int] = []
        zeros: list[int] = []
        negatives: list[int] = []

        for number in sorted(nums):
            if number < 0:
                negatives.append(number)
                continue

            if number == 0:
                zeros.append(number)
                continue

            if number > 0:
                positives.append(number)
                continue
        # end loop

        # region 4 negative
        if target < 0 and len(negatives) >= 4:
            for i in range(len(negatives) - 3):
                for j in range(i + 1, len(negatives) - 2):
                    m = j + 1
                    n = len(negatives) - 1

                    while m < n:
                        sum = negatives[i] + negatives[j] + \
                            negatives[m] + negatives[n]

                        if sum == target:
                            result.append(
                                [negatives[i], negatives[j], negatives[m], negatives[n]])

                            m += 1
                            n -= 1
                            continue

                        if sum < target:
                            m += 1
                            continue

                        if sum > target:
                            n -= 1
                            continue
                    # end loop
                # end loop
            # end loop
        # endregion

        # region 3 negative, 1 zero
        if target < 0 and len(negatives) >= 3 and len(zeros) >= 1:
            for i in range(len(negatives) - 2):
                j = i + 1
                k = len(negatives) - 1

                while j < k:
                    sum = negatives[i] + negatives[j] + negatives[k]

                    if sum == target:
                        result.append(
                            [negatives[i], negatives[j], negatives[k], 0])

                        j += 1
                        k -= 1
                        continue

                    if sum < target:
                        j += 1
                        continue

                    if sum > target:
                        k -= 1
                        continue
                # end loop
            # end loop
        # endregion

        # region 3 negative, 1 positive
        if len(negatives) >= 3 and len(positives) >= 1:
            for p in positives:
                for i in range(len(negatives) - 2):
                    j = i + 1
                    k = len(negatives) - 1

                    while j < k:
                        sum = negatives[i] + negatives[j] + negatives[k] + p

                        if sum == target:
                            result.append(
                                [negatives[i], negatives[j], negatives[k], p])

                            j += 1
                            k -= 1
                            continue

                        if sum < target:
                            j += 1
                            continue

                        if sum > target:
                            k -= 1
                            continue
                    # end loop
                # end loop
            # end loop
        # endregion

        # region 2 negative, 2 zero
        if target < 0 and len(negatives) >= 2 and len(zeros) >= 2:
            i: int = 0
            j: int = len(negatives) - 1

            while i < j:
                sum = negatives[i] + negatives[j]

                if sum == target:
                    result.append([negatives[i], negatives[j], 0, 0])
                    break

                if sum < target:
                    i += 1
                    continue

                if sum > target:
                    j -= 1
                    continue
            # end loop
        # endregion

        # region 2 negative, 1 zero, 1 postive
        if len(negatives) >= 2 and len(zeros) >= 1 and len(positives) >= 1:
            for p in positives:
                i: int = 0
                j: int = len(negatives) - 1

                while i < j:
                    sum = negatives[i] + negatives[j] + p

                    if sum == target:
                        result.append([negatives[i], negatives[j], 0, p])

                        i += 1
                        j -= 1
                        continue

                    if sum < target:
                        i += 1
                        continue

                    if sum > target:
                        j -= 1
                        continue
                # end loop
            # end loop
        # endregion

        # region 2 negative, 2 postive
        if len(negatives) >= 2 and len(positives) >= 2:
            for i in range(len(negatives) - 1):
                for j in range(i + 1, len(negatives)):
                    for m in range(len(positives) - 1):
                        for n in range(m + 1, len(positives)):
                            sum = negatives[i] + negatives[j] + \
                                positives[m] + positives[n]

                            if sum == target:
                                result.append(
                                    [negatives[i], negatives[j], positives[m], positives[n]])
                        # end loop
                    # end loop
                # end loop
            # end loop
        # endregion

        # region 1 negative, 3 zero
        if target < 0 and len(negatives) >= 1 and len(zeros) >= 3:
            if any(n == target for n in negatives):
                result.append([target, 0, 0, 0])
        # endregion

        # region 1 negative, 2 zero, 1 postive
        if len(negatives) >= 1 and len(zeros) >= 2 and len(positives) >= 1:
            i = 0
            j = len(positives) - 1

            while i < len(negatives) and j >= 0:
                sum = negatives[i] + positives[j]

                if sum == target:
                    result.append([negatives[i], 0, 0, positives[j]])

                    i += 1
                    j -= 1
                    continue

                if sum < target:
                    i += 1
                    continue

                if sum > target:
                    j -= 1
                    continue
            # end loop
        # endregion

        # region 1 negative, 1 zero, 2 postive
        if len(negatives) >= 1 and len(zeros) >= 1 and len(positives) >= 2:
            for n in negatives:
                i = 0
                j = len(positives) - 1

                while i < j:
                    sum = n + positives[i] + positives[j]

                    if sum == target:
                        result.append([n, 0, positives[i], positives[j]])

                        i += 1
                        j -= 1
                        continue

                    if sum < target:
                        i += 1
                        continue

                    if sum > target:
                        j -= 1
                        continue
                # end loop
            # end loop
        # endregion

        # region 1 negative, 3 postive
        if len(negatives) >= 1 and len(positives) >= 3:
            for n in negatives:
                for i in range(len(positives) - 2):
                    j = i + 1
                    k = len(positives) - 1

                    while j < k:
                        sum = n + positives[i] + positives[j] + positives[k]

                        if sum == target:
                            result.append(
                                [n, positives[i], positives[j], positives[k]])
                            j += 1
                            k -= 1
                            continue

                        if sum < target:
                            j += 1
                            continue

                        if sum > target:
                            k -= 1
                            continue
                    # end loop
                # end loop
            # end loop
        # endregion

        # region 4 zero
        if target == 0 and len(zeros) >= 4:
            result.append([0, 0, 0, 0])
        # endregion

        # region 3 zero, 1 postive
        if target > 0 and len(zeros) >= 3 and len(positives) >= 1:
            if any(p == target for p in positives):
                result.append([0, 0, 0, target])
        # endregion

        # region 2 zero, 2 postive
        if target > 0 and len(zeros) >= 2 and len(positives) >= 2:
            i = 0
            j = len(positives) - 1

            while i < j:
                sum = positives[i] + positives[j]

                if sum == target:
                    result.append([0, 0, positives[i], positives[j]])

                    i += 1
                    j -= 1
                    continue

                if sum < target:
                    i += 1
                    continue

                if sum > target:
                    j -= 1
                    continue
        # endregion

        # region 1 zero, 3 postive
        if target > 0 and len(zeros) >= 1 and len(positives) >= 3:
            for i in range(len(positives) - 2):
                j = i + 1
                k = len(positives) - 1

                while j < k:
                    sum = positives[i] + positives[j] + positives[k]

                    if sum == target:
                        result.append(
                            [0, positives[i], positives[j], positives[k]])

                        j += 1
                        k -= 1
                        continue

                    if sum < target:
                        j += 1
                        continue

                    if sum > target:
                        k -= 1
                        continue
                # end loop
            # end loop
        # endregion

        # region 4 postive
        if target > 0 and len(positives) >= 4:
            for i in range(len(positives) - 3):
                for j in range(i + 1, len(positives) - 2):
                    m = j + 1
                    n = len(positives) - 1

                    while m < n:
                        sum = positives[i] + positives[j] + \
                            positives[m] + positives[n]

                        if sum == target:
                            result.append(
                                [positives[i], positives[j], positives[m], positives[n]])

                            m += 1
                            n -= 1
                            continue

                        if sum < target:
                            m += 1
                            continue

                        if sum > target:
                            n -= 1
                            continue
                    # end loop
                # end loop
            # end loop
        # endregion

        uniqueSet = []

        for i in result:
            if i not in uniqueSet:
                uniqueSet.append(i)
        # end loop

        return uniqueSet
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = FourSum()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [1, 0, -1, 0, -2, 2]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [2, 2, 2, 2, 2]
        target = 8

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[2, 2, 2, 2]]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3: double postive solution'''
        # arrange
        nums = [0, 0, 1, 2, 3, 4]
        target = 5

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[0, 0, 1, 4], [0, 0, 2, 3]]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        nums = [-3, -1, 0, 2, 4, 5]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-3, -1, 0, 4]]
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        nums = [-2, -1, -1, 1, 1, 2, 2]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-2, -1, 1, 2], [-1, -1, 1, 1]]
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        nums = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-5, -4, 4, 5], [-5, -3, 3, 5], [-5, -2, 2, 5], [-5, -2, 3, 4], [-5, -1, 1, 5], [-5, -1, 2, 4], [-5, 0, 0, 5], [-5, 0, 1, 4], [-5, 0, 2, 3], [-4, -3, 2, 5], [-4, -3, 3, 4], [-4, -2, 1, 5], [-4, -2, 2, 4], [-4, -1, 0, 5],
                  [-4, -1, 1, 4], [-4, -1, 2, 3], [-4, 0, 0, 4], [-4, 0, 1, 3], [-3, -2, 0, 5], [-3, -2, 1, 4], [-3, -2, 2, 3], [-3, -1, 0, 4], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case7(self):
        '''test case7'''
        # arrange
        nums = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
        target = 0

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-4, -3, 3, 4], [-4, -2, 2, 4], [-4, -1, 1, 4], [-4, -1, 2, 3], [-4, 0, 0, 4], [-4, 0, 1, 3], [-3, -2, 1, 4],
                  [-3, -2, 2, 3], [-3, -1, 0, 4], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case8(self):
        '''test case8'''
        # arrange
        nums = [-9, -2, 7, 6, -8, 5, 8, 3, -10, -7, 8, -8, 0, 0, 1, -8, 7]
        target = 4

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-10, -2, 8, 8], [-10, 0, 6, 8], [-10, 0, 7, 7], [-10, 1, 5, 8], [-10, 1, 6, 7], [-10, 3, 5, 6], [-9, -2, 7, 8], [-9, 0, 5, 8], [-9, 0, 6, 7],
                  [-9, 1, 5, 7], [-8, -2, 6, 8], [-8, -2, 7, 7], [-8, 0, 5, 7], [-8, 1, 3, 8], [-8, 1, 5, 6], [-7, -2, 5, 8], [-7, -2, 6, 7], [-7, 0, 3, 8], [-7, 0, 5, 6], [-7, 1, 3, 7], [-2, 0, 0, 6], [-2, 0, 1, 5], [0, 0, 1, 3]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case9(self):
        '''test case9'''
        # arrange
        nums = [-6, -6, -2, 8, 1, -3, 0, -4, -2, -4, 0, -5, -6, 6, 9, 3, 9, 0]
        target = -14

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-6, -6, -5, 3], [-6, -6, -3, 1], [-6, -6, -2, 0], [-6, -5, -4, 1],
                  [-6, -5, -3, 0], [-6, -4, -4, 0], [-6, -4, -2, -2], [-5, -4, -3, -2]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def test_case10(self):
        '''test case10'''
        # arrange
        nums = [0, -7, -2, 8, -7, 8, 3, -8, 7, 5, -7, 3, 6, -8, 8, -2, 4]
        target = 19

        # act
        result = self.__solution.fourSum(nums, target)

        # assert
        expect = [[-2, 5, 8, 8], [-2, 6, 7, 8], [0, 3, 8, 8], [0, 4, 7, 8],
                  [0, 5, 6, 8], [3, 3, 5, 8], [3, 3, 6, 7], [3, 4, 5, 7]]
        self.assertEqual(sorted(expect), sorted(result))
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
