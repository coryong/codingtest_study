def solution(n, lost, reserve):
    # 조건5 set으로 처리
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))
    
    #
    for i in new_reserve:
        if (i-1) in new_lost:
            new_lost.remove(i-1)
            
        elif (i+1) in new_lost:
            new_lost.remove(i+1)
            
        else:
            continue
    
    result = n - len(new_lost)
    return result
