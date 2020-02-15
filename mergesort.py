'''
Implementing the MergeSort algorithm

input >> [3,43,34,53,5]
output >> [3,5,34,43,53]
'''

def merge(l1,l2):
    '''
    input: sorted lists l1 and l2
    output: one sorted list containing values in l1 and l2
    '''
    output = []
    output_length = len(l1) + len(l2)
    i = 0
    while i < output_length:
        if (len(l1) > 0 and len(l2) > 0):
            if l1[0] < l2[0]:
                output.append(l1[0])
                l1.remove(l1[0])
            else:
                output.append(l2[0])
                l2.remove(l2[0])
        elif (len(l1) == 0 and len(l2) > 0):
            for item in l2:
                output.append(item)
            return output
        else:
            for item in l1:
                output.append(item)
            return output
        i += 1
    return output

def mergesort(input):
    if len(input) == 1:
        return input

    l1 = mergesort(input[0:len(input)//2])
    l2 = mergesort(input[len(input)//2:])

    return merge(l1,l2)


print(mergesort([9,8,7,6,5,4,3,2,1]))