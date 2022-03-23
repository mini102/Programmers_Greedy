import itertools

def solution(number, k):
    answer = ''
    mlist = []
    tmplist = [i for i in range(0,len(number))]
    
    result = list(itertools.combinations((tmplist),k))
    numlist = list(number)
    
    for i in result:
        for j in reversed(range(0,k)): 
            numlist.pop(i[j])
        st = "".join(numlist)
        mlist.append(st)
        numlist = list(number)
    return str(max(mlist))
