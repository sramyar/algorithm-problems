'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

def find_index(input, target, first, last):
    i = (first+last)//2
    zcounter = 0
    while zcounter < 2:
        if target < input[i]:
            i = (i + first)//2
            if i == first : zcounter += 1
        elif target > input[i]:
            i = (i + last + 1)//2
            if i == last : zcounter += 1
        else:
            return i
    return -1

def check_pivot(input, index):
    if index - 1 >= 0 and index + 1 <= len(input) - 1:
        return not (input[index] > input[index - 1] 
                and input[index] <= input[index + 1])
    else:
        return False


def find_pivot(input):
    i = len(input)//2
    j = i
    while True:
        if check_pivot(input,i):
            return i+1
        else:
            i = i//2
            if check_pivot(input,i):
                return i+1
            j = (i+len(input))//2
            if check_pivot(input,j):
                return j+1

def find_rotated(input,target):
    p = find_pivot(input)
    
    upper = find_index(input,target,p,len(input)-1)
    lower = find_index(input,target,0,p)

    if upper != -1:
        return upper
    elif lower != -1:
        return lower
    else:
        return -1

print(find_rotated([4,5,6,7,0,1,2],0))
print(find_rotated([4,5,6,7,0,1,2],3))
