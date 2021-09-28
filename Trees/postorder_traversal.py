# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 28/09/21
# -----------------------------------------------

# ***** Postorder Traversal *****
# Problem Description
#
# Given a binary tree, return the Postorder traversal of its nodes values.
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
# Return an integer array denoting the Postorder traversal of the given binary tree.
#
#
#
# Example Input
#
# Input 1:
#    1
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
#  [3, 2, 1]
# Output 2:
#
#  [6, 3, 2, 1]
#
#
# Example Explanation
# Explanation 1:
#
#  The Preoder Traversal of the given tree is [3, 2, 1].
# Explanation 2:
#
#  The Preoder Traversal of the given tree is [6, 3, 2, 1].

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, root):

        stack = list()
        arr = list()

        while root is not None:

            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        while stack:

            if root is not None:

                while root is not None:

                    if root.right is not None:
                        stack.append(root.right)
                    stack.append(root)
                    root = root.left

            # IF STACK IS NOT EMPTY
            else:
                root = stack.pop()

                if stack and root.right is not None and root.right == stack[-1]:
                    temp = stack.pop()
                    stack.append(root)
                    root = temp
                else:
                    arr.append(root.val)
                    root = None

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
    print(node.postorderTraversal(root))

