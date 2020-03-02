'''
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord,
such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a
    transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is
"hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0
'''

def one_diff(w1,w2):
    counter = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            counter +=1
    if counter == 1:
        return True
    else:
        return False


def ladder(begin,end,dic):
    if end not in dic:
        return 0
    if one_diff(begin,end):
        return 1
    paths = []
    for item in dic:
        if one_diff(begin,item):
            paths.append(item)
    
    if len(paths) == 0:
        return 0
    else:
        dic2 = list(dic)
        if begin in dic2:
            dic2.remove(begin)

    return 1 + min([ladder(item,end,dic2) for item in paths])

print(ladder('hit','dot',['hot','dot']))
print(ladder('hit','cog',["hot","dot","dog","lot","log","cog"]))
print(ladder('hit','cog',["hot","dot","dog","lot","log"]))
print(ladder('talk','foss',["tall","toll","tols","fols","foss"]))
print(ladder('vice','fine',['dice','dine','fine']))