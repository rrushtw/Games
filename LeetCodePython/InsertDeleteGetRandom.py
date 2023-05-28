# from FolderName.FileName import ClassName
import unittest
import random


class RandomizeSet:
    def __init__(self) -> None:
        self.__list: list[int] = []
    # end def

    def insert(self, val: int) -> bool:
        if val in self.__list:
            return False
        # else:
        self.__list.append(val)
        return True
    # end def

    def remove(self, val: int) -> bool:
        if val not in self.__list:
            return False
        # else:
        self.__list.remove(val)
        return True
    # end def

    def getRandom(self) -> int:
        return self.__list[random.randint(0, len(self.__list) - 1)]
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RandomizeSet()
    # end def

    def test_case1(self):
        '''test case1'''
        result: bool = None

        result = self.__solution.insert(1)
        self.assertEqual(True, result)

        result = self.__solution.remove(2)
        self.assertEqual(False, result)

        result = self.__solution.insert(2)
        self.assertEqual(True, result)

        number = self.__solution.getRandom()
        self.assertTrue(number is not None)

        result = self.__solution.remove(1)
        self.assertEqual(True, result)

        result = self.__solution.insert(2)
        self.assertEqual(False, result)

        number = self.__solution.getRandom()
        self.assertTrue(number is not None)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
