# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 13/08/21
# -----------------------------------------------

# ***** Generate all Parentheses II *****
# Problem Description
#
# Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.
#
#
#
# Problem Constraints
# 1 <= A <= 20
#
#
#
# Input Format
# First and only argument is integer A.
#
#
#
# Output Format
# Return a sorted list of all possible paranthesis.
#
#
#
# Example Input
# Input 1:
#
# A = 3
# Input 2:
#
# A = 1
#
#
# Example Output
# Output 1:
#
# [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
# Output 2:
#
# [ "()" ]
#
#
# Example Explanation
# Explanation 1:
#
#  All paranthesis are given in the output list.
# Explanation 2:
#
#  All paranthesis are given in the output list.

class Solution:

    def __init__(self):
        self.answer = list()

    def generator(self, open_cnt, close_cnt, curr, n):

        # TERMINATION CONDITION
        if open_cnt > n or close_cnt > n:
            return

        # IF OPEN AND CLOSE COUNT IN EQUAL TO N THEN THE COMBINATION IS ONE OF THE ANSWER.
        if open_cnt == n and close_cnt == n:
            self.answer.append(curr)
            return

        if open_cnt < n:
            curr += "("
            self.generator(open_cnt+1, close_cnt, curr, n)
            curr = curr[:-1]

        if close_cnt < open_cnt:
            curr += ")"
            self.generator(open_cnt, close_cnt+1, curr, n)
            curr = curr[:-1]

        return

    def generateParenthesis(self, A):
        curr = ""
        self.generator(0, 0, curr, A)
        return self.answer


s = Solution()
print(s.generateParenthesis(3))
# OUTPUT: [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
