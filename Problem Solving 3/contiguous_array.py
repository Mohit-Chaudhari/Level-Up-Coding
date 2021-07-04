# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/07/21
# -----------------------------------------------

# Contiguous Array
# Given an array of integers A consisting of only 0 and 1.
#
# Find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
#
#
# Input Format
#
# The only argument given is the integer array A.
# Output Format
#
# Return the maximum length of a contiguous subarray with equal number of 0 and 1.
# Constraints
#
# 1 <= length of the array <= 100000
# 0 <= A[i] <= 1
# For Example
#
# Input 1:
#     A = [1, 0, 1, 0, 1]
# Output 1:
#     4
#     Explanation 1:
#         Subarray from index 0 to index 3 : [1, 0, 1, 0]
#         Subarray from index 1 to index 4 : [0, 1, 0, 1]
#         Both the subarrays have equal number of ones and equal number of zeroes.
#
# Input 2:
#     A = [1, 1, 1, 0]
# Output 2:
#     2

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        my_map = dict()
        s = 0
        longest_sub_array = 0

        for i in range(n):
            s = s + (-1 if A[i] == 0 else 1)
            if s == 0:
                if longest_sub_array < i + 1:
                    longest_sub_array = i + 1

            elif s in my_map.keys():
                if i - my_map[s] > longest_sub_array:
                    longest_sub_array = i - my_map[s]
            else:
                my_map[s] = i

        return longest_sub_array


s = Solution()
print(s.solve([1, 0, 1, 0, 1]))
# OUTPUT : 4
