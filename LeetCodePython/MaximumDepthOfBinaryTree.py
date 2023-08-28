import unittest
from TreeNode import TreeNode


class MaxDepth:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        # else:
        depthLeft: int = 0 if root.left is None else self.maxDepth(root.left)
        depthRight: int = 0 if root.right is None else self.maxDepth(root.right)

        return depthLeft + 1 if depthLeft > depthRight else depthRight + 1
    # end def
# end class


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.__solution = MaxDepth()
    # end def

    def test_case1(self) -> None:
        '''test case1'''
        # arrange
        root = TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(
                20,
                left=TreeNode(15),
                right=TreeNode(7)
            )
        )

        # act
        result = self.__solution.maxDepth(root)

        # assert
        expect = 3
        self.assertEqual(expect, result)
    # end def

    def test_case2(self) -> None:
        '''test case2'''
        # arrange
        root = TreeNode(
            1,
            left=None,
            right=TreeNode(2)
        )

        # act
        result = self.__solution.maxDepth(root)

        # assert
        expect = 2
        self.assertEqual(expect, result)
    # end def

    def test_case3(self) -> None:
        '''test case3'''
        # arrange
        root = None

        # act
        result = self.__solution.maxDepth(root) # type: ignore

        # assert
        expect = 0
        self.assertEqual(expect, result)
    # end def

    def tearDown(self) -> None:
        return super().tearDown()
    # end def
# end class

if __name__ == '__main__':
    unittest.main()