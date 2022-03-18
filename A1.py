def solution(n, lost, reserve):
    answer = n-len(lost)
    attend=[]
    while len(reserve)>0:
        for i in reserve:
            attend.append(i)
            if i in lost:
                answer+=1
                lost.remove(i)
                reserve.remove(i)
                continue
            if i-1 in lost and i-1 not in attend:
                answer+=1
                reserve.remove(i)
                attend.append(i-1)
                continue
            if i+1 in lost and i+1 not in attend:
                answer+=1
                reserve.remove(i)
                attend.append(i+1)
                continue
            reserve.remove(i)
    #print(attend)
    return answer
