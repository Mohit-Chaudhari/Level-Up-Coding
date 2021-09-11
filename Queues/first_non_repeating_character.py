# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 11/09/21
# -----------------------------------------------

# ***** First non-repeating character *****
# Problem Description
#
# Given a string A denoting a stream of lowercase alphabets.
#
# You have to make new string B. B is formed such that we have to find first non-repeating character
# each time a character is inserted to the stream and append it at the end to B.
# if no non-repeating character is found then append '#' at the end of B.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
#
#
# Input Format
# The only argument given is string A.
#
#
#
# Output Format
# Return a string B after processing the stream of lowercase alphabets A.
#
#
#
# Example Input
# Input 1:
#
#  A = "abadbc"
# Input 2:
#
#  A = "abcabc"
#
#
# Example Output
# Output 1:
#
# "aabbdd"
# Output 2:
#
# "aaabc#"
#
#
# Example Explanation
# Explanation 1:
#
# "a"      -   first non repeating character 'a'
# "ab"     -   first non repeating character 'a'
# "aba"    -   first non repeating character 'b'
# "abad"   -   first non repeating character 'b'
# "abadb"  -   first non repeating character 'd'
# "abadbc" -   first non repeating character 'd'
# Explanation 2:
#
# "a"      -   first non repeating character 'a'
# "ab"     -   first non repeating character 'a'
# "abc"    -   first non repeating character 'a'
# "abca"   -   first non repeating character 'b'
# "abcab"  -   first non repeating character 'c'
# "abcabc" -   no non repeating character so '#'

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = list()
        mp = dict()
        ans = ""
        j = 0

        for i in A:
            # MAP FREQUENCY OF ELEMENTS.
            if i in mp.keys():
                mp[i] += 1
            else:
                mp[i] = 1

            q.append(i)
            while q and j < len(q) and mp[q[j]] > 1:
                j += 1

            if q and j < len(q):
                ans += q[j]
            else:
                ans += "#"

        return ans


s = Solution()
print(s.solve("xxikrwmjvsvckfrqxnibkcasompsuyuogauacjrr"))
# print(s.solve("abcabcdxx"))

# print(s.solve("abadbc"))
# OUTPUT: "aabbdd
