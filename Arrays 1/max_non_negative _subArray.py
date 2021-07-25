# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 25/07/21
# -----------------------------------------------

# ***** Max Non Negative SubArray *****
# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
#
# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and
# skipping the third element is invalid.
#
# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
#
# Find and return the required subarray.
#
# NOTE:
#
#     1. If there is a tie, then compare with segment's length and return segment which has maximum length.
#     2. If there is still a tie, then return the segment with minimum starting index.
#
#
# Input Format:
#
# The first and the only argument of input contains an integer array A, of length N.
# Output Format:
#
# Return an array of integers, that is a subarray of A that satisfies the given conditions.
# Constraints:
#
# 1 <= N <= 1e5
# -INT_MAX < A[i] <= INT_MAX
# Examples:
#
# Input 1:
#     A = [1, 2, 5, -7, 2, 3]
#
# Output 1:
#     [1, 2, 5]
#
# Explanation 1:
#     The two sub-arrays are [1, 2, 5] [2, 3].
#     The answer is [1, 2, 5] as its sum is larger than [2, 3].
#
# Input 2:
#     A = [10, -1, 2, 3, -4, 100]
#
# Output 2:
#     [100]
#
# Explanation 2:
#     The three sub-arrays are [10], [2, 3], [100].
#     The answer is [100] as its sum is larger than the other two.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        ln = len(A)
        prefix = list()
        s = 0
        maxi = 0
        end_index = -1
        start_index = -1
        index = -float('inf')
        si = -1
        ei = -1

        # FIND PREFIX SUM ARRAY
        for i in range(ln):

            if A[i] >= 0:
                if s == -float('inf'):
                    s = 0
                s += A[i]
            else:
                s = -float('inf')

            if maxi < s:
                maxi = s

            prefix.append(s)

        for i in range(ln):
            if prefix[i] == maxi:
                end_index = i

            if start_index == -1:
                start_index = i

            if prefix[i] == -float('inf'):
                start_index = -1

            if start_index != -1 and end_index - start_index > index:
                si = start_index
                ei = end_index
                index = end_index - start_index

        return A[si:ei+1]


s = Solution()
print(s.maxset([6, -1, 3, 3, -2, 2, 2, 2]))
# OUTPUT: 2 2 2
