'''
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

def find_partitions(input):
    partitions = []
    for i in range(len(input)):
        if input[i] == 0:
           partitions.append(i)
        if i == 0:
            if input[i] <= 0 and input[i+1] > 0:
                partitions.append(i)
        elif i == len(input)-1:
            if input[i] <= 0 and input[i-1] > 0:
                partitions.append(i)
        else:
            if input[i] < 0 and input[i+1] > 0 and input[i-1] > 0:
                partitions.append(i)
    return partitions

def product(start,end,input):
    if start > end or start >= len(input) or end > len(input):
        return -float('inf')
    if start == end:
        return input[start]
    ans = 1
    for i in range(start,end):
        ans = ans*input[i]
    return ans

def all_neg(input):
    for item in input:
        if item >= 0:
            return False
    return True
    


def max_product(input):
    if all_neg(input):
        if len(input)%2 != 0:
            return max(product(0,len(input)-1,input), product(1,len(input),input))
        else:
            return(product(0,len(input),input))
    partitions = find_partitions(input)
    if len(partitions) == 0:
        return(product(0,len(input),input))
    maxx = []
    prev = 0
    for index in partitions:
        maxx.append(max_product(input[prev:index]))
        maxx.append(input[index])
        prev = index+1
    return max(maxx)
        
print(max_product([2,3,-2,4]))
print(max_product([-2,0,-1]))
print(max_product([2,3,-2,-10,0,4]))
print(max_product([-2,-3,-2,-10,0,-4]))
print(max_product([-2,-3,-2,-10,-10,-4]))

