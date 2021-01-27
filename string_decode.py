'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''

def decode(s):
    intstack=[]
    charstack=[]
    temp=""
    ans=""
    i = 0
    
    while i < len(s):
        # if char is int, add it to stack
        if s[i] in '123456789':
            intstack.append(int(s[i]))
            
        # if close bracket, get temp and put back ans in charstack
        elif s[i] == ']':
            temp = ""
            count = intstack.pop(-1)

            while (len(charstack) > 0 and charstack[-1] != '['):
                temp = charstack.pop(-1) + temp
            
            if charstack[-1]=='[':
                charstack.pop(-1)
            
            for n in range(count):
                ans += temp
            
            for item in ans:
                charstack.append(item)
            
            ans = ""
        
        # if open bracket, add to charstack and consider whether previous char is a number
        elif s[i] == '[':
            if (s[i-1] not in '123456789'):
                intstack.append(1)
                
            charstack.append(s[i])
            #print(charstack)
        # if ordinary character, add to charstack
        else:
            charstack.append(s[i])
        
        i+=1
    
    
    for item in charstack:
        ans += item
    
    return ans


print(decode("3[a]2[bc]"))
print(decode("3[a2[c]]"))
        