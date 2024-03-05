night = input()
cnt = 0
row = int(night[1])
column = int(ord(night[0])) - int(ord('a')) + 1 

steps = [(-1, -2), (1, -2), (2,-1), (2,1), (1,2), (-1,2),(-2,-1), (-2,1)]

for step in steps:
    n_row = row + step[0]
    n_column = column + step[1]

    if n_row >= 1 and n_row <= 8 and n_column >= 1 and n_column <= 8 :
        cnt += 1 


print(cnt)