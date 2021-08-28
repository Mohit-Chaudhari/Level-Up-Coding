# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 28/08/21
# -----------------------------------------------

# ***** Boring substring *****
# Problem Description
#
# Given a string A of lowercase English alphabets.
# Rearrange the characters of the given string A such that there is no boring substring in A.
#
# A boring substring has the following properties:
#
# Its length is 2.
# Both the characters are consecutive,
# for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then
# the next character can be either (C+1) or (C-1)).
# Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.
#
#
#
# Problem Constraints
# 1 <= |A| <= 105
#
#
#
# Input Format
# The only argument given is string A.
#
#
#
# Output Format
# Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.
#
#
#
# Example Input
# Input 1:
#
#  A ="abcd"
# Input 2:
#
#  A = "aab"
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
#  String A can be rearranged into "cadb" or "bdac"
# Explanation 2:
#
#  No arrangement of string A can make it free of boring substrings.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        odd = list()
        even = list()
        ln = len(A)

        for i in range(ln):
            if ord(A[i]) % 2 == 0:
                even.append(ord(A[i]))
            else:
                odd.append(ord(A[i]))

        even.sort()
        odd.sort()

        print(even)
        print(odd)

        even_ln = len(even)
        odd_ln = len(odd)

        if abs(odd[0] - even[even_ln - 1]) == 1 and abs(even[0] - odd[odd_ln - 1]) == 1:
            return 0
        return 1


s = Solution()
# print(s.solve("wwuvuw"))
print(s.solve("ajafafgja"))
# print(s.solve("abcd"))
# OUTPUT: 1
