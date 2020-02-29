'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

def merge_intervlas(input):
    '''
    This assumes intervals in the input are monotonically increasing
    i.e. lower bounds are sorted
    so, data is sorted first
    '''
    def get_first(item):
        return item[0]
    
    def sort_input(x):
        sorted_list = sorted(x, key=get_first)
        return sorted_list
    
    input = sort_input(input)
    merged = []
    curr_lo = input[0][0]
    curr_up = input[0][1]
    i = 0
    while i < len(input):
        if i != len(input) - 1:
            if curr_up >= input[i+1][0]:
                curr_up = input[i+1][1]
            else:
                merged.append([curr_lo,curr_up])
                curr_lo = input[i+1][0]
                curr_up = input[i+1][1]
        else:
            if input[i][0] == curr_lo:
                merged.append([input[i][0],input[i][1]])
            else:
                merged.append([curr_lo,input[i][1]])
        i += 1
    return merged


print(merge_intervlas([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervlas([[1,4],[4,5]]))
print(merge_intervlas([[8,10],[1,3],[2,6],[15,18]]))