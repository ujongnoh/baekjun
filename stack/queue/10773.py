import sys

input = sys.stdin.readline

n = int(input())

answer = []
for _ in range(n):
    i = int(input())
    if i > 0:
        answer.append(i)
    else :
        answer.pop(-1)
print(sum(answer))