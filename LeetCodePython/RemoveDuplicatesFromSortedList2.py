import unittest

from ListNode import ListNode, ListNodeHelper


class RemoveDuplicatesfromSortedList2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        node: ListNode = dummy
        temp: int = None

        while head is not None:
            if head.val == temp:
                head = head.next
                continue
            # else:
            temp = head.val
            next = head.next.val if head.next is not None else None
            if temp != next:
                node.next = ListNode(temp)
                node = node.next

            head = head.next
        # end loop

        return dummy.next
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__listNodeHelper = ListNodeHelper()
        self.__solution = RemoveDuplicatesfromSortedList2()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2, 3, 3, 4, 4, 5])

        # act
        result = self.__solution.deleteDuplicates(head)

        # assert
        expect = [1, 2, 5]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 1, 1, 2, 3])

        # act
        result = self.__solution.deleteDuplicates(head)

        # assert
        expect = [2, 3]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
