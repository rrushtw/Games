# from FolderName.FileName import ClassName
import unittest


class ThreeSumClosest:
    def __init__(self) -> None:
        pass
    # end def

    def function(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)

        outerTop10 = []  # [{'sum':0, 'gap':0}]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            innerTop10 = []  # [{'sum':0, 'gap':0}]

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == target:
                    return target

                gap = abs(s - target)
                # if this answer is not in top 5
                if len(innerTop10) > 0 and gap > innerTop10[len(innerTop10) - 1]['gap']:
                    break
                
                if not any(s == tuple['sum'] for tuple in innerTop10):
                    innerTop10.append({'sum': s, 'gap': gap})
                innerTop10 = sorted(
                    innerTop10, key=lambda tuple: tuple['gap'])[:10]

                if s > target:
                    right -= 1
                if s < target:
                    left += 1
            # end loop

            if len(outerTop10) == 0:
                outerTop10.extend(innerTop10)
                continue

            theLastOuter = outerTop10[len(outerTop10) - 1]
            if len(outerTop10) > 0 and not(any(tuple['gap'] < theLastOuter['gap'] for tuple in innerTop10)):
                break

            for tuple in innerTop10:
                if tuple['gap'] < theLastOuter['gap']:
                    outerTop10.append(tuple)

            outerTop10 = sorted(outerTop10, key=lambda tuple: tuple['gap'])[:10]
        # end loop

        return outerTop10[0]['sum']
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = ThreeSumClosest()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        nums = [-1, 2, 1, -4]
        target = 1

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        nums = [0, 0, 0]
        target = 1

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3: all numbers are smaller than target'''
        # arrange
        nums = [1, 1, 1]
        target = 3

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4: all numbers are bigger than target'''
        # arrange
        nums = [4, 1, 2, 3]
        target = 0

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 6
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5: some are bigger and some are smaller'''
        # arrange
        nums = [-3, -2, 5, 7]
        target = 0

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def test_case6(self):
        '''test case6'''
        # arrange
        nums = [-100, -98, -2, -1]
        target = -101

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = -101
        self.assertEqual(expect, result)
    # end def

    def test_case7(self):
        '''test case7'''
        # arrange
        nums = [321, 413, 82, 812, -646, -858, 729, 609, -339, 483, -323, -399, -82, -455, 18, 661, 890, -328, -311, 520, -865, -174, 55, 685, -636, 462, -172, -696, -296, -832, 766, -808, -763, 853, 482, 411, 703, 655, -793, -121, -726, 105, -966, -471, 612, 551, -257, 836, -94, -213, 511, 317, -293, 279, -571, 242, -519, 386, -670, -806, -612, -433, -481, 794, 712, 378, -325, -564, 477, 169, 601, 971, -300, -431, -152, 285, -899, 978, -419, 708, 536, -816, -
                335, 284, 384, -922, -941, 633, 934, 497, -351, 62, 392, -493, -44, -400, 646, -912, -864, 835, 713, -12, 322, -228, 340, -42, -307, -580, -802, -914, -142, 575, -684, -415, 718, -579, 759, 579, 732, -645, 525, 114, -880, -603, -699, -101, -738, -887, 327, 192, 747, -614, 393, 97, -569, 160, 782, -69, 235, -598, -116, 928, -805, -76, -521, 671, 417, 600, -442, 236, 831, 637, -562, 613, -705, -158, -237, -299, 808, -734, 364, 919, 251, -163, -343, 899]
        target = 2218

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 2218
        self.assertEqual(expect, result)
    # end def

    def test_case8(self):
        '''test case8'''
        # arrange
        nums = [13,252,-87,-431,-148,387,-290,572,-311,-721,222,673,538,919,483,-128,-518,7,-36,-840,233,-184,-541,522,-162,127,-935,-397,761,903,-217,543,906,-503,-826,-342,599,-726,960,-235,436,-91,-511,-793,-658,-143,-524,-609,-728,-734,273,-19,-10,630,-294,-453,149,-581,-405,984,154,-968,623,-631,384,-825,308,779,-7,617,221,394,151,-282,472,332,-5,-509,611,-116,113,672,-497,-182,307,-592,925,766,-62,237,-8,789,318,-314,-792,-632,-781,375,939,-304,-149,544,-742,663,484,802,616,501,-269,-458,-763,-950,-390,-816,683,-219,381,478,-129,602,-931,128,502,508,-565,-243,-695,-943,-987,-692,346,-13,-225,-740,-441,-112,658,855,-531,542,839,795,-664,404,-844,-164,-709,167,953,-941,-848,211,-75,792,-208,569,-647,-714,-76,-603,-852,-665,-897,-627,123,-177,-35,-519,-241,-711,-74,420,-2,-101,715,708,256,-307,466,-602,-636,990,857,70,590,-4,610,-151,196,-981,385,-689,-617,827,360,-959,-289,620,933,-522,597,-667,-882,524,181,-854,275,-600,453,-942,134]
        target = -2805

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = -2805
        self.assertEqual(expect, result)
    # end def

    def test_case9(self):
        '''test case9'''
        # arrange
        nums = [1,1,1,5,5,5,5,5,5]
        target = 14

        # act
        result = self.__solution.function(nums, target)

        # assert
        expect = 15
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
