# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 06/07/21
# -----------------------------------------------

# Minimize the absolute difference
# Given three sorted arrays A, B and Cof not necessarily same sizes.
#
# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |.
#
# Example :
#
# Input:
#
# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
# Output:
#
# 1
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        # assigning the length -1 value
        # to each of three variables
        i = len(A) - 1
        j = len(B) - 1
        k = len(C) - 1

        # calculating min difference
        # from last index of lists
        min_diff = abs(max(A[i], B[j], C[k]) -
                       min(A[i], B[j], C[k]))

        while i != -1 and j != -1 and k != -1:
            current_diff = abs(max(A[i], B[j],
                                   C[k]) - min(A[i], B[j], C[k]))

            # checking condition
            if current_diff < min_diff:
                min_diff = current_diff

            # calculating max term from list
            max_term = max(A[i], B[j], C[k])

            # Moving to smaller value in the
            # array with maximum out of three.
            if A[i] == max_term:
                i -= 1
            elif B[j] == max_term:
                j -= 1
            else:
                k -= 1
        return min_diff


# driver code

A = [1, 4, 5, 8, 10]
B = [6, 9, 15]
C = [2, 3, 6, 6]
s = Solution()
print(s.solve(A, B, C))
