# from FolderName.FileName import ClassName
import unittest


class IsomorphicStrings:
    def __init__(self) -> None:
        pass
    # end def

    def isIsomorphic(self, s: str, t: str) -> bool:
        myDictA: dict = {}
        myDictB: dict = {}
        id: int = 0

        for i in range(len(s)):
            if s[i] not in myDictA and t[i] not in myDictB:
                myDictA[s[i]] = id
                myDictB[t[i]] = id
                id += 1
            elif s[i] in myDictA and t[i] in myDictB:
                if myDictA[s[i]] == myDictB[t[i]]:
                    continue
                else:
                    return False
            else:
                return False
        # end loop

        return True
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = IsomorphicStrings()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        s = 'egg'
        t = 'add'

        # act
        result = self.__solution.isIsomorphic(s, t)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        s = 'foo'
        t = 'bar'

        # act
        result = self.__solution.isIsomorphic(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        s = 'paper'
        t = 'title'

        # act
        result = self.__solution.isIsomorphic(s, t)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case4'''
        # arrange
        s = 'bbbaaaba'
        t = 'aaabbbba'

        # act
        result = self.__solution.isIsomorphic(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case5'''
        # arrange
        s = 'badc'
        t = 'baba'

        # act
        result = self.__solution.isIsomorphic(s, t)

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
