'''
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.

Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

'''

def decode(s):
    tape= ''
    curr=''
    for i,c in enumerate(s):
        if c not in '123456789':
            curr += c
            tape += c
        else:
            for n in range(int(c)-1):
                tape += curr
            curr = tape
        #print(tape)
    return tape

print(decode("leet2code3"))
print(decode("ha22"))
print(len(decode("a2345678999999999999999")))