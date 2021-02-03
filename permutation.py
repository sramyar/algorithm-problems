'''

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

'''

def permutate(nums):
    ans = []
    def backtrack(taken=[],left=[i for i in range(len(nums))]):
        if len(taken)==len(nums):
            ans.append([nums[i] for i in taken])
        else:
            for i in left:
                backtrack(taken+[i],[x for x in left if x != i])
        
    backtrack()
    return ans

print(permutate([1,2,3]))
print(permutate([0,1]))
print(permutate([1]))
