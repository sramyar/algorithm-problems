'''
Implementation of binary tree
'''

class BinaryTree:
    class Node:
        def __init__(self,x):
            self.data = x
            self.left = self.right = self.parent = None
        
    def __init__(self):
        self.root = None
        self.size = 0
    
    def depth(self,u):
        if(u==self.root):
            return 0
        return depth(u.parent)+1

    def size(self,r):
        if(r==None):
            return 0
        return size(r.left) + size(r.right)

    def height(self,u):
        if(u==None):
            return 0
        return max(self.height(u.left), self.height(u.right))+1

    def traverse(self,u):
        if(u==self.root):
            print(u.data)
            return
        traverse(u.left)
        traverse(u.right)

    def traverse_iter(self):
        u=self.root
        prev = None
        while(u != None):
            if(prev == u.parent):
                print(u.data)
                if(u.left != None):
                    nxt = u.left
                elif(u.right != None):
                    nxt = u.right
                else:
                    nxt = u.parent
            elif(prev == u.left):
                if(u.right != None):
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prev = u
            u = nxt

    def size_iter(self):
        u = self.root
        size = 0
        prev = None
        while(u != None):
            if(prev == u.parent):
                size += 1
                if(u.left != None):
                    nxt = u.left
                elif(u.right != None):
                    nxt = u.right
                else:
                    nxt = u.parent
            elif(prev == u.left):
                if(u.right != None):
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prev = u
            u = nxt
    
    def bf_traverse(self):
        u=self.root
        a = list()
        if(curr.left != None): a.append(curr.left)
        if(curr.right != None): a.append(curr.right)
        while(len(a)>0):
            curr = a.pop(0)
            print(curr.data)
            if(curr.left != None): a.append(curr.left)
            if(curr.right != None): a.append(curr.right)

    def find_eq(self,x):
        u = self.root
        while(u!=None):
            if(u.data < x):
                u = u.right
            elif(u.data > x):
                u = u.left
            else:
                return u.data
        return None

    def find(self,x):
        # finds smallest value greater than or equal to 'x'
        z = None
        u = self.root
        while(u!=None):
            if(u.data < x):
                u = u.right
            elif(u.data > x):
                u = u.left
                z = u
            else:
                break
        if(z==None): return None
        return z.data
    
    def find_last(self,x):
        u = self.root
        prev = None
        while(u!=None):
            prev = u
            if(x > u.data):
                u = u.right
            elif(x < u.data):
                u = u.left
            else:
                return u
        return prev

    def add_child(self,p,c):
        if(p==None):
            self.root = c
        else:
            if(c.data > p.data):
                p.right = c
            elif(c.data < p.data):
                p.left = c
            else:
                return False
            c.parent = p
        self.size += 1
        return True

    def add(self,x):
        p = self.find_last(x)
        return self.add_child(p,self.Node(x))

    def splice(self,u):
        if(u.left != None):
            s = u.left
        else:
            s = u.right
        if(u == self.root):
            self.root = s
            p = None
        else:
            p = u.parent
            if(s == u.left):
                p.left = s
            else:
                p.right = s
        if(s != None):
            s.parent = p

        self.size -= 1

    def remove(self,x):
        u = self.find_last(x)
        if(u.data == x):
            if (u.left == None or u.right == None):
                self.splice(u)
            else:
                curr = u.right
                while(curr.left != None):
                    curr = curr.left
                u.data = curr.data
                self.splice(curr)
            return True
        else:
            return False
    
def main():
    t = BinaryTree()
    t.add(7)
    t.add(3)
    t.add(11)
    t.add(1)
    t.add(5)
    t.add(9)
    t.add(13)
    t.add(4)
    t.add(6)
    t.add(8)
    t.add(12)
    t.add(14)
    t.remove(11)
    t.traverse_iter()
    

if __name__ == "__main__":
    main()
    
        


