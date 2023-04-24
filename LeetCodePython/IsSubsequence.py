# from FolderName.FileName import ClassName
import unittest


class IsSubsequence:
    def __init__(self) -> None:
        pass
    # end def

    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            position = t.find(char)
            if position == -1:
                return False

            t = t[position + 1:]
        # end loop

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = IsSubsequence()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        s = 'abc'
        t = 'ahbgdc'

        # act
        result = self.__solution.isSubsequence(s, t)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        s = 'axc'
        t = 'ahbgdc'

        # act
        result = self.__solution.isSubsequence(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        s = 'cba'
        t = 'ahbgdc'

        # act
        result = self.__solution.isSubsequence(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case 4'''
        # arrange
        s = 'ab'
        t = 'baab'

        # act
        result = self.__solution.isSubsequence(s, t)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case 5'''
        # arrange
        s = 'aaaaaa'
        t = 'bbaaaa'

        # act
        result = self.__solution.isSubsequence(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == '__main__':
    unittest.main()
