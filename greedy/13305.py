n = int(input())
distance = [int(i) for i in input().split()]
price_oils = [int(i) for i in input().split()]
min_oil = 999999999999
answer = 0
for i in range(0,len(distance)):
    if min_oil > price_oils[i]:
        min_oil = price_oils[i]
    answer += (min_oil * distance[i])
print(answer)
