import sys

input = sys.stdin.readline

while True:
    text=input()
    temp_text= ""
    par_array = []
    if len(text) == 0 :
        break
    for alpabet in text:
        if alpabet == "[" or alpabet == "]" or alpabet == "(" or alpabet == ")" :
            temp_text = temp_text + alpabet
    if temp_text == "":
        print("yes")
        continue
    for par in temp_text:
        par_array.append(par)

        if len(par_array) > 1:
            if par_array[-2] == '(' and par_array[-1] == ')':
                par_array = par_array[:-2]
        if len(par_array) > 1:
            if par_array[-2] == '[' and par_array[-1] == ']':
                par_array = par_array[:-2]
    if len(par_array) == 0:
        print("yes")
    else :
        print("no")


