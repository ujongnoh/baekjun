n = int(input())
num_list=[]
for i in range(n):
    num_list.append(int(input())) ## int 형으로 넣어야지만 정렬이됨
num_list.sort()
for i in range(n):
    print(num_list[i])