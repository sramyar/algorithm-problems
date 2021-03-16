from graph import Graph

def initialize(start):
    temp = {i:float('Inf') for i in range(G.n - 1) if i != start}
    perm = {start:0}
    curr = start
    return curr, temp, perm
    
def update(G,curr,temp,perm):
    out = G.outEdges(curr)
    print(curr,out,temp,perm)
    for node in out:
        if (node in temp) and G.getCost(curr,node) + perm[curr] < temp[node]:
            temp[node] = G.getCost(curr,node) + perm[curr]
    
    # get the lowest cost from temp set (get the first element of sorted temp)
    lowest_cost = sorted(temp.items(), key = lambda x:x[1])[0]
    curr = lowest_cost[0]
    curr_cost = lowest_cost[1]
    perm[curr] = curr_cost
    temp.pop(curr)
    return curr, temp, perm

def dijkstra(G, start):
    curr, temp, perm = initialize(start)
    curr = start
    while len(temp) > 0:
        curr, temp, perm = update(G,curr,temp,perm)
    
    return perm
        