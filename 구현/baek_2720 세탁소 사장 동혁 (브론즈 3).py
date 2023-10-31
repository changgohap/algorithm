import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    change = int(input())

    result = []
    if change >= 25:
        result.append(change//25)
        change = change % 25
    else:
        result.append(0)
    if change >= 10:
        result.append(change//10)
        change = change % 10
    else:
        result.append(0)
    if change >= 5:
        result.append(change//5)
        change = change % 5
    else:
        result.append(0)
    if change >= 1:
        result.append(change//1)
    else:
        result.append(0)

    for i in result:
        print(i, end=' ')

