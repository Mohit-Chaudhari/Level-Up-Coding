# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 27/09/21
# -----------------------------------------------

# ***** Largest BST Subtree *****
# Problem Description
#
# Given a Binary Tree A with N nodes.
#
# Write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST).
#
# If the complete Binary Tree is BST, then return the size of whole tree.
#
# NOTE:
#
# Largest subtree means subtree with most number of nodes.
#
#
# Problem Constraints
# 1 <= N <= 105
#
#
#
# Input Format
# First and only argument is an pointer to root of the binary tree A.
#
#
#
# Output Format
# Return an single integer denoting the size of the largest subtree which is also a BST.
#
#
#
# Example Input
#
# Input 1:
#     10
#     / \
#    5  15
#   / \   \
#  1   8   7
#
# Input 2:
#
#      5
#     / \
#    3   8
#   / \ / \
#  1  4 7  9
#
# Example Output
# Output 1:
#
#  3
# Output 2:
#
#  7
#
# Example Explanation
#
# Explanation 1:
#
# Largest BST subtree is
#                             5
#                            / \
#                           1   8
# Explanation 2:
#
#  Given binary tree itself is BST.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:

    # Recursive function to calculate the size of a given binary tree
    def size(self, root):

        # base case: empty tree has size 0
        if root is None:
            return 0

        # recursively calculate the size of the left and right subtrees and
        # return the sum of their sizes + 1 (for root node)
        return self.size(root.left) + 1 + self.size(root.right)

    # Recursive function to determine if a given binary tree is a BST or not
    # by keeping a valid range (starting from [-INFINITY, INFINITY]) and
    # keep shrinking it down for each node as we go down recursively
    def isBST(self, node, min, max):

        # base case
        if node is None:
            return True

        # if the node's value falls outside the valid range
        if node.val < min or node.val > max:
            return False

        # recursively check left and right subtrees with updated range
        return self.isBST(node.left, min, node.val) and self.isBST(node.right, node.val, max)

    # @param A : root node of tree
    # @return an integer
    def solve(self, root):

        if self.isBST(root, -float('inf'), float('inf')):
            return self.size(root)

        return max(self.solve(root.left), self.solve(root.right))

