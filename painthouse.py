'''
Given a list of houses and the cost of painting each house, the houses can
be painted in three colors RED, GREEN and BLUE, two neighboring houses can’t
be painted in the same color, calculate the total minimum cost for painting
all houses.
'''
import math

def mincost(costs):
    n = len(costs)
    if n == 0:
        return 0
    for i in range(1,n):
        for j in range(3):
            costs[i][j] += min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3])
    
    return min(costs[n-1][0], costs[n-1][1], costs[n-1][2])


costs = [[1000,1000,1],[3,2,1],[1000,1000,1]]
print(mincost(costs))