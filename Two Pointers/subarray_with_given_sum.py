# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/09/21
# -----------------------------------------------

# ***** Subarray with given sum *****
# Problem Description
#
# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
#
# If the answer does not exist return an array with a single element "-1".
#
# First sub-array means the sub-array for which starting index in minimum.
#
#
#
# Problem Constraints
# 1 <= length of the array <= 100000
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
# Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 4, 5]
#  B = 5
# Input 2:
#
#  A = [5, 10, 20, 100, 105]
#  B = 110
#
#
# Example Output
# Output 1:
#
#  [2, 3]
# Output 2:
#
#  -1
#
#
# Example Explanation
# Explanation 1:
#
#  [2, 3] sums up to 5.
# Explanation 2:
#
#  No subarray sums up to required number.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        j = 0
        s = 0

        while s != B and j < len(A):
            if A[j] == B:
                return [A[j]]
            if s < B:
                s += A[j]
                j += 1
            elif s > B:
                s -= A[i]
                i += 1
            elif s == B:
                break

        # print(s)
        if s == B:
            return A[i:j]
        else:
            return [-1]


s = Solution()
print(s.solve([1, 1000000000], 1000000000))
# OUTPUT: 1000000000
