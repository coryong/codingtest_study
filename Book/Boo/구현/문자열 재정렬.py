l = input()
lst_n = []
lst_a = []

for i in l:
    if i.isalpha():
        lst_a.append(i)
    else:
        lst_n.append(int(i))

lst_a.sort()

for i in lst_a:
    print(i, end='')
print(sum(lst_n))