# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/08/21
# -----------------------------------------------

# ***** Min XOR value *****
# Problem Description
#
# Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value.
# Report the minimum XOR value.
#
#
#
# Problem Constraints
# 2 <= length of the array <= 100000
# 0 <= A[i] <= 109
#
#
#
# Input Format
# First and only argument of input contains an integer array A.
#
#
#
# Output Format
# Return a single integer denoting minimum xor value.
#
#
#
# Example Input
# Input 1:
#
#  A = [0, 2, 5, 7]
# Input 2:
#
#  A = [0, 4, 7, 9]
#
#
# Example Output
# Output 1:
#
#  2
# Output 2:
#
#  3
#
#
# Example Explanation
# Explanation 1:
#
#  0 xor 2 = 2

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        ln = len(A)
        A.sort()

        min = A[0] ^ A[1]
        for i in range(1, ln-1):
            if min > A[i] ^ A[i+1]:
                min = A[i] ^ A[i+1]

        return min


s = Solution()
print(s.findMinXor([0, 2, 5, 7]))
# OUTPUT: 2
