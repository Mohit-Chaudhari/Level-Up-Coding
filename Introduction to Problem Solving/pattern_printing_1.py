# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 17/07/21
# -----------------------------------------------

# ***** Pattern Printing -1 *****
# Problem Description
#
# Print a Pattern According to The Given Value of A.
#
# Example: For A = 3 pattern looks like:
#
# 1 0 0
#
# 1 2 0
#
# 1 2 3
#
# Print a Pattern According to The Given Value of A.
#
# Example: For A = 3 pattern looks like:
#
# 1 0 0
#
# 1 2 0
#
# 1 2 3
#
# Example Input
# Input 1:
#
#  A = 3
# Input 2:
#
#  A = 4
#
#
# Example Output
# Output :1
#
#  [
#    [1, 0, 0]
#    [1, 2, 0]
#    [1, 2, 3]
#  ]
# Output 2:
#
#  [
#    [1, 0, 0, 0]
#    [1, 2, 0, 0]
#    [1, 2, 3, 0]
#    [1, 2, 3, 4]
#  ]
#
# Example Explanation
# Explanation 2:
#
# For A = 4 pattern looks like:
#                              1 0 0 0
#                              1 2 0 0
#                              1 2 3 0
#                              1 2 3 4
#  So we will return it as two-dimensional array.

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        arr = [[0 for i in range(A)] for j in range(A)]

        for i in range(A):
            val = 1
            j = 0
            while j <= i:
                arr[i][j] = val
                j += 1
                val += 1

        return arr


s = Solution()
print(s.solve(3))
# OUTPUT: [[1, 0, 0], [1, 2, 0], [1, 2, 3]]
