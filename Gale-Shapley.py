'''
Implementing the Gale-Shapley algorithm for the stable mathcing problem

*** The algorithm is M-proposing

*** Finds the M-Optimal matching

Takes two dictionaries of the same length containing the individuales and
their preferences and returns a list of tuples containing the matched individuals

Example:
m = {1:[2,3,1], 2:[1,2,3], 3:[1,3,2]}
f = {1:[2,1,3], 2:[2,3,1], 3:[1,2,3]}

returns -> (1,3), (2,1), (3,2)
'''

def gale_shapley(m, f):
    if len(m) != len(f):
        print('Wrong size')
        return
    def remove(mm,mw):
        for man in m.keys():
            m[man].remove(mw)
        for woman in f.keys():
            f[woman].remove(mm)

    matches = []
    for dude in m.keys():
        for ch in m[dude]:
            if f[ch][0] == dude:
                matches.append((dude,ch))
                remove(dude,ch)
    
    return matches

m = {1:[2,3,1], 2:[1,2,3], 3:[1,3,2]}
f = {1:[2,1,3], 2:[2,3,1], 3:[1,2,3]}

print(gale_shapley(m,f))

