'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is
    greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

def sort_merge(nums1, nums2, m, n):
    merge = []
    i = 0
    j= 0
    while True:
        if nums2[j] < nums1[i]:
            merge.append(nums2[j])
            if j < n - 1:
                j += 1
            else:
                merge += nums1[i:m]
                break

        else:
            merge.append(nums1[i])
            if i < m - 1:
                i += 1
            else:
                merge += nums2[j:n]
                break

    for i in range(len(merge)):
        nums1[i] = merge[i]
    
    return nums1




print(sort_merge([1,2,3,0,0,0],[2,5,6],3,3))
print(sort_merge([1,2,3,0,0,0],[2,5],3,2))
print(sort_merge([10,20,30,0,0,0],[10,20,30],3,3))
print(sort_merge([1,20,30,0,0,0],[2,5],3,2))

