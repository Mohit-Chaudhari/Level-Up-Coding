# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 14/08/21
# -----------------------------------------------

# ***** Kth Smallest Element *****
# Problem Description
#
# Find the Bth smallest element in given array A .
#
# NOTE: Users should try to solve it in <= B swaps.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# 1 <= B <= min(|A|, 500)
#
# 1 <= A[i] <= 109
#
#
#
# Input Format
# First argument is vector A.
#
# Second argument is integer B.
#
#
#
# Output Format
# Return the Bth smallest element in given array.
#
#
#
# Example Input
# Input 1:
#
# A = [2, 1, 4, 3, 2]
# B = 3
# Input 2:
#
# A = [1, 2]
# B = 2
#
#
# Example Output
# Output 1:
#
#  2
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  3rd element after sorting is 2.
# Explanation 2:
#
#  2nd element after sorting is 2.
import solutions as solutions


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = sorted(A)
        return A[B-1]


s = Solution()
print(s.kthsmallest([2, 1, 4, 3, 2], 3))
# OUTPUT: 2
