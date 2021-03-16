'''
Graph implementation in python
using adjancency lists
'''

class Graph:

    def __init__(self,n):
        self.n = n
        self.alist = []
        self.costs = []
        for i in range(n):
            self.alist.append([])
            self.costs.append([])
    
    def addEdge(self,i,j,c):
        self.alist[i].append(j)
        self.costs[i].append(c)
    
    def removeEdge(self,i,j):
        if self.alist[i] != None:
            if j in self.alist[i]:
                indx = self.alist[i].index(j)
                self.alist[i].remove(j)
                self.costs[i].remove(costs[i][indx])
                return True
        else:
            return False

    def hasEdge(self,i,j):
        return (j in self.alist[i])
    
    def outEdges(self,i):
        return list(self.alist[i])
    
    def getCost(self,i,j):
        if j in self.alist[i]:
            return self.costs[i][self.alist[i].index(j)]

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



