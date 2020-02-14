'''
So, in this interview question, I was asked to sort the
input based on frequency.

Example:
input <- [3,4,6,3,4,3,5]
output: [3,4,6,5]

'''

def dic_maker(l):
    '''
    input: list of numbers
    output: a dictionary mapping key to frequency
    loops through list and maps key to frequency
    RETURNS dictionary
    '''
    dic = {}

    for item in l:
        if item not in dic.keys():
            dic[item] = 1
        else:
            dic[item] += 1
    return dic


def sorter(input):
    '''
    input: list of numbers/data
    output: sorted (desc) keys based on frequency
    sorts the keys based on frequency
    returns list of sorted keys
    '''
    dic = dic_maker(input)
    l = sorted(dic.items(),key = lambda t: t[1],
    reverse=True)
    return [item[0] for item in l]

data = [3,4,6,3,4,3,5]
print(sorter(data))