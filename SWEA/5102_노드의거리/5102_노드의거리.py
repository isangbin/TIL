# SWEA_5102. 노드의 거리
# 220825

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input())

def bfs(S, V, G):   # v시작, N마지막정점번호, t찾는정점
    visited = [0] * (V+1)
    queue = []
    queue.append(S)

    while queue:                            # q가 빌때까지 돌림
        S = queue.pop(0)                     # dequeue
        if S == G:
            return visited[S]               # 목표 발견시 몇번만에 발견한건지 리턴 (발견하자마자 나가므로 자동으로 최솟값임)
        for i in nodes[S]:                  # 인접점 enqueue
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[S] + 1 # 출발지로부터 몇 번만에 온 건지 기록

    return 0                                # while다돌리고 목표 못찾았으면 0 리턴

for tc in range(1, TC+1):
    V, E = map(int, input().split())

    nodes = [[] for _ in range(V+1)]        # 0번 노드는 신경안쓸 예정

    for i in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S, V, G)))