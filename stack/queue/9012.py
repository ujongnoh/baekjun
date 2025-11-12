import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    
    vps = input()
    while vps.find('()') != -1 :

        vps = vps.replace('()','').strip()
    if len(vps) == 0:
        print("YES")
    else :
        print("NO")