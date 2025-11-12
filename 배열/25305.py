number,cut = list(map(int,input().split()))
scores = list(map(int,input().split()))

scores.sort(reverse=True)
print(scores[cut-1])