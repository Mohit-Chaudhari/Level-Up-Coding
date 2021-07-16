# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 12/07/21
# -----------------------------------------------

# ***** Special Subsequences "AG" *****
# Problem Description
#
# You have given a string A having Uppercase English letters.
#
# You have to find that how many times subsequence "AG" is there in the given string.
#
# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
#
#
#
# Problem Constraints
# 1 <= length(A) <= 105
#
#
#
# Input Format
# First and only argument is a string A.
#
#
#
# Output Format
# Return an integer denoting the answer.
#
#
#
# Example Input
# Input 1:
#
#  A = "ABCGAG"
# Input 2:
#
#  A = "GAB"
#
#
# Example Output
# Output 1:
#
#  3
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  Subsequence "AG" is 3 times in given string
# Explanation 2:
#
#  There is no subsequence "AG" in the given string.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        cntA = 0
        cntG = 0

        for i in reversed(A):
            if i == "G":
                cntG += 1
            if i == "A":
                cntA += cntG
        return cntA


s = Solution()
print(s.solve("GUGPUAGAFQBMPYAGGAAOALAELGGGAOGLGEGZ"))
# OUTPUT: 52
