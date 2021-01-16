
"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);


"""

import random

def random_indx(nums,x):
    idx={}
    for i in range(len(nums)):
        if nums[i] not in idx:
            idx[nums[i]] = [i]
        else:
            idx[nums[i]].append(i)
    index = random.randint(0,len(idx[x])-1)
    return idx[x][index]

freqs={2:0,3:0,4:0}
n=1000000
for i in range(n):
    i = random_indx([1,2,3,3,3],3)
    if i==2:
        freqs[2]+=1/n
    elif i==3:
        freqs[3]+=1/n
    else:
        freqs[4]+=1/n

print(freqs)
    