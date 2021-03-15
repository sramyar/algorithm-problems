'''
Graph implementation in python
using adjancency lists
'''

class Graph:

    def __init__(self,n):
        self.n = n
        self.alist = []
        for i in range(n):
            self.alist.append([])
    
    def addEdge(self,i,j):
        self.alist[i].append(j)
    
    def removeEdge(self,i,j):
        if self.alist[i] != None:
            if j in self.alist[i]:
                self.alist.remove(j)
                return True
        else:
            return False

    def hasEdge(self,i,j):
        return (j in self.alist[i])
    
    def outEdges(self,i):
        return list(self.alist[i])

    def inEdges(self,j):
        inEdges = []
        for node in self.alist:
            if j in node:
                inEdges.append(node)
        return inEdges

    def __repr__(self):
        s=''
        i = 0
        for node in self.alist:
            s += str(i)
            s += ': '
            s += str(node)
            s += '\n'
            i += 1
        return s



