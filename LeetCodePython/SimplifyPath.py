import unittest


class SimplifyPath:
    def simplifyPath(self, path: str) -> str:
        stack: list[str] = list()
        directory: str = ''

        for char in path:
            if char != '/':
                directory += char
                continue
            # else:
            if directory == '..':
                if len(stack) > 0:
                    stack.pop(-1)
            elif directory == '.':
                pass
            elif directory != '':
                stack.append(directory)

            directory = ''
        # end loop

        if directory == '..':
            if len(stack) > 0:
                stack.pop(-1)
        elif directory == '.':
            pass
        elif directory != '':
            stack.append(directory)

        return ('/' + '/'.join(stack)).replace('//', '/')
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = SimplifyPath()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        path = '/home/'

        # act
        result = self.__solution.simplifyPath(path)

        # assert
        expect = '/home'
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        path = '/../'

        # act
        result = self.__solution.simplifyPath(path)

        # assert
        expect = '/'
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        path = '/home//foo/'

        # act
        result = self.__solution.simplifyPath(path)

        # assert
        expect = '/home/foo'
        self.assertEqual(expect, result)
    # end def

    def test_case4(self) -> None:
        '''test case 4'''
        # arrange
        path = "/a/./b/../../c/"

        # act
        result = self.__solution.simplifyPath(path)

        # assert
        expect = "/c"
        self.assertEqual(expect, result)
    # end def

    def test_case5(self) -> None:
        '''test case 5'''
        # arrange
        path = "/a/../../b/../c//.//"

        # act
        result = self.__solution.simplifyPath(path)

        # assert
        expect = "/c"
        self.assertEqual(expect, result)
    # end def

    def test_case6(self) -> None:
        '''test case 6'''
        # arrange
        path = "/a//b////c/d//././/.."

        # act
        result = self.__solution.simplifyPath(path)

        # assert
        expect = "/a/b/c"
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
