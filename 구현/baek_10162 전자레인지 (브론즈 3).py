import sys
input = sys.stdin.readline

time = int(input())

T = [300, 60, 10]

result = []
for i in T:
    result.append(time // i)
    time = time % i

if time != 0:
    print(-1)
else:
    print(*result)