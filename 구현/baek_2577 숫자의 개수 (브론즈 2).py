import sys
input = sys.stdin.readline

num = 1
for _ in range(3):
    i = int(input())
    num = num * i

# 순환을 위해 num 을 str로 변환
num = str(num)

# 0~9를 카운팅하기 위한 index list 설정
index = [0 for _ in range(10)]

# 각 자릿수의 숫자에 맞는 index에 1씩 추가
for i in num:
    index[int(i)] += 1

for j in index:
    print(j)