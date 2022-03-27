def solution(people, limit):
    answer = 0
    tmp = min(people)

    while len(people)!=0:
        tmp = min(people)
        people.remove(tmp)
        if len(people)==0:
            answer+=1
            break
        while tmp + min(people) <= limit:
                tmp += min(people)
                people.remove(min(people))
                if len(people)==0:
                    break
        answer+=1
    
    return answer
