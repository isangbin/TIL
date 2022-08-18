# SWEA_1219. 길찾기
# 2022-08-18

# 정답코드
import sys
sys.stdin = open('input.txt','r')


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

# testcase는 10개
for tc in range(1, 10+1):

    TC, routes = map(int, input().split())
    N = 100
    tmp = list(map(int, input().split()))
    adjList = [[] for _ in range(100)]
    for i in range(routes) :
        adjList[tmp[i*2]].append(tmp[i*2 +1])

    visited = [0] * N  # visited 생성
    stack = [0] * N  # stack 생성
    dfs(0, N)
    if visited[99] == 1 :
        print('#{} {}'.format(TC, 1))
    else:
        print('#{} {}'.format(TC, 0))