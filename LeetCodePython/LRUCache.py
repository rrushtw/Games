import unittest

from ListNode import ListNode, ListNodeHelper


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.__capacity: int = capacity
        self.__dictionary: dict = dict()
        self.__keyList: list[int] = list()
    # end def

    def get(self, key: int) -> int:
        if key not in self.__dictionary:
            return -1
        # else:
        self.__keyList.remove(key)
        self.__keyList.append(key)
        return self.__dictionary[key]
    # end def

    def put(self, key: int, value: int) -> None:
        if key in self.__dictionary:
            self.__dictionary[key] = value
            self.__keyList.remove(key)
            self.__keyList.append(key)
            return
        # else: if key not in self.__dictionary:
        if len(self.__dictionary) < self.__capacity:
            self.__dictionary[key] = value
            self.__keyList.append(key)
            return

        if len(self.__dictionary) == self.__capacity:
            firstElement = self.__keyList[0]
            self.__dictionary.pop(firstElement)
            self.__keyList.remove(firstElement)

            self.__dictionary[key] = value
            self.__keyList.append(key)
            return
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        pass
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(1, cache.get(1))
        cache.put(3, 3)
        self.assertEqual(-1, cache.get(2))
        cache.put(4, 4)
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(4, cache.get(4))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
