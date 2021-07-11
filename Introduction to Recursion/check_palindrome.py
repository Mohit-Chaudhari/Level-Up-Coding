# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 11/07/21
# -----------------------------------------------


# ***** Check Palindrome *****
# Problem Description
#
# Write a recursive function that checks whether a string A is a palindrome or Not.
# Return 1 if the string A is palindrome, else return 0.
#
# Note: A palindrome is a string that's the same when reads forwards and backwards.
#
#
#
# Problem Constraints
# 1 <= A <= 50000
#
# String A consist only of lowercase letters.
#
#
#
# Input Format
# First and only argument is a string A.
#
#
#
# Output Format
# Return 1 if the string A is palindrome, else return 0.
#
#
#
# Example Input
# Input 1:
#
#  A = "naman"
# Input 2:
#
#  A = "strings"
#
#
# Example Output
# Output 1:
#
#  1
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  "naman" is a palindomic string, so return 1.
# Explanation 2:
#
#  "strings" is not a palindrome, so return 0.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        Flag = 1
        for i in range(int(n/2)):
            if A[n-i-1] != A[i]:
                return 0
        return Flag


s = Solution()
print(s.solve("naman"))
# OUTPUT: 1
