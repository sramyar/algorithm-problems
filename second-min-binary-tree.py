'''
Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node.

If the node has two sub-nodes, then this node's value is the smaller value
among its two sub-nodes. More formally, the property

root.val = min(root.left.val, root.right.val)

always holds.

Given such a binary tree, you need to output the second minimum value in the set made
of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''
import math

from binarytree import BinaryTree, Node



def second_min(tree: BinaryTree):
    root = tree.root
    height = tree.find_height(root)
    second_min = math.inf
    q = []
    q.append(root)
    h = 0
    while h < height:
        u = q.pop(0)
        if u.left != None:
            q.append(u.right)
            q.append(u.left)
        if u.value > root.value and u.value < second_min:
            second_min = u.value
        h += 1
    if second_min > root.value and second_min != math.inf:
        return second_min
    else:
        return -1
        
tree1 = BinaryTree()
tree1.add(2)
tree1.add(2)
tree1.add(5)
tree1.add(5)
tree1.add(7)


tree2 = BinaryTree()
tree2.add(2)
tree2.add(2)
tree2.add(2)

print(second_min(tree1))
print(second_min(tree2))