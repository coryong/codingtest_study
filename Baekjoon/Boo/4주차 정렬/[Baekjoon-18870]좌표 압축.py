n = int(input())
lst = list(map(int, input().split()))

com = sorted(list(set(lst)))
idx = [i for i in range(len(com))]

dict = {key:value for key, value in zip(com, idx)}
for i in lst:
		print(dict[i])