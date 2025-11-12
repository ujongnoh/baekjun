answer = []
for i in range(5):
    N = int(input())
    answer.append(N)
print(int(sum(answer)/5))
answer.sort()
print(answer[2])