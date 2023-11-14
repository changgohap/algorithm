import sys
input = sys.stdin.readline

def check(a, b):

    global man_list

    cnt = 1

    for i in man_list:
        if i[장0] > a and i[1] > b:
            cnt += 1

    return cnt

N = int(input())

man_list = []

for _ in range(N):
    a, b = map(int, input().split())
    man_list.append([a, b])

# 위치를 기억한 후 순위값을 저장해 줄 배열 생성
memo = [0 for _ in range(N)]

# check 함수에서 본인보다 큰수를 + 카운팅 한 후 memo에 저
for i in range(N):
    memo[i] += check(man_list[i][0], man_list[i][1])

print(*memo)
