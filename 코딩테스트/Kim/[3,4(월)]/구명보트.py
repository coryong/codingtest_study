# 무거운 사람을 먼저 보낸다고 생각
# 무거운 사람과 가벼운사람을 같이 보내면 최소값 도달 가능
def solution(people, limit):
    answer = 0
    people.sort()
    
    first = 0 
    end = len(people) - 1
    
    while first <= end:
        if people[first] + people[end] <= limit :
            first += 1 
            end -= 1 
            answer += 1 

        else : 
            end -= 1
            answer += 1 

    return answer 
            
        