# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 03/05/22
# -----------------------------------------------


def result(arr):
    print("\n")
    missing = list()
    duplicate = list()
    mapping = dict()

    for i in range(1, len(arr) + 1):
        mapping[i] = 0

    for element in arr:
        if element in mapping.keys():
            mapping[element] += 1
        else:
            mapping[element] = 1

    for i in mapping.keys():
        if mapping[i] == 0:
            missing.append(i)
        if mapping[i] > 1:
            duplicate.append(i)

    print("The missing elements is/are : ", missing)
    print("The duplicate elements is/are : ", duplicate)


if __name__ == "__main__":
    arr = [2, 2, 2, 2, 2, 2]
    result(arr)
    arr = [1, 1, 1, 1, 1, 1]
    result(arr)
    arr = [1, 2, 5, 6, 5, 4]
    result(arr)
    # vishal.s@smarter.codes

# LOGIC EXPLAINED:
# 1. Keep the keys in the mapping/ dictionary in the range of 1 to length of an array.
#    (Initially the values will the zero for each key)
# 2. Count the appearance of each element from the array in the dictionary.
# 3. Iterate and dictionary and check the count of appearance of and elements.
# 4. If we got 0 count then the number is missing in the array.
# 5. If we get count greater than 1 then it will be duplicate element

# HOW TO RUN THE CODE.
# 1. Open terminal.
# 2. Navigate to the file location.
# 3. Run command "python filename.py"

