# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 23/07/21
# -----------------------------------------------

# ***** Count Occurrences *****
# Problem Description
#
# Find number of occurrences of bob in the string A consisting of lowercase english alphabets.
#
#
#
# Problem Constraints
# 1 <= |A| <= 1000
#
#
# Input Format
# The first and only argument contains the string A consisting of lowercase english alphabets.
#
#
# Output Format
# Return an integer containing the answer.
#
#
# Example Input
# Input 1:
#
#   "abobc"
# Input 2:
#
#   "bobob"
#
#
# Example Output
# Output 1:
#
#   1
# Output 2:
#
#   2
#
#
# Example Explanation
# Explanation 1:
#
#   The only occurrence is at second position.
# Explanation 2:
#
#   Bob occures at first and third position.
import re


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        # This is alternative method using regex
        # return len(re.findall("(?=bob)", A))

        sb = "bob"
        cnt = 0
        ln = len(A)
        sbln = len(sb)
        for i in range(ln):
            if A[i:i+sbln] == "bob":
                cnt += 1
        return cnt


s = Solution()
print(s.solve("bobob"))
# OUTPUT: 2
