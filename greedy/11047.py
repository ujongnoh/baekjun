import sys

input = sys.stdin.readline

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
index, answer = [0,0]

print(coins)
while k != 0:
    if coins[index] <= k :
        k = k - coins[index]
        answer += 1
    else :
        index += 1
    print(answer)
    