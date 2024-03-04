# 처음에 조건문으로 풀다가 정확도랑 시간복잡도에서 잡힘
# for문 indexError 이후 LIFO 형식 파악 후 스택으로 돌림
def solution(number, k):
    stack = [] 

    for num in number:
        # 스택이 비어있지 않고, 현재 숫자가 스택의 top 값보다 크고, 아직 제거해야 할 숫자가 남아있으면
        while stack and stack[-1] < num and k > 0:
            stack.pop()  
            k -= 1       
        
        stack.append(num)  
    
    if k > 0:
        stack = stack[:-k]

    # list to str
    return ''.join(stack)
