'''
You are given two NONEMPTY linked lists representing two non-negative integers.
The digits are stored in REVERSE ORDER and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6-> 4)
Output: 7 -> 0 -> 8

'''
#Singly list class
class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, start_node):
        self.start = start_node
        self.nodelist = [start_node]
    
    def add(self, node):
        cur = self.start
        while cur.next is not None:
            cur = cur.next
        cur.next = node


n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)

m1.next = m2
m2.next = m3

input1 = set(n1,n2,n3)
input2 = set(m1,m2,m3)


class Solution:
    def addtwonums(self, list1, list2):
        cue1 = list1.start
        cue12 = list2.start
        output = LinkedList(ListNode(cue1.value + cue2.value))
        ocue = output.start
        while True:
            
    