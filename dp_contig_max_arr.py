'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-100000]
Output: -100000
'''

# DP approach

def get_max_subarr(l):
    curr = l[0]
    maxi = l[0]
    for i in range(1,len(l)):
        if l[i] > curr+l[i]:
            start_index = i
            curr = l[i]
        else:
            curr += l[i]
        if curr > maxi:
            maxi = curr
            fin_index = i+1

        #curr = max(l[i],curr+l[i])
        #maxi = max(maxi,curr)
    return l[start_index:fin_index]

print(get_max_subarr([-2,1,-3,4,-1,2,1,-5,4]))