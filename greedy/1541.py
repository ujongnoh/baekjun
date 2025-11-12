
array = input()
buho = []
alpabets = []
first_minus = 0
for alpabet in array:
    if alpabet in "+-":
        buho.append(alpabet)
alpabets = list(map(int, array.replace('-',' ').replace('+',' ').split()))
# print(buho)
# print(alpabets)
for i in range(0,len(buho)):
    if buho[i] == '-':
        first_minus = i + 1
        break
if first_minus == 0:
    print(sum(alpabets))
else :
# print(sum(alpabets[:first_minus]))
# print(sum(alpabets[first_minus:]))
    print(sum(alpabets[:first_minus]) - sum(alpabets[first_minus:]))