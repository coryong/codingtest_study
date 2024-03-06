n = int(input())
lst = []
answer = 1
for _ in range(n):
    lst.append(list(input().rstrip()))

def count_candy(lst):
    cnt_max = 1
    
    for i in range(n):
        cnt = 1
        # 가로
        for j in range(1, n):
            if lst[i][j] == lst[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            cnt_max = max(cnt, cnt_max)

        cnt = 1
        # 세로
        for j in range(1, n):
            if lst[j][i] == lst[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            cnt_max = max(cnt, cnt_max)

    return cnt_max

for k in range(n):
    for l in range(n - 1):
        # 오른쪽
        if l + 1 < n and lst[k][l] != lst[k][l + 1]:
            tmp = lst[k][l]
            lst[k][l]= lst[k][l + 1]
            lst[k][l + 1] = tmp
            answer = max(count_candy(lst),answer)
            tmp = lst[k][l]
            lst[k][l]= lst[k][l + 1]
            lst[k][l + 1] = tmp
        # 왼쪽
        if k + 1 < n and lst[k][l] != lst[k + 1][l]:
            tmp = lst[k][l]
            lst[k][l] = lst[k + 1][l]
            lst[k + 1][l] = tmp
            answer = max(count_candy(lst),answer)
            tmp = lst[k][l]
            lst[k][l] = lst[k + 1][l]
            lst[k + 1][l] = tmp
print(answer)