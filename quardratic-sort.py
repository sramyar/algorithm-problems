'''
Given a sorted list A, return a sorted list B where each element in B is
f(x) = a*x^{2} + b*c + c (a > 0) if (x) is an element in A.

P.S. This is was my question when I was interviewing for LinkedIn.
'''

def get_min(a,b):
    return -b/(2*a)

def find_pivot(A,a,b,c):
    # returns index of pivot i.e. min
    p = get_min(a,b)
    lower = 0
    upper = len(A)
    while upper - lower > 1:
        if p >= A[((lower+upper)//2)]:
            lower = (lower+upper)//2
        else:
            upper = (lower+upper)//2
    return lower

def slicer(A,index):
    left = A[:index]
    right = A[index+1:]
    return left, right

def f(x,a,b,c):
    return a*(x**2) + b*x + c

def apply(A,a,b,c):
    left, right = slicer(A,find_pivot(A,a,b,c))
    left = [f(x,a,b,c) for x in left]
    right = [f(x,a,b,c) for x in right]
    return left, right

def merge(left,right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[-1] <= right[0]:
            merged.append(left.pop(-1))
        else:
            merged.append(right.pop(0))
    if len(right) > 0 and len(left) == 0:
        merged += right
    if len(right) == 0 and len(left) > 0:
        merged += [left[-i] for i in range(1,len(left)+1)]
    return merged

def quadratic_sort(A,a,b,c):
    left, right = apply(A,a,b,c)
    return merge(left,right)


print(quadratic_sort([-2,-1,0,1,2,3],1,-4,-1))