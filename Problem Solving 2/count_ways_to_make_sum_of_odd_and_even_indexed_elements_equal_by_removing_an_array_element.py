# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/07/21
# -----------------------------------------------

# Count ways to make sum of odd and even indexed elements equal by removing an array element
# Problem Description
#
# Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
#
#
#
# Problem Constraints
# 1<=n<=1e5
# -1e5<=A[i]<=1e5
#
#
# Input Format
# First argument contains an array A of integers of size N
#
#
# Output Format
# Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
#
#
#
# Example Input
# Input 1:
# A=[2, 1, 6, 4]
# Input 2:
#
# A=[1, 1, 1]
#
#
# Example Output
# Output 1:
# 1
# Output 2:
#
# 3
#
#
# Example Explanation
# Explanation 1:
# Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
# Therefore, the required output is 1.
# Explanation 2:
#
#  Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Therefore, the required output is 3.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # INITIALISING VARIABLES
        opre = list()
        epre = list()
        oddpresum = list()
        evenpresum = list()
        esum = 0
        osum = 0
        cnt = 0
        n = len(A)

        # FINDING EVEN PREFIX SUM AND ODD PREFIX SUM ARRAY
        for i in range(n):
            if i % 2 == 0:
                epre.append(A[i])
                opre.append(0)
            else:
                epre.append(0)
                opre.append(A[i])
            esum += epre[i]
            osum += opre[i]
            evenpresum.append(esum)
            oddpresum.append(osum)

        # CALCULATING THE INDEX COUNT
        for i in range(n):
            oddsum = esum - evenpresum[i] + oddpresum[i - 1]
            evensum = osum - oddpresum[i] + evenpresum[i - 1]
            if oddsum == evensum:
                cnt += 1

        # RETURNING THE COUNT
        return cnt


s = Solution()
print(s.solve([2, 1, 6, 4]))
# OUTPUT: 1
