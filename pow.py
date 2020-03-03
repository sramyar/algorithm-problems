'''
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

'''

def pow(x,n):
    if n > 0:
        ans = 1
        for i in range(0,n):
            ans = x*ans
        return ans
    elif n < 0:
        return (1/pow(x,-n))
    else:
        return 1

def pow_re(x,n):
    if n == 0:
        return 1
    if n > 0:
        return x*pow_re(x,n-1)
    else:
        return x*pow_re(x,n+1)

print(pow(2.00000,10))
print(pow(2.10000,3))
print(pow(2.00000,-2))
print(pow(10,0))

print(pow_re(2.00000,10))
print(pow_re(2.10000,3))
print(pow_re(2.00000,-2))
print(pow_re(10,0))