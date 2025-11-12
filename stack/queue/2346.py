from collections import deque

N = int(input())
papers = list(map(int, input().split()))
result = []
# 풍선 번호와 종이 값을 함께 저장
balloons = deque((i+1, papers[i]) for i in range(N))

while balloons :
    num, move = balloons.popleft()
    result.append(num)
    if move > 0 :            
        balloons.rotate((-1 * move) +1 )

    else :
        balloons.rotate(-1 * move)

print(" ".join(map(str,result)))
## 123 4 5
## 321-3-1

##  4 5 2 3
## -3-1 2 1

##  5 2 3
## -1 2 1

# 3 2
# 1 2

    
