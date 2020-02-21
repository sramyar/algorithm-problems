'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def out_of_order(curr, next):
    if curr == 'I' and (next == 'V' or next == 'X'):
        return True
    
    elif curr == 'X' and (next == 'L' or next == 'C'):
        return True
    
    elif curr == 'C' and (next == 'D' or next == 'M'):
        return True
    
    else:
        return False

def roman_to_integer(input):
    sum = 0
    for i in range(len(input)):
        curr = input[i]
        next = input[i+1] if i+1 < len(input) else None
        if out_of_order(curr,next):
            sum -= value[curr]
        else:
            sum += value[curr]
    return sum

print(roman_to_integer('III'))
print(roman_to_integer('IV'))
print(roman_to_integer('IX'))
print(roman_to_integer('LVIII'))
print(roman_to_integer('MCMXCIV'))