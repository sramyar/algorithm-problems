'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
'''

def fibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return (fibonacci(n-1)+fibonacci(n-2))

def print_fibonacci(n):
    s=''
    for i in range(n+1):
        s+= str(fibonacci(i))
        s+= "\t"
    return s
print("for n=2: ", fibonacci(2))
print("for n=3: ", fibonacci(3))
print("for n=4: ", fibonacci(4))
print("for n=5: ", fibonacci(5))
print("series for {}: ".format(6),print_fibonacci(6))

