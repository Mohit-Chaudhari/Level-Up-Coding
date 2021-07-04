# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 04/07/21
# -----------------------------------------------

# Smallest sequence with given Primes
# Problem Description
#
# Given three prime number(A, B, C) and an integer D.
# Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.
#
#
#
# Problem Constraints
# 1 <= A, B, C <= 10000
#
# 1 <= D <= 100000
#
#
#
# Input Format
# First argument is an integer A.
# Second argument is an integer B.
# Third argument is an integer C.
# Fourth argument is an integer D.
#
#
#
# Output Format
# Return an integer array of size D, denoting the first D integers described above.
#
# NOTE: The sequence should be sorted in ascending order
#
#
#
# Example Input
# Input 1:
#
#  A = 2
#  B = 3
#  C = 5
#  D = 5
# Input 2:
#
#  A = 3
#  B = 2
#  C = 7
#  D = 3
#
#
# Example Output
# Output 1:
#
#  [2, 3, 4, 5, 6]
# Output 2:
#
#  [2, 3, 4]
#
#
# Example Explanation
# Explanation 1:
#
#  4 = A * A ( 2 * 2 ), 6 = A * B ( 2 * 3 )
# Explanation 2:
#
#  2 has only prime factor 2. Similar 3 has only prime factor 3. 4 = A * A ( 2 * 2 )

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        lst = [1]
        prime = [A, B, C]
        cnt = 0
        i = 0
        Ai = 0
        Bi = 0
        Ci = 0

        while cnt < D:
            Amin = lst[Ai] * prime[0]
            Bmin = lst[Bi] * prime[1]
            Cmin = lst[Ci] * prime[2]
            mini = min(Amin, Bmin, Cmin)
            lst.append(mini)

            if mini == lst[Ai] * prime[0]:
                Ai += 1
            if mini == lst[Bi] * prime[1]:
                Bi += 1
            if mini == lst[Ci] * prime[2]:
                Ci += 1
            i += 1
            cnt += 1

        lst.pop(0)
        return lst


s = Solution()
print(s.solve(2, 3, 5, 5))