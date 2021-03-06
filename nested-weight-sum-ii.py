'''
364. Nested List Weight Sum II
(Medium)

Given a nested list of integers, return the sum of all integers in the
list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

Different from the previous question where weight is increasing from root to leaf,
now the weight is defined from bottom up. i.e., the leaf level integers have
weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.

Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1;
1*3 + 4*2 + 6*1 = 17.

'''

def get_depth(input,d = 1):
    depths = []
    for item in input:
        if isinstance(item,int):
            depths.append(d)
        else:
            depths += get_depth(item,d+1)

    return depths
    
def fun(input):
    dep = sorted(get_depth(input))[-1]
    def weighted_sum(input, d = dep):
        sum = 0
        for item in input:
            if isinstance(item,int):
                sum += item*d
            else:
                sum += weighted_sum(item,d-1)
        return sum
    return weighted_sum(input,dep)

print(fun([[1,1],2,[1,1]]))
print(fun([1,[4,[6]]]))