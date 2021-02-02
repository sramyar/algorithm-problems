'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

'''
def form_dic():
    dic={}
    alphs = 'abcdefghijklmnopqrstuvwxyz'
    alph = []
    for s in alphs:
        alph.append(s)

    for i in range(2,10):
        dic[i]=[alph.pop(0)]
        if i!=7 and i != 9:
            for _ in range(2):
                dic[i].append(alph.pop(0))
        else:
            for _ in range(3):
                dic[i].append(alph.pop(0))
    return dic
        

def combos(s):
    dic = form_dic()
    def backtrack(c,nxt_dgts):
        if len(nxt_dgts) == 0:
            ans.append(c)
        else:
            for char in dic[int(nxt_dgts[0])]:
                backtrack(c+char,nxt_dgts[1:])
        
    ans = []
    backtrack("",s)
    return ans

print(combos("23"))
                
    
    