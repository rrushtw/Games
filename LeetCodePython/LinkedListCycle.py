import unittest

# from FolderName.FileName import ClassName
from ListNode import ListNode, ListNodeHelper


class LinkedListCycle:
    def __init__(self) -> None:
        pass
    # end def

    def hasCycle(self, head: ListNode) -> bool:
        nodes = {}

        while head is not None:
            if head.next in nodes:
                return True
            # else:
            nodes[head.next] = 1
            head = head.next
        # end loop

        return False
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = LinkedListCycle()
        self.__listNodeHelper = ListNodeHelper()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        head = self.__listNodeHelper.ListToNode([3, 2, 0, -4])
        head.next.next.next.next = head.next

        # act
        result = self.__solution.hasCycle(head)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2])
        head.next.next = head

        # act
        result = self.__solution.hasCycle(head)

        # assert
        expect = True
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1])

        # act
        result = self.__solution.hasCycle(head)

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
