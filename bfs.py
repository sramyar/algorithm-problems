from graph import Graph

def bfs(Graph: G, start = 0):
    seen = [start]
    q = [start]
    while len(q)>0:
        new = q.pop(0)
        for node in G.outEdges(new):
            if node not in seen:
                q.append(node)
                seen.append(node)
    return


G = Graph(5)

G.addEdge(0,1)
G.addEdge(0,2)
G.addEdge(1,2)
G.addEdge(2,3)
G.addEdge(1,3)
G.addEdge(2,4)