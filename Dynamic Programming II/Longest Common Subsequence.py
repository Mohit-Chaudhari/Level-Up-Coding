# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 22/11/21
# -----------------------------------------------

# ***** Longest Common Subsequence *****
#
# Problem Description
#
# Given two strings A and B. Find the longest common subsequence
# ( A sequence which does not need to be contiguous), which is common in both the strings.
#
# You need to return the length of such longest common subsequence.
#
#
#
# Problem Constraints
#
# 1 <= Length of A, B <= 1005
#
#
#
# Input Format
#
# First argument is a string A.
# Second argument is a string B.
#
#
#
# Output Format
#
# Return an integer denoting the length of the longest common subsequence.
#
#
#
# Example Input
#
# Input 1:
#
#  A = "abbcdgf"
#  B = "bbadcgf"
# Input 2:
#
#  A = "aaaaaa"
#  B = "ababab"
#
#
# Example Output
#
# Output 1:
#
#  5
# Output 2:
#
#  3
#
#
# Example Explanation
#
# Explanation 1:
#
#  The longest common subsequence is "bbcgf", which has a length of 5.
# Explanation 2:
#
#  The longest common subsequence is "aaa", which has a length of 3.

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, X, Y):
        # find the length of the strings
        m = len(X)
        n = len(Y)

        # declaring the array for storing the dp values
        L = [[None] * (n + 1) for i in range(m + 1)]
        print(L)

        """Following steps build L[m + 1][n + 1] in bottom up fashion
        Note: L[i][j] contains length of LCS of X[0..i-1]
        and Y[0..j-1]"""
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        print(L)
        return L[m][n]


if __name__ == "__main__":
    A = "abbcdgf"
    B = "bbadcgf"
    s = Solution()
    print(s.solve(A, B))
