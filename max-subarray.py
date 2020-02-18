'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def max_finder(input):
    if len(input) == 0 or len(input) == 1:
        return input
    
    sum, min, local_max, jump = 0, 0, 0, 0
    min_index, prev_min = 0, -1
    for i in range(len(input)):

        sum += input[i]

        if sum < min:
            min = sum
            local_max = sum
            prev_min = min_index
            min_index = i

        if sum > local_max:
            local_max = sum

        if local_max - min > jump:
            jump = local_max - min
            max_index = i
    
    if max_index > min_index:
        subarray = input[min_index + 1: max_index + 1]
    else:
        subarray = input[prev_min + 1 : max_index + 1]

    return jump, subarray


print(max_finder([-2,1,-3,4,-1,2,1,-5,4]))
print(max_finder([1,-100,49,11,-1011,500]))

        
        
