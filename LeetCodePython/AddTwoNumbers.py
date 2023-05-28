import unittest

# from FolderName.FileName import ClassName
from ListNode import ListNode, ListNodeHelper


class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head: ListNode = ListNode(0)
        currentNode = head
        temp: int = 0

        while l1 is not None or l2 is not None:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0

            temp += value1 + value2
            currentNode.next = ListNode(temp % 10)
            temp = int(temp / 10)

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            currentNode = currentNode.next
        # end loop

        if temp != 0:
            currentNode.next = ListNode(temp)

        return head.next
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__listNodeHelper = ListNodeHelper()
        self.__solution = AddTwoNumbers()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        l1 = self.__listNodeHelper.ListToNode([2, 4, 3])
        l2 = self.__listNodeHelper.ListToNode([5, 6, 4])

        # act
        result = self.__solution.addTwoNumbers(l1, l2)

        # assert
        expect = [7, 0, 8]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        l1 = self.__listNodeHelper.ListToNode([0])
        l2 = self.__listNodeHelper.ListToNode([0])

        # act
        result = self.__solution.addTwoNumbers(l1, l2)

        # assert
        expect = [0]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        l1 = self.__listNodeHelper.ListToNode([9, 9, 9, 9, 9, 9, 9])
        l2 = self.__listNodeHelper.ListToNode([9, 9, 9, 9])

        # act
        result = self.__solution.addTwoNumbers(l1, l2)

        # assert
        expect = [8, 9, 9, 9, 0, 0, 0, 1]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
