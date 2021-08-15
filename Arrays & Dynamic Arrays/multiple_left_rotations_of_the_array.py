# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 15/08/21
# -----------------------------------------------

# ***** Multiple left rotations of the array *****
#
# Problem Description
#
# Given an array of integers A and multiple values in B which represents number of times
# array A needs to be left rotated.
#
# Find the rotated array for each value and return the result in the from of a matrix where i'th row represents the
# rotated array for the i'th value in B.
#
# Problem Constraints
#
# 1 <= length of both arrays <= 2000 -10^9 <= A[i] <= 10^9 0 <= B[i] <= 2000
#
# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer array B.
#
# Output Format
# Return the resultant matrix.
#
# Example
# Input
# Input
# 1:
#
# A = [1, 2, 3, 4, 5]
# B = [2, 3]
#
# Input
# 2:
#
# A = [5, 17, 100, 11]
# B = [1]
#
# Example Output
# Output
# 1:
#
# [[3, 4, 5, 1, 2]
#  [4, 5, 1, 2, 3]]
#
# Output
# 2:
#
# [[17, 100, 11, 5]]
#
# Example Explanation
# for input 1 -> B[0] = 2 which requires 2 times left rotations
#
# 1: [2, 3, 4, 5, 1]
#
# 2: [3, 4, 5, 1, 2]
#
# B[1] = 3 which requires 3 times left rotation
#
# 1: [2, 3, 4, 5, 1]
#
# 2: [3, 4, 5, 1, 2]
#
# 2: [4, 5, 1, 2, 4]

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        arr = list()
        ln = len(B)
        arr_ln = len(A)

        for i in range(ln):
            arr.append(A[B[i] % arr_ln:]+A[:B[i] % arr_ln])

        return arr


s = Solution()
print(s.solve([1, 2, 3, 4, 5], [2, 3]))
# OUTPUT: [ [3, 4, 5, 1, 2], [4, 5, 1, 2, 3] ]
