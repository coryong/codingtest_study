a=int(input())
room=[]
answer=0
time=0
for _ in range(a):
    room.append(list(map(int,input().split())))
room.sort(key=lambda x:(x[1],x[0]))
for start,end in room:
    if time <=start:
        time=end
        answer+=1
print(answer)