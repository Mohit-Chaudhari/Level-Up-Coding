# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 27/09/21
# -----------------------------------------------

# ***** Sorted Array To Balanced BST *****
# Problem Description
#
# Given an array where elements are sorted in ascending order,
# convert it to a height Balanced Binary Search Tree (BBST).
#
# Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
# every node never differ by more than 1.
#
#
#
# Problem Constraints
# 1 <= length of array <= 100000
#
#
#
# Input Format
# First argument is an integer array A.
#
#
#
# Output Format
# Return a root node of the Binary Search Tree.
#
#
#
# Example Input
# Input 1:
#
# A : [1, 2, 3]
# Input 2:
#
# A : [1, 2, 3, 5, 10]
#
#
# Example Output
#
# Output 1:
#
#       2
#     /   \
#    1     3
#
# Output 2:
#
#       3
#     /   \
#    2     5
#   /       \
#  1         10
#
# Example Explanation
# Explanation 1:
#
#  You need to return the root node of the Binary Tree.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def attach_node(self, low, high, arr):
        if low > high:
            return None

        mid = (low + high) // 2
        node = TreeNode(arr[mid])

        node.left = self.attach_node(low, mid - 1, arr)
        node.right = self.attach_node(mid + 1, high, arr)

        return node

    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        return self.attach_node(0, len(A) - 1, A)

