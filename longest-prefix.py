'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

'''

def longest(strings):
    index_range = 200
    
    #get shortest-length string
    for item in strings:
        if len(item) < index_range:
            index_range = len(item)
    i = 0
    while i < index_range:
        j = 0
        curr = strings[j][i]
        for j in range(1,len(strings)):
            if strings[j][i] != curr:
                return i
        i += 1
    
    return i


def get_prefix(strings):
    i = longest(strings)
    #if i==0:
     #   return ""
    return strings[0][:i]
print(get_prefix(["flower","flow","flight"]))
print(get_prefix(["dog","racecar","car"]))