import sys
input = sys.stdin.readline

goal = int(input())
minnum = 1
temp_stack = []
array = list(map(int,input().split(' ')))

while goal != minnum :
    if temp_stack and temp_stack[-1] == minnum:
        temp_stack.pop()
        minnum = minnum + 1
        continue
    
    if minnum == array[0] :
        array.pop(0)
        minnum = minnum + 1
    else :
        temp_stack.append(array.pop(0))
    
    if len(array) == 0 and temp_stack[-1] != minnum :
        break

if goal == minnum : 
    print("Nice")
else :
    print("Sad")

