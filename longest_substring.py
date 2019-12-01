'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

'''

def substringer(index, string):
    dic = {}
    i = index
    while i < len(string):
        if string[i] not in dic.keys():
            dic[string[i]] = None
            i += 1
        else:
            break
    return(len(dic))

def find_longest(string):
    l = []
    for i in range(len(string)):
        l.append(substringer(i, string))
    return(max(l))


print(find_longest('abcabcbb'))
print(find_longest('bbbbb'))
print(find_longest('pwwkew'))

