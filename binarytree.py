import queue

class Node:

    def __init__(self, val):
        self.parent = None
        self.right = None
        self.left = None
        self.value = val

class BinaryTree:

    def __init__(self):
        self.root = None
        self.n = 0
    
    def add_child(self, parent, child):
        if parent == None:
            self.root = child
        else:
            if child.value > parent.value:
                parent.right = child
            elif child.value < parent.value:
                parent.left = child
            else:
                return False
            child.parent = parent
        self.n += 1
        return True
    
    def find_depth(self, u):
        d = 0
        while u != self.root:
            u = u.parent
            d += 1
        return d
    
    def find_size(self, u: Node):
        if u is None:
            return 0
        return 1 + self.find_size(u.left) + self.find_size(u.right)

    def find_height(self, u: Node):
        if u is None:
            return 0
        return 1 + max(self.find_height(u.left), self.find_height(u.right))

    def depth_first_recur(self, u: Node):
        if u is None:
            return
        self.depth_first_recur(u.left)
        self.depth_first_recur(u.right)

    def depth_first(self, u: Node):
        prev = None
        while u != None:
            if prev == u.parent:
                if u.left != None:
                    next = u.left
                elif u.right != None:
                    next = u.right
                else:
                    next = u.parent
            elif prev == u.left:
                if u.right != None:
                    next = u.right
                else:
                    next = u.parent
            else:
                next = u.parent
            prev = u
            u = next
    
    def bf_traverse(self):
        u = self.root
        q = queue.Queue()
        q.put(u)
        while not q.empty():
            temp = q.get()
            print(temp.value)
            if temp.left != None:
                q.put(temp.left)
            if temp.right != None:
                q.put(temp.right)
            
    def find_eq(self, val):
        u = self.root
        while u != None:
            if u.value == val:
                return u.value
            elif val > u.value:
                u = u.right
            else:
                u = u.left
        return None

    def find(self, val):
        '''
        Returns smallest value in the tree that greater than or equal to target val
        '''
        u = self.root
        z = None
        while u is not None:
            if val < u.value:
                z = u
                u = u.left
            elif val > u.value:
                u = u.right
            else:
                z = u
        if z is None:
            return None
        return z.value

    def find_last(self, val):
        u = self.root
        prev = None
        while u != None:
            prev = u
            if val > u.value:
                u = u.right
            elif val < u.value:
                u = u.left
            else:
                return u
        return prev
    
    def add(self, val):
        u = self.find_last(val)
        child = Node(val)
        return self.add_child(u, child)

    def splice(self, u: Node):
        if u.left is not None:
            child = u.left
        else:
            child = u.right

        if u == self.root:
            self.root = child
            p = None
        else:
            p = u.parent   
            if p.left == u:
                p.left = child
            else:
                p.right = child

        if child is not None:
            child.parent = p
        self.n -= 1
        return True

    def remove(self, u: Node):
        if u.left is not None or u.right is not None:
            self.splice(u)
        # using the find(val, u) function above
        #w = self.find(u.value, u.right)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.value = w.value
            self.splice(w)
    

tree = BinaryTree()
tree.add(7)
tree.add(8)
tree.add(5)
tree.add(7.5)
tree.add(10)
tree.bf_traverse()
tree.add(100)
tree.bf_traverse()

    
    
