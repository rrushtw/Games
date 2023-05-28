import unittest


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None) -> None:
        self.val: int = int(x)
        self.next: Node = next
        self.random: Node = random
    # end def
# end class


class CopyListWithRandomPointer:
    def copyRandomList(self, head: Node) -> Node:
        resultList: list[Node] = list()
        nodeList: list[Node] = list()

        while head is not None:
            nodeList.append(head)

            temp: Node = Node(head.val)
            if head.random == None:
                temp.random = None
            resultList.append(temp)

            head = head.next
        # end loop

        for i in range(0, len(resultList)):
            currentNode = resultList[i]
            if i > 0:
                resultList[i - 1].next = currentNode

            if nodeList[i].random is None:
                continue
            
            for j in range(0, len(nodeList)):
                if nodeList[i].random == nodeList[j]:
                    currentNode.random = resultList[j]
                    break
            # end loop
        # end loop

        return resultList[0] if len(resultList) > 0 else None
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = CopyListWithRandomPointer()
    # end def

    def test_case1(self) -> None:
        '''test case 1'''
        # arrange
        # head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = Node(x=7, random=None)
        node1 = Node(x=13, random=head)
        head.next = node1
        node2 = Node(x=11)
        node1.next = node2
        node3 = Node(x=10, random=node2)
        node2.next = node3
        node4 = Node(x=1, random=head, next=None)
        node3.next = node4
        node2.random = node4

        # act
        result: Node = self.__solution.copyRandomList(head)

        # assert
        # output = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        self.assertFalse(result == head)

        while not (result is None and head is None):
            if (result is None and head is not None) or (result is not None and head is None):
                self.assertTrue(False)
                break

            # assert value
            self.assertEqual(head.val, result.val)
            # assert randome
            self.assertEqual(head.random is None, result.random is None)
            if head.random is not None and result.random is not None:
                self.assertEqual(head.random.val, result.random.val)

            result = result.next
            head = head.next
        # end loop
    # end def

    def test_case2(self) -> None:
        '''test case 2'''
        # arrange
        # head = [[1, 1], [2, 1]]
        head = Node(x=1)
        node1 = Node(x=3, next=None)
        node1.random = node1
        head.next = node1
        head.random = node1

        # act
        result: Node = self.__solution.copyRandomList(head)

        # assert
        # output = [[1, 1], [2, 1]]
        self.assertFalse(result == head)

        while not (result is None and head is None):
            if (result is None and head is not None) or (result is not None and head is None):
                self.assertTrue(False)
                break

            # assert value
            self.assertEqual(head.val, result.val)
            # assert randome
            self.assertEqual(head.random is None, result.random is None)
            if head.random is not None and result.random is not None:
                self.assertEqual(head.random.val, result.random.val)

            result = result.next
            head = head.next
        # end loop
    # end def

    def test_case3(self) -> None:
        '''test case 3'''
        # arrange
        # head = [[3, None], [3, 0], [3, None]]
        head = Node(x=3, random=None)
        node1 = Node(x=3, random=head)
        head.next = node1
        node2 = Node(x=3, random=None, next=None)
        node1.next = node2

        # act
        result: Node = self.__solution.copyRandomList(head)

        # assert
        # output = [[3, None], [3, 0], [3, None]]
        self.assertFalse(result == head)

        while not (result is None and head is None):
            if (result is None and head is not None) or (result is not None and head is None):
                self.assertTrue(False)
                break

            # assert value
            self.assertEqual(head.val, result.val)
            # assert randome
            self.assertEqual(head.random is None, result.random is None)
            if head.random is not None and result.random is not None:
                self.assertEqual(head.random.val, result.random.val)

            result = result.next
            head = head.next
        # end loop
    # end def

    def tearDown(self) -> None:
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
