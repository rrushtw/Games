# from FolderName.FileName import ClassName
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right
    # end def
# end class


class LongestZigZag:
    def __init__(self) -> None:
        self.__maxLength = 0
    # end def

    def longestZigZag(self, root: TreeNode) -> int:
        self.getCount(root, 0, None)

        return self.__maxLength
    # end def

    def getCount(self, node: TreeNode, currentLength: int, direction) -> None:
        self.__maxLength = max(self.__maxLength, currentLength)

        if node.left is not None:
            if direction == 'left':
                self.getCount(node.left, 1, 'left')
            else:
                self.getCount(node.left, currentLength + 1, 'left')

        if node.right is not None:
            if direction == 'right':
                self.getCount(node.right, 1, 'right')
            else:
                self.getCount(node.right, currentLength + 1, 'right')

        return
    # end def

    def listToNode(self, inputs: list[int]) -> TreeNode:
        root = TreeNode(inputs[0])

        queue: list[TreeNode] = []

        queue = [root]  # giving the first element - root
        inputs = inputs[1:]  # remove the first element

        while len(inputs) > 0:
            node = queue[0]

            # handle the left node
            # if len(inputs) == 0:
            #     break
            # else:
            node.left = TreeNode(inputs[0]) if inputs[0] is not None else None
            inputs = inputs[1:]
            if node.left is not None:
                queue.append(node.left)

            # handle the right node
            if len(inputs) == 0:
                break
            # else:
            node.right = TreeNode(inputs[0]) if inputs[0] is not None else None
            inputs = inputs[1:]
            if node.right is not None:
                queue.append(node.right)

            queue = queue[1:]
        # end loop

        return root
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__solution = LongestZigZag()
    # end def

    def test_case1(self):
        '''test case1'''
        # arrange
        array = [1, None, 1, 1, 1, None, None, 1, 1,
                 None, 1, None, None, None, 1, None, 1]
        root = self.__solution.listToNode(array)

        # act
        result = self.__solution.longestZigZag(root)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self):
        '''test case2'''
        # arrange
        array = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
        root = self.__solution.listToNode(array)

        # act
        result = self.__solution.longestZigZag(root)

        # assert
        expect = 4
        self.assertEqual(expect, result)
    # end def

    def test_case3(self):
        '''test case3'''
        # arrange
        array = [1]
        root = self.__solution.listToNode(array)

        # act
        result = self.__solution.longestZigZag(root)

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def tearDown(self):
        pass
    # end def
# end class


if __name__ == "__main__":
    unittest.main()
