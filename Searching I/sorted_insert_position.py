# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 21/08/21
# -----------------------------------------------

# ***** Sorted Insert Position *****
# Problem Description
#
# Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.
#
#
#
# Problem Constraints
# 1 <= N <= 106
#
#
#
# Input Format
# First argument is an integer array A of size N.
# Second argument is an integer B.
#
#
#
# Output Format
# Return an integer denoting the index of target value.
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 5, 6]
#  B = 5
# Input 2:
#
# A = [1]
#  B = 1
#
#
# Example Output
# Output 1:
#
# 2
# Output 2:
#
# 0

# Example Explanation
# Explanation 1:
#
# The target value is present at index 2.
# Explanation 2:
#
# The target value is present at index 0.

class Solution:

    def helper(self, arr, start, end, key):
        pivot = (start + end) // 2

        a = arr[start:end+1]
        start_element = arr[start]
        end_element = arr[end]
        pivot_element = arr[pivot]

        if arr[pivot] == key:
            return pivot
        elif arr[start] <= key < arr[pivot]:
            return self.helper(arr, start, pivot - 1, key)
        elif arr[pivot] < key <= arr[end]:
            return self.helper(arr, pivot + 1, end, key)
        else:
            if start == end:
                if key > arr[pivot]:
                    return pivot + 1
                elif key < arr[pivot]:
                    return pivot

            if arr[start] > key:
                return start
            elif arr[end] < key:
                return end + 1

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        ln = len(A)

        if A[ln - 1] < B:
            return ln
        elif A[0] > B:
            return 0

        return self.helper(A, 0, ln - 1, B)


s = Solution()
A = [ 9, 12, 35, 39, 56, 60, 61, 67, 71, 76, 80, 83, 104, 115, 134, 138, 148, 157, 166, 182, 187, 191, 196, 209, 213, 214, 216, 231, 238, 243, 246, 254, 259, 270, 274, 278, 282, 286, 289, 291, 293, 296, 303, 322, 335, 338, 353, 356, 367, 368, 370, 372, 376, 393, 433, 448, 452, 455, 461, 470, 484, 519, 522, 530, 532, 542, 545, 573, 578, 584, 586, 606, 612, 617, 619, 630, 640, 651, 658, 662, 664, 666, 681, 686, 695, 700, 713, 714, 717, 749, 752, 757, 763, 765, 777, 780, 787, 789, 795, 808, 818, 824, 825, 829, 850, 864, 888, 898, 900, 905, 911, 918, 923, 924, 930, 935, 937, 943, 950, 956, 961, 964, 969, 977, 979, 981, 987, 989, 996, 1001 ]
print(s.searchInsert(A, 821))
# print(s.searchInsert([1, 3, 5, 6], 5))
# OUTPUT: 2
