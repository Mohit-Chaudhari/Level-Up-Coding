# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 25/07/21
# -----------------------------------------------

# ***** Rotate Matrix *****
# Problem Description
#
# You are given a n x n 2D matrix A representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# You need to do this in place.
#
# Note: If you end up using an additional array, you will only receive partial score.
#
#
#
# Problem Constraints
# 1 <= n <= 1000
#
#
#
# Input Format
# First argument is a 2D matrix A of integers
#
#
#
# Output Format
# Return the 2D rotated matrix.
#
#
#
# Example Input
# Input 1:
#
#  [
#     [1, 2],
#     [3, 4]
#  ]
# Input 2:
#
#  [
#     [1]
#  ]
#
#
# Example Output
# Output 1:
#
#  [
#     [3, 1],
#     [4, 2]
#  ]
# Output 2:
#
#  [
#     [1]
#  ]
#
#
# Example Explanation
# Explanation 1:
#
#  After rotating the matrix by 90 degree:
#  1 goes to 2, 2 goes to 4
#  4 goes to 3, 3 goes to 1
# Explanation 2:
#
#  2D array remains the same as there is only element.

class Solution:
    # @param A : list of list of integers
    def solve(self, A):

        ln = len(A)
        for i in range(ln//2):
            for j in range(i, ln - i - 1):
                temp = A[i][j]
                A[i][j] = A[ln - j - 1][i]
                A[ln - j - 1][i] = A[ln - i - 1][ln - j - 1]
                A[ln - i - 1][ln - j - 1] = A[j][ln - i - 1]
                A[j][ln - i - 1] = temp
        return A


s = Solution()
A = [
    [1, 2],
    [3, 4]
 ]
print(s.solve(A))
# [ [3, 1], [4, 2] ]
