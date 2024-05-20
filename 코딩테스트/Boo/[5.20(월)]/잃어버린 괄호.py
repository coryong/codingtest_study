l = input()
m = l.split('-')
sumx = 0

x = sum(map(int, (m[0].split('+'))))
if l[0] == '-':
    sumx -= x
else:
    sumx += x
    
mm = m[1:]

for x in mm: 
    x = sum(map(int, (x.split('+'))))
    sumx -= x
    
print(sumx)