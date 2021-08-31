# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 01/09/21
# -----------------------------------------------

# ***** Longest Consecutive Sequence *****
# Problem Description
#
# Given an unsorted integer array A of size N.
#
# Find the length of the longest set of consecutive elements from the array A.
#
#
#
# Problem Constraints
# 1 <= N <= 106
#
# -106 <= A[i] <= 106
#
#
#
# Input Format
# First argument is an integer array A of size N.
#
#
#
# Output Format
# Return an integer denoting the length of the longest set of consecutive elements from the array A.
#
#
#
# Example Input
# Input 1:
#
# A = [100, 4, 200, 1, 3, 2]
# Input 2:
#
# A = [2, 1]
#
#
# Example Output
# Output 1:
#
#  4
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  The set of consecutive elements will be [1, 2, 3, 4].
# Explanation 2:
#
#  The set of consecutive elements will be [1, 2].

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, arr):

        n = len(arr)
        ans = 0
        count = 0

        # Sort the array
        arr = sorted(arr)

        v = [arr[0]]

        # Insert repeated elements only
        # once in the vector
        for i in range(1, n):
            if arr[i] != arr[i - 1]:
                v.append(arr[i])

        # Find the maximum length
        # by traversing the array
        for i in range(len(v)):

            # Check if the current element is
            # equal to previous element +1
            if i > 0 and v[i] == v[i - 1] + 1:
                count += 1

            # Reset the count
            else:
                count = 1

            # Update the maximum
            ans = max(ans, count)

        return ans


s = Solution()
print(s.longestConsecutive([97, 86, 67, 19, 107, 9, 8, 49, 23, 46, -4, 22, 72, 4, 57, 111, 20, 52, 99, 2, 113, 81, 7, 5, 21, 0, 47, 54, 76, 117, -2, 102, 34, 12, 103, 69, 36, 51, 105, -3, 33, 91, 37, 11, 48, 106, 109, 45, 58, 77, 104, 60, 75, 90, 3, 62, 16, 119, 85, 63, 87, 43, 74, 13, 95, 94, 56, 28, 55, 66, 92, 79, 27, 42, 70]))
# print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
