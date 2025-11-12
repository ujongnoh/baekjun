N = list(map(int,(input().split(' '))))
from collections import deque
# print(N)
array = deque([str(i) for i in range(1,N[0]+1)])
answer = []
index = int(N[1])
count =1

while array:
    if count == index:
        answer.append(array.popleft())
        count =1
    else :
        array.append(array.popleft())
        count += 1


print('<' + ', '.join(answer)+">")