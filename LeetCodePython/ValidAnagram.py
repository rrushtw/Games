# from FolderName.FileName import ClassName
import unittest


class ValidAnagrame:
    def __init__(self) -> None:
        pass
    # end def

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myDict: dict = {}

        for char in s:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1
        # end loop

        for char in t:
            if char not in myDict:
                return False
            # else:
            if myDict[char] == 0:
                return False
            # else:
            myDict[char] -= 1
        # end loop

        if any(value != 0 for key, value in myDict.items()):
            return False

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = ValidAnagrame()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        s = 'anagram'
        t = 'nagaram'

        # act
        result = self.__solution.isAnagram(s, t)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        s = 'rat'
        t = 'car'

        # act
        result = self.__solution.isAnagram(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
