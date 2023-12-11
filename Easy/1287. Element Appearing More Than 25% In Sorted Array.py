# 1287. Element Appearing More Than 25% In Sorted Array
# Easy
# Topics
# Companies
# Hint
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1
 
# Constraints:
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

# Solution
class Solution:
    def findSpecialInteger(self, arr): 
        n = len(arr)  # the length of the array
        threshold = n // 4  # the threshold of 25%

        i = 0
        while i < n:  # iterate through the array
            count = 1  # count the number of times the element appears
            while i + 1 < n and arr[i] == arr[i + 1]:  # check if the next element is the same as the current element
                count += 1  # increment the count
                i += 1  # increment the index

            if count > threshold:  # check if the count is greater than the threshold
                return arr[i]  # return the element immediately when threshold is exceeded

            i += 1  # increment the index for the outer loop

        return -1  # return -1 if no element exceeds the threshold
