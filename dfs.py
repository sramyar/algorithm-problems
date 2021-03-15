from graph import Graph

def dfs(G,start):
    seen = [start]
    stack = [start]
    while len(stack) > 0:
        new = stack.pop(-1)
        for node in G.outEdges(new):
            if node not in seen:
                stack.append(node)
                seen.append(node)
    return