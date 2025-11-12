import sys

n = sys.stdin.readline()
# print(input().split())
# print([i for i in input().split('')])
# array = list(map(int,input().split('')))
array = list(map(int,input().split(' ')))
array.sort()
print(array)
answer = 0 
tmp = 0 
for minute in array:
    tmp += minute
    answer += tmp
print(answer)