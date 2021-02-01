'''

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

'''

def colorways(n,k):
    if n== 1:
        return k
    same = k
    diff = k * (k-1)
    for item in range(3,n+1):
        same, diff = diff, (same+diff)*(k-1)
    return same + diff

print(colorways(3,2))
    