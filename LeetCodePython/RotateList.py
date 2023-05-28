# from FolderName.FileName import ClassName
import unittest

from ListNode import ListNode, ListNodeHelper


class RotateList:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        length: int = 1
        tempNode: ListNode = head
        theLastNode: ListNode = head
        while theLastNode.next is not None:
            length += 1
            theLastNode = theLastNode.next
        # end loop

        theLastNode.next = head
        k = k % length

        for _ in range(length - k - 1):
            tempNode = tempNode.next
        # end loop
        result = tempNode.next
        tempNode.next = None

        return result
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__listNodeHelper = ListNodeHelper()
        self.__solution = RotateList()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2, 3, 4, 5])
        k = 2

        # act
        result = self.__solution.rotateRight(head, k)

        # assert
        expect = [4, 5, 1, 2, 3]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        head = self.__listNodeHelper.ListToNode([0, 1, 2])
        k = 4

        # act
        result = self.__solution.rotateRight(head, k)

        # assert
        expect = [2, 0, 1]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        head = self.__listNodeHelper.ListToNode([0, 1, 2])
        k = 2

        # act
        result = self.__solution.rotateRight(head, k)

        # assert
        expect = [1, 2, 0]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case4(self) -> None:
        '''test case4'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2])
        k = 3

        # act
        result = self.__solution.rotateRight(head, k)

        # assert
        expect = [2, 1]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case5(self) -> None:
        '''test case5'''
        # arrange
        head = self.__listNodeHelper.ListToNode([1, 2, 3])
        k = 2000000000

        # act
        result = self.__solution.rotateRight(head, k)

        # assert
        expect = [2, 3, 1]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
