import sys
import heapq as hq
input = sys.stdin.readline

def solution(m, cards):
    # 왼쪽 오른쪽 비교해서 작은 값을 더한뒤에 pop and push
    hq.heapify(cards)
    for _ in range(m):
        card1 = cards[0]
        hq.heappop(cards)
        card2 = cards[0]
        hq.heappop(cards)

        # 새로운 카드 2개를 생성해서 push
        new_card1, new_card2 = card1 + card2, card1+card2
        hq.heappush(cards, new_card1)
        hq.heappush(cards, new_card2)
    
    result = sum(cards)
    return result

n, m = map(int, input().split())
cards = list(map(int, input().split()))
print(solution(m, cards))
