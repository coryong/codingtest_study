import sys

def solution(lst):
    # 방향 설정(북, 동, 남 ,서)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = []
    # Thanks to Boo~
    # 너비를 어떻게 할지 모르다가 코드 참고해서 짬
    for i in range(T):
        x, y = 0, 0
        st_d = 0 # 처음 시작할 때 방향은 북쪽
        x_lst = [0]
        y_lst = [0]
        for w in lst[i]:
            if w == 'F':
                x += dx[st_d]
                y += dy[st_d]
                x_lst.append(x)
                y_lst.append(y)
            elif w == 'B':
                x -= dx[st_d]
                y -= dy[st_d]
                x_lst.append(x)
                y_lst.append(y)
            elif w == 'L':
                st_d -= 1
                if st_d < 0:
                    st_d += 4
            else: # w == 'R'
                st_d += 1
                if st_d > 3:
                    st_d -= 4
            
        result.append((max(x_lst) - min(x_lst))*(max(y_lst) - min(y_lst)))
    return result


T = int(input())
lst = [sys.stdin.readline().rstrip() for _ in range(T)]
[print(_) for _ in solution(lst)]
