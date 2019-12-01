'''
Singly linked list
'''

class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

class SLList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
    
    def __repr__(self):
        l = []
        cue = self.head
        while cue != None:
            l.append(cue.value)
            cue = cue.next
        return str(l)

    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        if self.n == 0:
            self.tail = node
        self.n += 1
        return val

    def pop(self):
        if self.n == 0:
            return None
        u = self.head
        self.head = u.next
        if self.n == 1:
            self.tail = None
        self.n -= 1
        return u.value

    def remove(self):
        self.pop()

    def add(self, val):
        u = Node(val)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True
    


l = SLList()
for i in range(5):
    l.add(2**(-i))
    print(l)
for i in range(5):
    l.pop()
    print(l)
    