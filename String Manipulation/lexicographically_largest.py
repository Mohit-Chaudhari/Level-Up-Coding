# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 19/07/21
# -----------------------------------------------

# ***** Lexicographically Largest *****
# You are given a string S. You want to change it to the lexicographically largest possible string by changing some of
# its characters. But you can only use characters of the string T as a replacement for characters of S. Formally,
# find the lexicographically largest string you can form by replacing some(or none) of the characters of S by using
# only the characters of string T. Note: Each character of T can be used at the most once.
#
# Constraints:
#
# 1.   1 <= Length of S and T <= 50
# 2.   All the alphabets of S and T are lower case (a - z)
# Input: A string A containing S and T separated by "_" character. (See example below)
#
# Output: Lexicographically largest string P that can be formed by changing some or (none) characters of S using the
# characters of T.
#
# Example:
#
# Input:
#
# A : "abb_c"
# This implies S is "abb" and T is "c".
#
# Output:
#
# P = "cbb"

class Solution:
    # @param A : string
    # @return a strings
    def getLargest(self, A):
        a = A.split("_")
        s = a[0]
        t = a[1]
        len_s = len(s)
        len_t = len(t)

        if len_s == 1 and len_t == 1:
            if ord(s) > ord(t):
                return s
            else:
                return t

        ord_t = [ord(t[i]) for i in range(len_t)]
        ord_t.sort(reverse=True)
        string = list(s)

        j = 0
        for i in range(len_s):
            if j > len_t-1:
                break
            if ord(s[i]) < ord_t[j]:
                string[i] = chr(ord_t[j])
                j += 1

        return "".join(string)


s = Solution()
print(s.getLargest("a_xyz"))
# OUTPUT: cbb
