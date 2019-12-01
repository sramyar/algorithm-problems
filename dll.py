'''
Doubly linked list
'''

class Node:
    
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.value = val

class DLList:

    def __init__(self):
        self.dummy = Node(None)
        self.n = 0
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
    
    def __repr__(self):
        l = []
        cue = self.dummy
        while cue.next != self.dummy:
            cue = cue.next
            l.append(cue.value)
        return str(l)
    
    def get_node(self, index):
        if index not in range(self.n):
            return self.dummy
        if index < self.n/2:
            cue = self.dummy.next
            for i in range(index):
                cue = cue.next
        else:
            cue = self.dummy.prev
            for i in range(self.n, index, -1):
                cue = cue.prev
        return cue
    
    def get(self, index):
        return self.get_node(index).value

    def set(self, index, val):
        node = self.get_node(index)
        old_value = node.value
        node.value = val
        return old_value
        
    def add_before(self, w: Node, val):
        u = Node(val)
        w.prev.next = u
        u.prev = w.prev
        w.prev = u
        u.next = w
        self.n += 1
        return u

    def add(self, index, val):
        w = self.get_node(index)
        self.add_before(w, val)

    def remove(self, w : Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w
    
    def remove_index(self, index):
        w = self.get_node(index)
        self.remove(w)


l = DLList()
for i in range(5):
    l.add(i, 10**(-i))
    print(l)
while l.n is not 0:
    l.remove_index(0)
    print(l)
    
    