'''
Suppose you have a long flowerbed in which some of the plots are planted and
some are not. However, flowers cannot be planted in adjacent plots - they would
compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0means empty
and 1 means not empty), and a number n, return if n new flowers can be planted in it
without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:

  1. The input array won't violate no-adjacent-flowers rule.
  2. The input array size is in the range of [1, 20000].
  3. n is a non-negative integer which won't exceed the input array size.

'''

def can_place(input, n):
    if len(input) == 1:
        if n == 1:
            return 0 in input
        else:
            return False
    
    if len(input) == 2:
        if 1 in input:
            return False
        elif n == 1:
            return True
        else:
            return False

    prev = input[0]
    counter = 0
    for i in range(1,len(input)-1):
        nxt = input[i+1]
        if prev != 1 and input[i] == 0 and nxt != 1:
            counter += 1
            if counter == n:
                return True
        prev = input[i]
    return False


input = [1,0,0,0,1]
print(can_place(input,1))
print(can_place(input,2))

