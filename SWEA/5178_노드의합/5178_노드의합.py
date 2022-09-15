# SWEA_5178. 노드의 합
# 220915

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def num(n):
    global ans
    ans = 0
    if nodes[n] == 0:                   # 리프노드가 아니라면 자식들의 합을 반환
        if 2*n+1 <= N:                  # 자식이 하나일 경우
            ans = num(2*n) + num(2*n+1)
        else:                           # 자식이 둘일 경우
            ans = num(2*n)
        return ans
    else:                               # 리프노드라면 본인의 값을 반환
        ans = nodes[n]
        return ans

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    nodes = [0]*(N+1)
    for i in range(M):
        tmp = list(map(int, input().split()))
        nodes[tmp[0]] = tmp[1]

    print('#{} {}'.format(tc, num(L)))
