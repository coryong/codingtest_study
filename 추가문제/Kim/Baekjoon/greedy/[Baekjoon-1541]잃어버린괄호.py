N = str(input())
N_split = N.split('-') # - 기준으로 나누기

tmp = []
for n in N_split: # 각 요소 들 정수 변환및 덧셈
    sum_ = 0 
    for i in n.split('+'): 
        sum_ += int(i)
    tmp.append(sum_)

first = tmp.pop(0) # 첫번째 요소 
second = sum(tmp) # 괄호 칠 요소

print(first-second)




