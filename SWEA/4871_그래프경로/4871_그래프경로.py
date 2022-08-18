# SWEA_4871. 그래프경로
# 2022-08-18

# 정답코드
import sys
sys.stdin = open('sample_input.txt','r')

def dfs(now, N):  # N은 정점의 개수

    top = -1

    visited[now] = 1  # 시작점 방문 표시
    while True:
        for w in adjList[now]:      # v의 인접정점 중에서
            if visited[w] == 0:     # 방문기록이 없는 w가 있으면
                top += 1            # push(now)
                stack[top] = now
                now = w             # w로 위치를 이동

                visited[w] = 1      # visited[w] 방문기록을 저장
                break

        else:                       # 방문 안한 정점 w가 더이상 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                now = stack[top]    # pop()
                top -= 1
            else:                   # 스택이 비어있는 경우
                break               # 다돈거니까 끝냄

TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())        # V:노드 수, E: 간선 수

    N = V+1                                 # idx는 0부턴데 노드는 1부터라서 번호를 맞추기 위함
    adjList = [[] for _ in range(N)]        # 0번 노드는 존재만 하고 없는취급 할 것임

    for i in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)

    visited = [0] * N
    stack = [0] * N

    S,G = map(int, input().split())
    dfs(S, N)                               # 0번노드는 오지도 가지도 않을거라 무시하면 됨

    if visited[G] == 0 :
        print('#{} 0'.format(tc))
    else :
        print('#{} 1'.format(tc))