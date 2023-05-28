import unittest

# from FolderName.FileName import ClassName
from ListNode import ListNode, ListNodeHelper


class MergeTwoSortedLists:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head: ListNode = ListNode()
        currentNode = head

        while list1 is not None or list2 is not None:
            value1 = list1.val if list1 is not None else None
            value2 = list2.val if list2 is not None else None

            if value1 is not None and value2 is None:
                currentNode.next = ListNode(value1)
                list1 = list1.next
                currentNode = currentNode.next
                continue

            if value1 is None and value2 is not None:
                currentNode.next = ListNode(value2)
                list2 = list2.next
                currentNode = currentNode.next
                continue
            
            if value1 <= value2:
                currentNode.next = ListNode(value1)
                list1 = list1.next
                currentNode = currentNode.next
                continue

            if value1 > value2:
                currentNode.next = ListNode(value2)
                list2 = list2.next
                currentNode = currentNode.next
                continue

            # else:
            return None
        # end loop

        return head.next
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__listNodeHelper = ListNodeHelper()
        self.__solution = MergeTwoSortedLists()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        l1 = self.__listNodeHelper.ListToNode([1, 2, 4])
        l2 = self.__listNodeHelper.ListToNode([1, 3, 4])

        # act
        result = self.__solution.mergeTwoLists(l1, l2)

        # assert
        expect = [1, 1, 2, 3, 4, 4]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        l1 = self.__listNodeHelper.ListToNode([])
        l2 = self.__listNodeHelper.ListToNode([])

        # act
        result = self.__solution.mergeTwoLists(l1, l2)

        # assert
        expect = []
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        l1 = self.__listNodeHelper.ListToNode([])
        l2 = self.__listNodeHelper.ListToNode([0])

        # act
        result = self.__solution.mergeTwoLists(l1, l2)

        # assert
        expect = [0]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
