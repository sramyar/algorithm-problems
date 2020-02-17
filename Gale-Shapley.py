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

    def check():
        for man in m.keys():
            if len(m[man]) > 0:
                return True
        return False
    
    def check_w_free(w):
        if len(matches) == 0:
            return None
        for item in matches:
            if w == item[1]:
                return item[0]
        return None

    matches = []

    while (check()):
        print(matches)
        for man in m.keys():
            if len(m[man]) == 0:
                continue
            w = m[man][0]
            m[man].remove(w)
            current_match = check_w_free(w)
            if current_match is None:
                matches.append((man,w))
                m[man] = []
            else:
                if f[w].index(current_match) < f[w].index(man):
                    continue
                else:
                    matches.append((man,w))
                    m[man] = []
                    matches.remove((current_match,w))

    return matches


# test case:

m = {1:[2,3,1], 2:[1,2,3], 3:[1,3,2]}
f = {1:[2,1,3], 2:[2,3,1], 3:[1,2,3]}

print(gale_shapley(m,f))

