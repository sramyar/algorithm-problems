class LinkedList:
    '''
    Singly linked list
    '''
    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None

    def push(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        if self.n == 0:
            self.tail = new_head
        self.n += 1
        return val

    def pop(self):
        if self.n == 0:
            return None
        
        val = self.head.value
        self.head =self.head.next
        self.n -= 1

        if self.n == 0:
            self.tail = None

        return val
    
    def remove(self):
        self.pop()

    def add(self, val):
        if self.n == 0:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.n += 1
        return True

    def __repr__(self):
        if self.n == 0:
            return str([])
        else:
            output = []
            cue = self.head
            while cue is not None:
                output.append(cue.value)
                cue = cue.next
            return str(output)
    


class Node:
    '''
    Nodes in the linkedlist
    '''
    def __init__(self, val):
        self.value = val
        self.next = None

# Testing here:
import math
llist = LinkedList()
for i in range(5):
    llist.add(math.pow(2,i))
    print(llist)
llist.remove()
print(llist)