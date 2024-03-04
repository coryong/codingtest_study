def solution(number, k):
    lst = []
    
    for i in number:
        if not lst:
            lst.append(i)
            continue
        if k > 0:
            while lst[-1] < i:
                lst.pop()
                k -= 1
                if not lst or k <= 0:
                    break
        lst.append(i)
    
    if k > 0:
        return ''.join(lst[:-k])
    else: 
        return ''.join(lst)
    