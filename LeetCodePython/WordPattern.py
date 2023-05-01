# from FolderName.FileName import ClassName
import unittest


class WordPattern:
    def __init__(self) -> None:
        pass
    # end def

    def wordPattern(self, pattern: str, s: str) -> bool:
        words: list[str] = s.split(' ')

        if len(pattern) != len(words):
            return False

        myDictA: dict = {}
        myDictB: dict = {}
        id: int = 0

        for i in range(len(pattern)):
            if pattern[i] not in myDictA and words[i] not in myDictB:
                myDictA[pattern[i]] = id
                myDictB[words[i]] = id
                id += 1
            elif pattern[i] in myDictA and words[i] in myDictB:
                if myDictA[pattern[i]] == myDictB[words[i]]:
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
        self.__solution = WordPattern()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        s = 'abba'
        t = 'dog cat cat dog'

        # act
        result = self.__solution.wordPattern(s, t)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        s = 'abba'
        t = 'dog cat cat fish'

        # act
        result = self.__solution.wordPattern(s, t)

        # assert
        expect = False
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        s = 'aaaa'
        t = 'dog cat cat dog'

        # act
        result = self.__solution.wordPattern(s, t)

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
