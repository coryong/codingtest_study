def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    length = len(people)-1
    count = 0
    for i in range(length):
        if(i>=length):
            break
        if(people[i]+people[length] <= limit):
            length -= 1
            count += 1
    return len(people)-count