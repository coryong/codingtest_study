S = list(str(input()))
T = list(str(input()))

while len(T) >= len(S) :

    if T == S :
        print(1)
        break

    else:
        if T[-1] == 'A' :
            T.pop()
        
        else :
            T.pop()
            T = list(reversed(T))


if T != S :
    print(0)
        

    

    