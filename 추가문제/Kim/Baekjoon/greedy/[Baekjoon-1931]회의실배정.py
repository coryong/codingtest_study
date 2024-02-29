N = int(input())

time = []

for _ in range(N) :
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x : (x[1], x[0])) # 종료시간을 오름차순으로 정렬

endtime = 0 
answer =0 

for t in time:
    if endtime <= t[0]: 
        endtime = t[1] # 종료시간 업데이트
        answer += 1

print(answer)
