# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 08/09/21
# -----------------------------------------------

# ***** Double Character Trouble *****
# Problem Description
#
# You are given a string A.
#
# An operation on the string is defined as follows:
#
# Remove the first occurrence of same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".
#
# Therefore the string after this operation will be "acd".
#
# Keep performing this operation on the string until there are no more occurrences of same consecutive characters and return the final string.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
#
#
# Input Format
# First and only argument is string A.
#
#
#
# Output Format
# Return the final string.
#
#
#
# Example Input
# Input 1:
#
#  A = abccbc
# Input 2:
#
#  A = ab
#
#
# Example Output
# Output 1:
#
#  "ac"
# Output 2:
#
#  "ab"
#
#
# Example Explanation
# Explanation 1:
#
# Remove the first occurrence of same consecutive characters. eg for a string "abbc", the first occurrence of same consecutive characters is "bb".
# Therefore the string after this operation will be "ac".
# Explanation 2:
#
#  No removals are to be done.


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, arr):
        lst = list()
        for i in arr:
            if lst:
                if lst[-1] == i:
                    lst.pop()
                else:
                    lst.append(i)
            else:
                lst.append(i)
        return "".join(lst)


s = Solution()
print(s.solve("abccbc"))
# OUTPUT: ac
