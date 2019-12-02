class Node:

    def __init__(self, val):
        self.parent = None
        self.right = None
        self.left = None
        self.value = val

class BinaryTree:

    def __init__(self):
        self.root = None
    
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