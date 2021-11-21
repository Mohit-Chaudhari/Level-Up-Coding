# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 21/11/21
# -----------------------------------------------

# ***** Longest Common Prefix *****
#
# Problem Description
#
# Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.
#
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
#
# For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".
#
#
#
# Problem Constraints
#
# 0 <= sum of length of all strings <= 1000000
#
#
#
# Input Format
#
# The only argument given is an array of strings A.
#
#
#
# Output Format
#
# Return the longest common prefix of all strings in A.
#
#
#
# Example Input
#
# Input 1:
#
# A = ["abcdefgh", "aefghijk", "abcefgh"]
# Input 2:
#
# A = ["abab", "ab", "abcd"];
#
#
# Example Output
#
# Output 1:
#
# "a"
# Output 2:
#
# "ab"
#
#
# Example Explanation
#
# Explanation 1:
#
# Longest common prefix of all the strings is "a".
# Explanation 2:
#
# Longest common prefix of all the strings is "ab".

class Solution:

    def commonPrefixUtil(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)

        result = ""

        # Compare str1 and str2
        j = 0
        i = 0
        while (i <= n1 - 1 and j <= n2 - 1):
            if (str1[i] != str2[j]):
                break
            result += (str1[i])

            i += 1
            j += 1

        return (result)

        # @param A : list of strings
        # @return a strings
    def longestCommonPrefix(self, A):
        n = len(A)

        A.sort(reverse=False)
        print(A)
        print(A[0], A[n-1])
        return self.commonPrefixUtil(A[0], A[n - 1])


if __name__ == "__main__":
    A = ["abcdefgh", "aefghijk", "abcefgh"]
    s = Solution()
    print(s.longestCommonPrefix(A))
