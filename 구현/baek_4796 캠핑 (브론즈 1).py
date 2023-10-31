import sys
input = sys.stdin.readline

cnt = 1
while True:
    ava, ent, vac = map(int, input().split())
    if ava == ent == vac == 0:
        break
    if ava >= vac % ent:
        print(f'Case {cnt}:', (vac % ent) + ((vac // ent)*ava))
    else:
        print(f'Case {cnt}:', ava + ((vac // ent) * ava))
    cnt += 1