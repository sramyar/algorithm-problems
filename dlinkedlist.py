'''
Implmentation of Doubly Linked List data structure
'''

class Node:
    
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.n = 0
        self.dummy = Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
    
    def get_node(self,index):

        if (self.n == 0 or index > self.n - 1):
            return self.dummy

        cue = self.dummy

        if index < self.n/2:
            i = -1
            while i is not index:
                cue = cue.next
                i += 1
        else:
            i = self.n
            while i != index:
                cue = cue.prev
                i -= 1

        return cue

    def get(self, index):
        return self.get_node(index).value
    
    def set_value(self, index, val):
        cue = self.get_node(index)
        old_value = cue.value
        cue.value = val
        return old_value
    
    def add_before(self, cue, val):
        new_node = Node(val)

        new_node.prev = cue.prev
        new_node.next = cue
        cue.prev.next = new_node
        cue.prev = new_node
        
        self.n += 1

        return new_node

    def add(self, index, val):
        cue = self.get_node(index)
        self.add_before(cue, val)

    def remove(self, cue):
        cue.next.prev = cue.prev
        cue.prev.next = cue.next
        self.n -= 1
        return cue

    def remove_by_index(self, index):
        self.remove(self.get_node(index))
    
    def __repr__(self):
        output = []
        for i in range(self.n):
            output.append(self.get(i))
        return str(output)


# Test cases:
import math
dll = LinkedList()
for i in range(5):
    dll.add(i,math.pow(10,i))
    print(dll)

dll.remove_by_index(3)
print(dll)

dll.add(3, 8)
print(dll)