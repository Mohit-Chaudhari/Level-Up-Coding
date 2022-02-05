# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 05/02/22
# -----------------------------------------------

# ***** Hotel Bookings Possible *****
#
# Problem Description
#
# A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms.
#
# Bookings contain an arrival date and a departure date.
#
# He wants to find out whether there are enough rooms in the hotel to satisfy the demand.
#
# Write a program that solves this problem in time O(N log N) .
#
#
#
# Problem Constraints
#
# 1 <= N <= 106
#
# 1 <= K <= 106
#
# 0 <= arrive[i] <= depart[i] <= 108
#
#
#
# Input Format
#
# First argument is an integer array named arrive denoting the arrival times of bookings.
#
# Second argument is an integer array named depart denoting the departure times of bookings.
#
# Third argument is an integer K which denotes count of rooms.
#
#
#
# Output Format
#
# A boolean which tells whether its possible to make a booking.
#
# Return 0/1 for C programs.
#
# O -> No there are not enough rooms for N booking.
#
# 1 -> Yes there are enough rooms for N booking.
#
#
#
# Example Input
#
# Input 1:
#
#  arrive = [1, 3, 5]
#  depart = [2, 6, 8]
#  K = 1
#
#
# Example Output
#
# Output 1:
#
#  False / 0
#
#
# Example Explanation
#
# Explanation 1:
#
#  At day = 5, there are 2 guests in the hotel. But hotel has only one room so it is not possible to take the booking
#  so we will return false or 0 for C Program.


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()

        i = 0
        j = 0
        plt = 0
        n = len(arrive)

        while i < n and j < n:
            if arrive[i] <= depart[j]:
                plt += 1
                i += 1
            elif arrive[i] > depart[j]:
                plt -= 1
                j += 1
            if plt > K:
                return 0

        return 1


if __name__ == "__main__":
    arrive = [1, 3, 5]
    depart = [2, 6, 8]
    K = 1
    s = Solution()
    print(s.hotel(arrive, depart, K))
    # OUTPUT : 0
