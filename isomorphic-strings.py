'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same character
but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
'''

def dic_builder(w):
    dic={}
    for i in range(len(w)):
        if w[i] not in dic.keys():
            dic[w[i]] = i
        else:
            continue
    return dic


def is_isomorphic(w1,w2):
    dic1 = dic_builder(w1)
    dic2 = dic_builder(w2)

    for i in range(len(w1)):
        if dic1[w1[i]] != dic2[w2[i]]:
            return False
    return True


print(is_isomorphic('egg','add'))
print(is_isomorphic('foo','bar'))
print(is_isomorphic('paper','title'))