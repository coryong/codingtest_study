#구명보트 초안
def solution(people, limit):
    people.sort(reverse=True)
    count=0
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            if (people[i]+people[j])<limit+1:
                people[i]=250
                people[j]=250
                count+=1
            elif j==len(people)-1 and people[j]!=250 :
                people[i]=250
                count+=1
                break
            print(i,j,people,count)
    for i in people:
        if i!=250:
            count+=1
    return count

# 구명보트
def solution(people, limit):
    people.sort()
    answer = 0
    i=0
    j=len(people)-1
    while i<=j:
        if people[i]+people[j]<=limit:
            i=i+1
        j-=1
        answer+=1
    return answer

# 큰 수 만들기
def solution(number, k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1]<num :
            answer.pop()
            k-=1
        answer.append(num)
    k=''
    for num in answer:
       k =k+str(num)
    return k

#즐겨찾기가 가장 많은 식당 정보
-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN
(SELECT FOOD_TYPE,MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC