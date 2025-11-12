from itertools import combinations

n, m = map(int, input().split())
card_list = sorted(map(int, input().split()))
answer = 0


for i in range(n-2):
    left, right = i+1, n-1
    while left > right :
        total = card_list[i] + card_list[left] + card_list[right]
        if total > m :
            right -= 1
        else : 
            left += 1
            answer = max(answer,total)
        if answer == m :
            break
    if answer == m :
        break


