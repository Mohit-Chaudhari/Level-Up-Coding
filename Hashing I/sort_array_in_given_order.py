# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 31/08/21
# -----------------------------------------------

# ***** Sort Array in given Order *****
# Problem Description
#
# Given two array of integers A and B,
# Sort A in such a way that the relative order among the elements will be the same as those are in B.
# For the elements not present in B, append them at last in sorted order.
#
# Return the array A after sorting from the above method.
#
# NOTE: Elements of B are unique.
#
#
#
# Problem Constraints
# 1 <= length of the array A <= 100000
#
# 1 <= length of the array B <= 100000
#
# -10^9 <= A[i] <= 10^9
#
#
#
# Input Format
# The first argument given is the integer array A.
#
# The second argument given is the integer array B.
#
#
#
# Output Format
# Return the array A after sorting as described.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, 5]
# B = [5, 4, 2]
# Input 2:
#
# A = [5, 17, 100, 11]
# B = [1, 100]
#
#
# Example Output
# Output 1:
#
# [5, 4, 2, 1, 3]
# Output 2:
#
# [100, 5, 11, 17]
#
#
# Example Explanation
# Explanation 1:
#
#  Simply sort as described.
# Explanation 2:
#
#  Simply sort as described

class Solution:

    def first(self, arr, low, high, x, n):
        if high >= low:
            mid = low + (high - low) // 2  # (low + high)/2;
            if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
                return mid
            if x > arr[mid]:
                return self.first(arr, (mid + 1), high, x, n)
            return self.first(arr, low, (mid - 1), x, n)

        return -1

    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A1, A2):
        m = len(A1)
        n = len(A2)
        temp = [0] * m
        visited = [0] * m

        for i in range(0, m):
            temp[i] = A1[i]
            visited[i] = 0

        # Sort elements in temp
        temp.sort()

        # for index of output which is sorted A1[]
        ind = 0

        """Consider all elements of A2[], find
        them in temp[] and copy to A1[] in order."""
        for i in range(0, n):

            # Find index of the first occurrence
            # of A2[i] in temp
            f = self.first(temp, 0, m - 1, A2[i], m)

            # If not present, no need to proceed
            if f == -1:
                continue

            # Copy all occurrences of A2[i] to A1[]
            j = f
            while j < m and temp[j] == A2[i]:
                A1[ind] = temp[j]
                ind = ind + 1
                visited[j] = 1
                j = j + 1

        # Now copy all items of temp[] which are
        # not present in A2[]
        for i in range(0, m):
            if visited[i] == 0:
                A1[ind] = temp[i]
                ind = ind + 1

        return A1


s = Solution()
print(s.solve([10, 2, 18, 16, 16, 16], [3, 13, 2, 16, 4, 19]))  # 2 16 16 16 10 18
# print(s.solve([1, 2, 3, 4, 5], [5, 4, 2]))
# OUTPUT: [5, 4, 2, 1, 3]
