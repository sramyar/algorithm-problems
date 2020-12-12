'''
You are given two NONEMPTY linked lists representing two non-negative integers.
The digits are stored in REVERSE ORDER and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6-> 4)
Output: 7 -> 0 -> 8
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,x):
        if(self.size == 0):
            self.head = node(x)
            self.tail = self.head
        else:
            self.tail.next = node(x)
            self.tail = self.tail.next
            self.tail.next = None
        self.size += 1

    def pop(self):
        if (self.size == 0):
            return None
        else:
            u = self.tail.data
            if(self.size == 1):
                self.head = self.tail = null
            else:
                cue = self.head
                while(cue.next != self.tail):
                    cue = cue.next
                self.tail = cue
                self.tail.next = None
            self.size -= 1
            return u


    def __repr__(self):
        out = ''
        u = self.head
        while(u.next != None):
            out += str(u.data)
            out += ' -> '
            u=u.next
        out += str(u.data)
        return out

def add(x,y,flag):
    if(not flag):
        if(x+y < 10):
            return x+y, flag
        else:
            return x+y-10, (not flag)
    else:
        if(x+y <9):
            return x+y+1, (not flag)
        else:
            return x+y+1-10, flag

def add_lists(left, right):
    flag = False
    l = left.head
    r = right.head
    a = linkedlist()
    while (True):
        if(l != None and r != None):
            s, flag = add(l.data, r.data, flag)
            a.add(s)
            r = r.next
            l = l.next
        elif(l != None and r == None):
            s, flag = add(l.data, 0, flag)
            a.add(s)
            l = l.next
        elif(l == None and r != None):
            s, flag = add(r.data, 0, flag)
            a.add(s)
            r = r.next
        else:
            break
    return a


def main():
    l = linkedlist()
    l.add(2)
    l.add(4)
    l.add(3)
    r = linkedlist()
    r.add(5)
    r.add(6)
    r.add(4)
    a = add_lists(l,r)
    print(a)
    print(l)
    print(l.pop())
    print(l)
    
if __name__ == "__main__":
    main()

    