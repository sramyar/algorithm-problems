'''
Given a list of words and two words word1 and word2, 
return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

    Note: You may assume that word1 does not equal to word2, and word1
    and word2 are both in the list.
'''

def find_distance(w1,w2,l):
    w1i = -1
    w2i = -1
    d = len(l)

    for i in range (len(l)):
        if l[i] == w1:
            w1i = i
        elif l[i] == w2:
            w2i = i
        
        if w1i >= 0 and w2i >=0 and abs(w1i - w2i) < d:
            d = abs(w1i - w2i)

    return d

l = ["practice", "makes", "perfect", "coding", "makes"]
print(find_distance('coding','practice',l))
print(find_distance('makes','coding',l))