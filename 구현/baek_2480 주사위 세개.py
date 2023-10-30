import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))

dice.sort()

tmp = 0 # 체크용 변수
result = 0 # 중복있을시 곱해야할 기준 값 설정
cnt = 0

for i in dice:
    if i == tmp:
       cnt += 1
       result = i
    else:
        tmp = i

if cnt == 0:
    print(max(dice) * 100)
elif cnt == 1:
    print(1000 + (result * 100))
else:
    print(10000 + (result * 1000))
