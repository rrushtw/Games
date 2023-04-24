import unittest
# from FolderName.FileName import ClassName
from ListNode import ListNode
from ListNode import ListNodeHelper


class SwapNodes:
    def __init__(self) -> None:
        pass
    # end def

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow: ListNode = head
        fast: ListNode = head

        for _ in range(k - 1):
            fast = fast.next
        # end loop

        targetA: ListNode = fast
        fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
        # end loop

        targetB: ListNode = slow

        # swap
        temp = targetA.val
        targetA.val = targetB.val
        targetB.val = temp

        return head
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = SwapNodes()
        self.__listNodeHelper = ListNodeHelper()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2, 3, 4, 5])
        k = 2

        # act
        result = self.__solution.swapNodes(head, k)
        result = self.__listNodeHelper.NodeToList(result)

        # assert
        expect = [1, 4, 3, 2, 5]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        head = self.__listNodeHelper.ListToNode([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
        k = 5

        # act
        result = self.__solution.swapNodes(head, k)
        result = self.__listNodeHelper.NodeToList(result)

        # assert
        expect = [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2, 3, 4, 5])
        k = 5

        # act
        result = self.__solution.swapNodes(head, k)
        result = self.__listNodeHelper.NodeToList(result)

        # assert
        expect = [5, 2, 3, 4, 1]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1])
        k = 1

        # act
        result = self.__solution.swapNodes(head, k)
        result = self.__listNodeHelper.NodeToList(result)

        # assert
        expect = [1]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
