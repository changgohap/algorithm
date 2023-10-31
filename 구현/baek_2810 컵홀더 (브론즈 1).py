import sys
input = sys.stdin.readline

N = int(input())
seat = input()

cnt = 0
l_cnt = 0
for i in seat:
    if i == 'L' and l_cnt == 0:
        l_cnt += 1
    elif i == 'L' and l_cnt == 1:
        cnt += 1
        l_cnt = 0

if cnt == 0:
    print(N)
else:
    print(N+1-cnt)
