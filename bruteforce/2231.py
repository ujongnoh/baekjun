n = int(input())
# 101x + 11y + 2z = answer
for i in range(1,n+1):
    sumnum = 0
    for j in str(i):
        sumnum += int(j)
    if i + sumnum == n :
        print(i)
        break
    if i == n:
        print(0)