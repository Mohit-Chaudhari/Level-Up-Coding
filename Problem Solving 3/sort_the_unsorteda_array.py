# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/07/21
# -----------------------------------------------

# Sort the Unsorted Array
# Problem Description
#
# You are given an integer array A having N integers.
#
# You have to find the minimum length subarray A[l..r] such that sorting this subarray makes the whole array sorted.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# -109 <= A[i] <= 109
#
#
#
# Input Format
# First and only argument is an integer array A.
#
#
#
# Output Format
# Return an integer denoting the minimum length.
#
#
#
# Example Input
# Input 1:
#
#  A = [0, 1, 15, 25, 6, 7, 30, 40, 50]
# Input 2:
#
#  A = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
#
#
# Example Output
# Output 1:
#
#  4
# Output 2:
#
#  6
#
#
# Example Explanation
# Explanation 1:
#
#  The smallest subarray to be sorted to make the whole array sorted =  A[3..6] i.e, subarray lying between positions 3 and 6.
# Explanation 2:
#
#  The smallest subarray to be sorted to make the whole array sorted =  A[4..9] i.e, subarray lying between positions 4 and 9.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        B = A.copy()
        B.sort()
        n = len(A)
        min = 0
        max = 0

        for i in range(n):
            if A[i] != B[i]:
                min = i
                break

        for i in range(n - 1, -1, -1):
            if A[i] != B[i]:
                max = i
                break

        if max == 0 and min == 0:
            return 0
        return max - min + 1


s = Solution()
print(s.solve([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))
# OUTPUT : 6
