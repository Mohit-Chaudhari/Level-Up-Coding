# ***** Recover Binary Search Tree *****
# Problem Description
# Two elements of a binary search tree (BST),represented by root A are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.
#
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#
#
#
# Problem Constraints
# 1 <= size of tree <= 100000
#
#
#
# Input Format
# First and only argument is the head of the tree,A
#
#
#
# Output Format
# Return the 2 elements which need to be swapped.
#
#
#
# Example Input
#
# Input 1:
#
#          1
#         / \
#        2   3
#
# Input 2:
#
#          2
#         / \
#        3   1
#
# Example Output
# Output 1:
#
#  [2, 1]
# Output 2:
#
#  [3, 1]
#
# Example Explanation
#
# Explanation 1:
#
# Swapping 1 and 2 will change the BST to be
#          2
#         / \
#        1   3
# which is a valid BST
#
# Explanation 2:
#
# Swapping 1 and 3 will change the BST to be
#          2
#         / \
#        1   3
# which is a valid BST


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prevEle = TreeNode(-float('inf'))
        self.firstEle = None
        self.secondEle = None

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)

        if not self.firstEle and (root.val < self.prevEle.val):
            self.firstEle = self.prevEle
        if self.firstEle and (root.val < self.prevEle.val):
            self.secondEle = root

        self.prevEle = root
        self.inOrder(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.inOrder(root)
        if not self.firstEle or not self.secondEle:
            return
        self.firstEle.val, self.secondEle.val = self.secondEle.val, self.firstEle.val
        return [self.firstEle.val, self.secondEle.val]


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    node = Solution()
    print(node.recoverTree(root))
    # OUTPUT: [3, 4]
