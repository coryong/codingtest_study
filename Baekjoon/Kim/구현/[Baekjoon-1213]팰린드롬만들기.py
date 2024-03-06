from collections import Counter #Counter 함수 유용하게 사용하기
name = list(input())
name.sort()
cnt = Counter(name)

odd = 0  # 한개씩 남는거 개수 체크 -> 2개 이상일 경우 팰린드롬을 만들 수 없음 
odd_alpha = '' # 한개씩 남는 알파벳
tmp = '' # 팰린드롬 문자열 추가 하는 변수

for i in cnt : 
    if cnt[i] % 2 != 0: # Counter 함수에서 갯수가 홀수 인거 찾아내기
        odd += 1  
        odd_alpha += i
    
    for _ in range(cnt[i] // 2) : # 짝수인경우 변수에 알파벳 추가 
        tmp += i

if odd > 1 :
    print("I'm Sorry Hansoo")

elif odd == 0 : 
    print(tmp + tmp[::-1]) # tmp[::-1]로 역순 더해주면 팰린드롬 완성

else :
    print(tmp + odd_alpha + tmp[::-1])