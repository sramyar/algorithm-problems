'''
You are given two NONEMPTY linked lists representing two non-negative integers.
The digits are stored in REVERSE ORDER and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6-> 4)
Output: 7 -> 0 -> 8

'''
from slinkedlist import LinkedList, Node


l1 = LinkedList()
l1.add(2)
l1.add(4)
l1.add(3)

l2 = LinkedList()
l2.add(5)
l2.add(6)
l2.add(4)

def addtwonums(list1: LinkedList, list2: LinkedList) -> LinkedList:
        
    solution = LinkedList()
    c1 = list1.head
    c2 = list2.head
    carry = 0
    while c1 != None or c2 != None:
        if c1 is None:
            x = 0
        else:
            x = c1.value
        if c2 is None:
            y = 0
        else:
            y = c2.value
        total = x + y + carry
        if total < 10:
            solution.add(total)
            carry = 0
        else:
            solution.add(total - 10)
            carry = 1
        if c1 is not None: c1 = c1.next
        if c2 is not None: c2 = c2.next
    return solution

print(addtwonums(l1,l2))


