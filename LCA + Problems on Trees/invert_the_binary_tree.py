# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 29/09/21
# -----------------------------------------------

# ***** Invert the Binary Tree *****
# Problem Description
#
# Given a binary tree A, invert the binary tree and return it.
#
# Inverting refers to making left child as the right child and vice versa.
#
#
#
# Problem Constraints
# 1 <= size of tree <= 100000
#
#
#
# Input Format
# First and only argument is the head of the tree A.
#
#
#
# Output Format
# Return the head of the inverted tree.
#
# Example Input
# Input 1:
#
#      1
#    /   \
#   2     3
#
# Input 2:
#
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#
# Example Output
#
# Output 1:
#
#      1
#    /   \
#   3     2
#
# Output 2:
#
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4
#
# Example Explanation
# Explanation 1:
#
# Tree has been inverted.
# Explanation 2:
#
# Tree has been inverted.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, root):
        if root is None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.helper(root.left)
        self.helper(root.right)

    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        self.helper(root)

        return root


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
    print(node.invertTree(root))
