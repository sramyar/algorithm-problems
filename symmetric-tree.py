'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

 

Note:
Bonus points if you could solve it both recursively and iteratively.
'''
from binarytree import Node, BinaryTree

def isSymmetric(input):
    i = 1
    while i < len(input):
        sub = input[2**i - 1 : 2**(i+1) - 1]
        while len(sub) > 0:
            if sub.pop(0) != sub.pop():
                return False
        i += 1
    return True



print(isSymmetric([1,2,2,3,4,4,3]))
print(isSymmetric([1,2,2,None,3,None,3]))