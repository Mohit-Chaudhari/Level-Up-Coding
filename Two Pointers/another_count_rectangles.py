# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 26/08/21
# -----------------------------------------------

# ***** Another Count Rectangles *****
# Problem Description
#
# Given a sorted array of distinct integers A and an integer B,
# find and return how many rectangles with distinct configurations can be created using elements of this array as
# length and breadth whose area is lesser than B.
#
# (Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= A[i] <= 109
# 1 <= B <= 109
#
#
#
# Input Format
# The first argument given is the integer array A.
#
# The second argument given is integer B.
#
#
#
# Output Format
# Return the number of rectangles with distinct configurations with area less than B modulo (109 + 7).
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2]
#  B = 5
# Input 2:
#
#  A = [1, 2]
#  B = 1
#
#
# Example Output
# Output 1:
#
#  4
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  All 1X1, 2X2, 1X2 and 2X1 have area less than 5.
# Explanation 2:
#
#  No Rectangle is valid.

class Solution:

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = 1000000007
        ln = len(A)
        i = 0
        j = ln - 1
        cnt = 0

        while i < ln and j >= 0:

            ans = A[i] * A[j]

            if ans < B:
                cnt = (cnt % mod + (j + 1) % mod) % mod
                # cnt = (cnt + 2 * (i - j) + 1) % mod
                i += 1
            else:
                j -= 1

        return cnt % mod


s = Solution()
print(s.solve([1, 2, 4, 5], 5))
# OUTPUT: 6
