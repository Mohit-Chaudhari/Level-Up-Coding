# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 23/09/21
# -----------------------------------------------

# ***** TOP VIEW *****
# Problem Description
#
# Given a binary tree of integers denoted by root A.
# Return an array of integers representing the top view of the Binary tree.
#
# Top view of a Binary Tree is a set of nodes visible when the tree is visited from top.
#
# Return the nodes in any order.
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
# Return an array, representing the top view of the binary tree.
#
#
#
# Example Input
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
#  [1, 2, 4, 8, 3, 7]
# Output 2:
#
#  [1, 2, 3]
#
#
# Example Explanation
# Explanation 1:
#
# Top view is described.
# Explanation 2:
#
# Top view is described.

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
        q.append((A, 0))
        mp = dict()

        while q:
            curr = q.pop(0)

            if curr[0].left:
                q.append((curr[0].left, curr[1] - 1))

            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))

            if curr[1] in mp.keys():
                mp[curr[1]].append(curr[0].val)
            else:
                mp[curr[1]] = [curr[0].val]

        ans = list()

        for dist in mp.keys():
            ans.append(mp[dist][0])

        return ans
