# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 02/06/22
# -----------------------------------------------

# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
#
# The frequency of a character in a string is the number of times it appears in the string.
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
#
# Example
# 1:
#
# Input: s = "aab"
# Output: 0
# Explanation: s is already
# good.
#
# Example 2:
#
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
#
# Example 3:
#
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
#
# Constraints:
#
# 1 <= s.length <= 105
# s contains only lowercase English letters.

# LINK: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def min_deletions(self, s: str) -> int:
        ans = 0
        d = {}
        for i in set(s):
            d[i] = s.count(i)
        # print(d)
        helper = set()
        # print(helper)
        print(d.values())
        for i in sorted(d.values(), reverse=True):
            print(i)
            while i in helper:
                # print(f"while i : {i}")
                i -= 1
                ans += 1
            if i:
                # print(f"If i : {i}")
                helper.add(i)
        # print(helper)
        return ans


if __name__ == "__main__":
    obj = Solution()
    s = "ceabaacb"
    print(obj.min_deletions(s))
