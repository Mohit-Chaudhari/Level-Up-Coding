# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 04/08/21
# -----------------------------------------------


# ***** Permutations of A in B *****
# Problem Description
#
# You are given two strings A and B of size N and M respectively.
#
# You have to find the count of all permutations of A present in B as a substring.
# You can assume a string will have only lowercase letters.
#
#
#
# Problem Constraints
# 1 <= N < M <= 105
#
#
#
# Input Format
# Given two argument, A and B of type String.
#
#
#
# Output Format
# Return a single Integer, i.e number of permutations of A present in B as a substring.
#
#
#
# Example Input
# Input 1:
#
#  A = "abc"
#  B = "abcbacabc"
# Input 2:
#
#  A = "aca"
#  B = "acaa"
#
#
# Example Output
# Output 1:
#
#  5
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  Permutations of A that are present in B as substring are:
#     1. abc
#     2. cba
#     3. bac
#     4. cab
#     5. abc
#     So ans is 5.
# Explanation 2:
#
#  Permutations of A that are present in B as substring are:
#     1. aca
#     2. caa

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        len_a = len(A)
        len_b = len(B)
        a_map = dict()
        b_map = dict()
        cnt = 0

        for i in range(len_a):
            if A[i] in a_map.keys():
                a_map[A[i]] = a_map[A[i]] + 1
            else:
                a_map[A[i]] = 1

        for i in range(len_b - len_a + 1):
            # print(i)
            if i == 0:
                for j in range(len_b - (len_b - len_a)):
                    if B[j] in b_map.keys():
                        b_map[B[j]] = b_map[B[j]] + 1
                    else:
                        b_map[B[j]] = 1
                print(b_map)
            else:
                if b_map[B[i-1]] != 0:
                    b_map[B[i-1]] = b_map[B[i-1]] - 1
                    if b_map[B[i-1]] == 0:
                        del b_map[B[i-1]]

                if B[i + len_a - 1] in b_map.keys():
                    b_map[B[i + len_a - 1]] = b_map[B[i + len_a - 1]] + 1
                else:
                    b_map[B[i + len_a - 1]] = 1
                print(b_map)
            if a_map == b_map:
                cnt += 1

        return cnt


s = Solution()
print(s.solve("p", "pccdpeeooadeocdoacddapacaecb"))
# print(s.solve("abc", "abcbacabc"))
# OUTPUT: 5
