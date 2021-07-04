# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/07/21
# -----------------------------------------------

# Subarray with least average
# Problem Description
#
# Given an array of size N, Find the subarray with least average of size k.
#
#
#
# Problem Constraints
# 1<=k<=N<=1e5
# -1e5<=A[i]<=1e5
#
#
# Input Format
# First argument contains an array A of integers of size N.
# Second argument contains integer k.
#
#
# Output Format
# Return the index of the first element of the subarray of size k that has least average.
# Array indexing starts from 0.
#
#
# Example Input
# Input 1:
# A=[3, 7, 90, 20, 10, 50, 40]
# B=1;
# Input 2:
#
# A=[3, 7, 5, 20, -10, 0, 12]
# B=2
#
#
# Example Output
# Output 1:
# 3
# Output 2:
#
# 4
#
#
# Example Explanation
# Explanation 1:
# Subarray between indexes 3 and 5
# The subarray {20, 10, 50} has the least average
# among all subarrays of size 3.
# Explanation 2:
#
#  Subarray between [4, 5] has minimum average

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        min = float('inf')
        min_index = -1
        s = 0
        temp = list()
        for i in range(n-B+1):
            if i == 0:
                temp = [A[i] for i in range(i, i+B)]
                s = sum(temp)
            else:
                poped = temp.pop(0)
                temp.append(A[i+B-1])
                s = s - poped + A[i+B-1]
            if s < min:
                min = s
                min_index = i

        return min_index


s = Solution()
s.solve([3, 7, 90, 20, 10, 50, 40], 1)
# OUTPUT: 3
