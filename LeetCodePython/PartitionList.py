import unittest
from ListNode import ListNode, ListNodeHelper


class PartitionList:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyLess = ListNode(None)
        less = dummyLess
        dummyGreat = ListNode(None)
        great = dummyGreat

        while head is not None:
            value = head.val
            if value < x:
                less.next = ListNode(value)
                less = less.next
            else:
                great.next = ListNode(value)
                great = great.next

            head = head.next
        # end loop

        less.next = dummyGreat.next

        return dummyLess.next
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__listNodeHelper = ListNodeHelper()
        self.__solution = PartitionList()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 4, 3, 2, 5, 2])

        # act
        result = self.__solution.partition(head, 3)

        # assert
        expect = [1, 2, 2, 4, 3, 5]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        head = self.__listNodeHelper.ListToNode([2, 1])

        # act
        result = self.__solution.partition(head, 2)

        # assert
        expect = [1, 2]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end
# end class


if __name__ == "__main__":
    unittest.main()
