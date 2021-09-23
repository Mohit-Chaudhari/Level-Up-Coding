# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 23/09/21
# -----------------------------------------------

# ***** Vertical Order traversal *****
# Problem Description
#
# Given a binary tree, return a 2-D array with vertical order traversal of it.
# Go through the example and image for more details.
#
#
# NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
#
#
#
# Problem Constraints
# 0 <= number of nodes <= 105
#
#
#
# Input Format
# First and only arument is a pointer to the root node of binary tree, A.
#
#
#
# Output Format
# Return a 2D array denoting the vertical order traversal of tree as shown.
#
#
#
# Example Input
# Input 1:
#
#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9
# Input 2:
#
#       1
#     /   \
#    3     7
#   /       \
#  2         9
#
#
# Example Output
# Output 1:
#
#  [
#     [2],
#     [3],
#     [6, 5],
#     [7],
#     [9]
#  ]
# Output 2:
#
#  [
#     [2],
#     [3],
#     [1],
#     [7],
#     [9]
#  ]
#
#
# Example Explanation
# Explanation 1:
#
#  First row represent the verical line 1 and so on.

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):

        q = list()
        q.append((A, 0))

        mp = dict()

        while q:

            curr = q.pop(0)

            if curr[1] in mp.keys():
                mp[curr[1]].append(curr[0].val)
            else:
                mp[curr[1]] = [curr[0].val]

            if curr[0].left:
                q.append((curr[0].left, curr[1] - 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))

        ans = list()

        for dist in sorted(mp.keys()):
            ans.append(mp[dist])

        return ans
