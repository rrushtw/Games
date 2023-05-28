import unittest
from ListNode import ListNode, ListNodeHelper


class ReverseLinkedList2:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        currentNode: ListNode = head
        nodeList: list[ListNode] = list()

        isLeftHead: bool = False
        previousNode: ListNode = ListNode(None)
        nextNode: ListNode = None
        i: int = 0
        while i < right and currentNode is not None:
            if i == left - 2:
                previousNode = currentNode

            if i == left - 1 and i == 0:
                isLeftHead = True

            if i >= left - 1:
                nodeList.append(currentNode)
            # else:
            i += 1
            currentNode = currentNode.next
        # end loop
        nextNode = currentNode

        nodeList.reverse()
        previousNode.next = nodeList[0]
        for i in range(1, len(nodeList)):
            nodeList[i - 1].next = nodeList[i]
        # end loop
        nodeList[-1].next = nextNode

        return head if not isLeftHead else previousNode.next
    # end def
# end def


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__listNodeHelper = ListNodeHelper()
        self.__solution = ReverseLinkedList2()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4,
                        next=ListNode(val=5, next=None)
                    )
                )
            )
        )

        # act
        result = self.__solution.reverseBetween(head, 2, 4)

        # assert
        expect = [1, 4, 3, 2, 5]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        head = ListNode(val=5, next=None)

        # act
        result = self.__solution.reverseBetween(head, 1, 1)

        # assert
        expect = [5]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4,
                        next=ListNode(val=5, next=None)
                    )
                )
            )
        )

        # act
        result = self.__solution.reverseBetween(head, 4, 5)

        # assert
        expect = [1, 2, 3, 5, 4]
        self.assertEqual(expect, self.__listNodeHelper.NodeToList(result))
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
