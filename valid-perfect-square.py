'''
Given a positive integer num, write a function which returns True if num is
a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false

'''

def isvalidsquare(num):
    i = 1
    while i**2 <= num:
        if i**2 == num:
            return True
        i += 1
    return False

print(isvalidsquare(16))
print(isvalidsquare(14))