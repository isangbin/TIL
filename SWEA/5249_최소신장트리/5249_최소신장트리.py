# SWEA_5249. 최소신장트리
# 220929

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    val = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        val.append([n1, n2, w])

    val.sort(key=lambda x: x[2])

    rep = [i for i in range(V+1)]
    N = V+1
    cnt = 0
    total = 0
    for n1, n2, w in val:
        if find_set(n1) != find_set(n2):
            cnt += 1
            union(n1, n2)
            total += w
            if cnt == N-1:
                break

    print('#{} {}'.format(tc, total))