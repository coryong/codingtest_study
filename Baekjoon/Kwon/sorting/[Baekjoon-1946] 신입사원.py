# Sorting

import sys  # 시간초과 오류로 인해

T = int(input())
cnt_print = []
for i in range(T):
    apply = int(input())
    count = 1
    cnt_lst = [list(map(int, sys.stdin.readline().strip().split())) for i in range(apply)]
    cnt_lst.sort()
    # print(cnt_lst)
    first_sc = cnt_lst[0][1]  # 성적!!

    for i in range(1, apply):
        if first_sc > cnt_lst[i][1]:  # 순위 말고 성적이라고 생각하면 됨.
            count += 1
            first_sc = cnt_lst[i][1]
            #  하나가 성적이고 하나가 순위라 상관없음
            # print(first_sc)

    cnt_print.append(count)
    
# result
for i in cnt_print:
    print(i)
