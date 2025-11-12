import sys
input = sys.stdin.readline

stack = []
output = []

n = int(input())

for _ in range(n):
    cmd = input().split()
    print(cmd)
    if cmd[0] == '1':
        stack.append(cmd[1])

    elif cmd[0] == '2':
        if stack:
            output.append(stack.pop())
        else:
            output.append('-1')

    elif cmd[0] == '3':
        output.append(str(len(stack)))

    elif cmd[0] == '4':
        output.append('0' if stack else '1')

    elif cmd[0] == '5':
        if stack:
            output.append(stack[-1])
        else:
            output.append('-1')

# 한 번에 출력
sys.stdout.write('\n'.join(output))
