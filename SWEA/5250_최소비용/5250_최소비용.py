# SWEA_5250. 최소비용
# 220929

# 정답 코드
from collections import deque
import sys
sys.stdin = open('sample_input.txt', 'r')


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[100000]*N for _ in range(N)]        # visited는 1000 * 100을 넘을 수 없음
    visited[0][0] = 0

    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                tmp = visited[i][j] + 1             # 이동시 비용 1 추가
                if Hs[ni][nj] > Hs[i][j]:           # 만약 더 높은곳으로 이동했다면
                    tmp += Hs[ni][nj] - Hs[i][j]    # 높이차만큼 비용 추가

                if tmp < visited[ni][nj]:           # 만약 기록된 최소비용보다 더 작은 비용으로 도착 가능하면
                    visited[ni][nj] = tmp           # 더 작은 비용으로 갱신
                    q.append((ni, nj))              # enqueue

    return visited[N-1][N-1]                        # while문 종료후 도착점에 저장되어있는 최소비용을 리턴


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Hs = []
    for i in range(N):
        h = list(map(int, input().split()))
        Hs.append(h)

    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    print('#{} {}'.format(tc, bfs()))
