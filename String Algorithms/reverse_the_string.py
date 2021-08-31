# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 28/08/21
# -----------------------------------------------

# ***** Reverse the String *****
# Problem Description
#
# Given a string A of size N.
#
# Return the string A after reversing the string word by word.
#
# NOTE:
#
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
#
#
# Problem Constraints
# 1 <= N <= 3 * 105
#
#
#
# Input Format
# The only argument given is string A.
#
#
#
# Output Format
# Return the string A after reversing the string word by word.
#
#
#
# Example Input
# Input 1:
#     A = "the sky is blue"
# Input 2:
#     A = "this is ib"
#
#
# Example Output
# Output 1:
#     "blue is sky the"
# Output 2:
#     "ib is this"
#
#
# Example Explanation
# Explanation 1:
#     We reverse the string word by word so the string becomes "the sky is blue".
# Explanation 2:
#     We reverse the string word by word so the string becomes "this is ib".

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        arr = A.split()
        ln = len(arr)
        string = ""

        for i in range(ln):
            if i != 0:
                string += " " + arr[ln - i - 1]
            else:
                string += arr[ln - i - 1]

        return string


s = Solution()
print(s.solve("the sky is blue"))
# OUTPUT: "blue is sky the"
