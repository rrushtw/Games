import unittest


class ValidParentheses:
    def isValid(self, s: str) -> bool:
        beginChar: set[str] = {'(', '[', '{'}
        pair: dict[str, str] = {
            # '(': ')',
            # '{': '}',
            # '[': ']',
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stackList: list[str] = list()

        for char in s:
            if char in beginChar:
                stackList.append(char)
                continue
            # else:
            if len(stackList) == 0:
                return False
            if stackList[-1] != pair[char]:
                return False
            # else: if stackList[-1] == pair[char]:
            stackList.pop(-1)
        # end loop

        return len(stackList) == 0
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = ValidParentheses()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        s = '()'

        # act
        result = self.__solution.isValid(s)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        s = '()[]{}'

        # act
        result = self.__solution.isValid(s)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        s = '(]'

        # act
        result = self.__solution.isValid(s)

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
