'''
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have EXACTLY one solution, and you may not
use the same element twice.

Example:

Nums = [2,7,11,15], tagert = 9
returns [0,1]
'''

def return_indicies(num_list, target):
    dic = {}
    for i in range(len(num_list)):
        complement = target - num_list[i]
        if complement in dic.keys():
            return[dic[complement], i]
        else:
            dic[num_list[i]] = i

print(return_indicies([2,7,11,15], 9))