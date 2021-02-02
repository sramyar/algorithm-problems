'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

'''

def generate_parentheses(n):
    ans = []
    def backtrack(c = '', left = 0, right = 0):
        if len(c)==2*n:
            ans.append(c)
            return
        if left < n:
            backtrack(c+'(',left+1,right)
        if right < n and left > right:
            backtrack(c+')',left, right+1)
    backtrack()
    return ans


print(generate_parentheses(3))