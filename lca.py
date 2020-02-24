'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

 

Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.

'''

from binarytree import BinaryTree, Node

def LCA(input : BinaryTree, p: Node, q: Node):
    lca = input.root
    while q.parent != None and p.parent != None:
        if p == q.parent and p.value < lca.value:
            lca = p
        elif q == p.parent and q.value < lca.value:
            lca = q
        elif p.parent == q.parent and p.parent.value < lca.value:
            lca = p.parent
        else:
            p = p.parent
            q = q.parent
    return lca

input1 = [6,2,8,0,4,7,9,3,5]
tree = BinaryTree()
for item in input1:
    tree.add(item)

print(LCA(tree,tree.find_last(2),tree.find_last(8)))
print(LCA(tree,tree.find_last(2),tree.find_last(4)))






