# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 14/08/21
# -----------------------------------------------

# ***** Merge Two Sorted Arrays *****
# Problem Description
#
# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.
#
#
#
# Problem Constraints
# -1010 <= A[i],B[i] <= 1010
#
#
#
# Input Format
# First Argument is a 1-D array representing A.
#
# Second Argument is also a 1-D array representing B.
#
#
#
# Output Format
# Return a 1-D vector which you got after merging A and B.
#
#
#
# Example Input
# Input 1:
#
# A = [4, 7, 9 ]
# B = [2 ,11, 19 ]
# Input 2:
#
# A = [1]
# B = [2]
#
#
# Example Output
# Output 1:
#
# [2, 4, 7, 9, 11, 19]
# Output 2:
#
# [1, 2]
#
#
# Example Explanation
# Explanation 1:
#
# Merging A and B produces the output as described above.
# Explanation 2:
#
#  Merging A and B produces the output as described above.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        a_ln = len(A)
        b_ln = len(B)
        ln = max(a_ln, b_ln)
        i = 0
        j = 0
        arr = list()

        while i < ln and j < ln:
            if A[i] < B[j]:
                arr.append(A[i])
                i += 1
            else:
                arr.append(B[j])
                j += 1

        if a_ln != i:
            arr += A[i:]
        if b_ln != j:
            arr += B[j:]
        return arr


s = Solution()
print(s.solve([4, 7, 9], [2, 11, 19]))
# OUTPUT: [2, 4, 7, 9, 11, 19]
