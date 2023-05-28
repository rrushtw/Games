# from FolderName.FileName import ClassName
import unittest


class ReverseWordsInString:
    def __init__(self) -> None:
        pass
    # end def

    def reverseWords(self, s: str) -> str:
        words: list[str] = []
        word: str = ''

        for char in s:
            if char == ' ':
                if word != '':
                    words.append(word)
                    word = ''

                continue

            word += char
        # end loop

        if word != '':
            words.append(word)

        result = ''
        i = len(words) - 1
        while i >= 0:
            result += ' '
            result += words[i]

            i -= 1
        # end loop

        return result[1:]
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = ReverseWordsInString()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        s = "the sky is blue"

        # act
        result = self.__solution.reverseWords(s)

        # assert
        expect = "blue is sky the"
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        s = "  hello world  "

        # act
        result = self.__solution.reverseWords(s)

        # assert
        expect = "world hello"
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        s = "a good   example"

        # act
        result = self.__solution.reverseWords(s)

        # assert
        expect = "example good a"
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
