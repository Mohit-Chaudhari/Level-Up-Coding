# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 12/08/21
# -----------------------------------------------

# SIXLETS
# Problem Description
#
# Given a array of integers A of size N and an integer B.
#
# Return number of non-empty subsequences of A of size B having sum <= 1000.
#
#
#
# Problem Constraints
# 1 <= N <= 20
#
# 1 <= A[i] <= 1000
#
# 1 <= B <= N
#
#
#
# Input Format
# The first argument given is the integer array A.
#
# The second argument given is the integer B.
#
#
#
# Output Format
# Return number of subsequences of A of size B having sum <= 1000.
#
#
#
# Example Input
# Input 1:
#
#     A = [1, 2, 8]
#     B = 2
# Input 2:
#
#     A = [5, 17, 1000, 11]
#     B = 4
#
#
# Example Output
# Output 1:
#
# 3
# Output 2:
#
# 0
#
#
# Example Explanation
# Explanation 1:
#
#  {1, 2}, {1, 8}, {2, 8}
# Explanation 1:
#
#  No valid subsequence

class Solution:

    def __init__(self):
        self.answer = 0

    def sixlets(self, arr, b, sum, cnt, idx):
        if sum > 10 ** 3:
            return
        if cnt == b:
            self.answer += 1
            return
        if idx == len(arr):
            return

        self.sixlets(arr, b, sum + arr[idx], cnt + 1, idx + 1)
        self.sixlets(arr, b, sum, cnt, idx + 1)

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        self.sixlets(A, B, 0, 0, 0)
        return self.answer


s = Solution()
print(s.solve([1, 2, 8], 2))
# OUTPUT: 3
