# from FolderName.FileName import ClassName
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next
    # end def
# end class


class RemoveNthNodeFromEndOfList:
    def __init__(self) -> None:
        pass
    # end def

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes: list[ListNode] = []
        currentElement: ListNode = head

        while currentElement is not None:
            nodes.append(currentElement)

            currentElement = currentElement.next
        # end loop

        if len(nodes) == n:
            if head.next is not None:
                return head.next
            # else:
            return None

        if n == 1:
            nodes[len(nodes) - 2].next = None
        else:
            nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n + 1]

        return head
    # end def

    def listToNode(self, list: list[int]) -> ListNode:
        head = ListNode(list[0])
        currentNode = head

        for element in list[1:]:
            currentNode.next = ListNode(element)
            currentNode = currentNode.next
        # end loop

        return head
    # end def

    def nodeToList(self, head: ListNode) -> list[int]:
        if head is None:
            return None

        currentElement = head
        list = []

        while currentElement is not None:
            list.append(currentElement.val)
            currentElement = currentElement.next
        # end loop

        return list
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = RemoveNthNodeFromEndOfList()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        inputNode = self.__solution.listToNode([1, 2, 3, 4, 5])
        n = 2

        # act
        result = self.__solution.removeNthFromEnd(inputNode, n)
        result = self.__solution.nodeToList(result)

        # assert
        expect = [1, 2, 3, 5]
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        inputNode = self.__solution.listToNode([1])
        n = 1

        # act
        result = self.__solution.removeNthFromEnd(inputNode, n)
        result = self.__solution.nodeToList(result)

        # assert
        expect = None
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        inputNode = self.__solution.listToNode([1, 2])
        n = 1

        # act
        result = self.__solution.removeNthFromEnd(inputNode, n)
        result = self.__solution.nodeToList(result)

        # assert
        expect = [1]
        self.assertEqual(expect, result)
    # end def

    def test_case4(self):
        '''test case4'''
        # arrange
        inputNode = self.__solution.listToNode([1, 2, 3, 4, 5])
        n = 1

        # act
        result = self.__solution.removeNthFromEnd(inputNode, 5)
        result = self.__solution.nodeToList(result)

        # assert
        expect = [2, 3, 4, 5]
        self.assertEqual(expect, result)
    # end def

    def test_case5(self):
        '''test case5'''
        # arrange
        inputNode = self.__solution.listToNode([1, 2, 3, 4, 5])
        n = 1

        # act
        result = self.__solution.removeNthFromEnd(inputNode, n)
        result = self.__solution.nodeToList(result)

        # assert
        expect = [1, 2, 3, 4]
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
