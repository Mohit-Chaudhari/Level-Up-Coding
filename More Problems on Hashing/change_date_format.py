# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 06/09/21
# -----------------------------------------------


# ***** Change Date Format *****
# Given a date string in the format Day Month Year, where:
#
# Day is in the set {"1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", ..., "29th", "30th", "31th"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the inclusive range [1900, 3000].
#
# Convert the date string to the format YYYY-MM-DD, where:
#
# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
# For example:
#
# 1st Mar 1984 → 1984-03-01
# 2nd Feb 2013 → 2013-02-02 4th Apr 1900 → 1900-04-04
#
#
#
# Input Format
#
# The only argument given is a String, a date in the above-mentioned format.
# Output Format
#
# Return a String, i.e date in YYYY-MM-DD format.
# Constraints
#
# The values of Day, Month, and Year are restricted to the value ranges specified above.
# The given dates are guaranteed to be valid, so no error handling is necessary.
# Sample Test 1
#
# Input:
#     A = "16th Mar 2068"
# Output:
#     2068-03-16
# Sample Test 2
#
# Input:
#     A = "6th Jun 1933"
# Output:
#     1933-06-06

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        arr = A.split()
        string = ""
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = {"1st": "01", "2nd": "02", "3rd": "03", "4th": "04", "5th": "05", "6th": "06", "7th": "07", "8th": "08", "9th": "09", "10th": "10", "11th": "11", "12th": "12", "13th": "13", "14th": "14", "15th": "15", "16th": "16", "17th": "17", "18th": "18", "19th": "19", "20th": "20", "21th": "21", "22th": "22", "23th": "23", "24th": "24", "25th": "25", "26th": "26", "27th": "27", "28th": "28", "29th": "29", "30th": "30", "31th": "31"}

        string += arr[2]
        string += "-" + month[arr[1]]
        string += "-" + day[arr[0]]

        return string


s = Solution()
print(s.solve("16th Mar 2068"))
# OUTPUT: 2068-03-16
