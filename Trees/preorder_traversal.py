# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 29/09/21
# -----------------------------------------------

# ***** Preorder Traversal *****
# Problem Description
#
# Given a binary tree, return the preorder traversal of its nodes values.
#
# NOTE: Using recursion is not allowed.
#
#
#
# Problem Constraints
# 1 <= number of nodes <= 105
#
#
#
# Input Format
# First and only argument is root node of the binary tree, A.
#
#
#
# Output Format
# Return an integer array denoting the preorder traversal of the given binary tree.
#
#
#
# Example Input
#
# Input 1:
#
#     1
#     \
#      2
#     /
#    3
#
# Input 2:
#
#    1
#   / \
#  6   2
#     /
#    3
#
# Example Output
# Output 1:
#
#  [1, 2, 3]
# Output 2:
#
#  [1, 6, 2, 3]
#
#
# Example Explanation
# Explanation 1:
#
#  The Preoder Traversal of the given tree is [1, 2, 3].
# Explanation 2:
#
#  The Preoder Traversal of the given tree is [1, 6, 2, 3].

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, root):

        stack = list()
        stack.append(root)
        arr = list()

        while stack:

            curr = stack.pop()

            arr.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return arr


if __name__ == '__main__':
    root = None

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
    print(node.preorderTraversal(root))
