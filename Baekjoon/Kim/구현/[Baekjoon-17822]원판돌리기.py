from collections import deque
N, M, T = map(int, input().split())
circles = [deque(list(map(int, input().split()))) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(T)]

def spin(circle, d, k) :

    if d == 0 :
        for _ in range(k):
            circle.appendleft(circle.pop())
    
    else : 
        for _ in range(k):
            circle.append(circle.popleft())


def check(arr, N, M):
    tmp_arr = [deque([arr[i][j] for j in range(M)]) for i in range(N)] # tmp_arr 사용하지 않으면 인접한 모든 것을 제거하지 못하는 경우 발생 
    ch = False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(N) : 
        for j in range(M):
            for z in range(4):
                nx = (i + dx[z])
                ny = (j + dy[z]) % M 
                if 0<=nx<N and 0<=ny<M and arr[i][j] != 'x' and arr[i][j] == arr[nx][ny]:
                    tmp_arr[i][j] = 'x'
                    tmp_arr[nx][ny] = 'x'
                    ch = True 

    if not ch: 
        cnt = 0 
        num = 0 
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 'x':
                    num += arr[i][j]
                    cnt += 1 
        if cnt == 0 : 
            return arr, False
        avg = num / cnt 
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 'x' :
                    if arr[i][j] < avg:
                        tmp_arr[i][j] += 1 
                    elif arr[i][j] > avg:
                        tmp_arr[i][j] -= 1 
    return tmp_arr, True


for comm in command: 
    X, D, K = comm 
    for i in range(X, N+1, X) :
        spin(circles[i-1], D, K)
    circles, check_state = check(circles, N, M)
    if not check_state:
        break

result = 0

for i in range(N):
    for j in range(M) :
        if circles[i][j] != 'x':
            result += circles[i][j]

print(result)
    
