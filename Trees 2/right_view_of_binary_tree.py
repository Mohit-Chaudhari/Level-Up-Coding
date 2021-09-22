# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 23/09/21
# -----------------------------------------------

# ***** Right view of Binary tree *****
# Problem Description
#
# Given a binary tree of integers denoted by root A.
# Return an array of integers representing the right view of the Binary tree.
#
# Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.
#
#
#
# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000
#
# 0 <= node values <= 10^9
#
#
#
# Input Format
# First and only argument is head of the binary tree A.
#
#
#
# Output Format
# Return an array, representing the right view of the binary tree.
#
# Example Input
#
# Input 1:
#
#             1
#           /   \
#          2    3
#         / \  / \
#        4   5 6  7
#       /
#      8
#
# Input 2:
#
#             1
#            /  \
#           2    3
#            \
#             4
#              \
#               5
#
# Example Output
# Output 1:
#
#  [1, 3, 7, 8]
# Output 2:
#
#  [1, 3, 4, 5]
#
#
# Example Explanation
# Explanation 1:
#
# Right view is described.
# Explanation 2:
#
# Right view is described.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):

        q = list()
        q.append(A)
        ans = list()

        while q:

            count = len(q)
            level = list()

            while count > 0:

                temp = q.pop(0)
                level.append(temp.val)

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)

                count -= 1
            ans.append(level[-1])
        return ans
