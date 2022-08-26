# SWEA_1226. 미로1
# 220825

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')


def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    queue = []
    queue.append((i, j))  # 시작점 enqueue

    while queue:
        # dequeue
        i, j = queue.pop(0)
        # 도착점이 3이면 반복 종료
        if maze[i][j] == '3':
            # 도착까지 통과한 칸 수는 도착까지의 거리 - 1이다.
            return 1

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 4방향에 대해 조사
            ni, nj = i + di, j + dj
            # 이동할 곳이 범위안에 있고 벽(1)이 아니면서 방문한적 없을 경우
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                queue.append((ni, nj))  # enqueue
                visited[ni][nj] = visited[i][j] + 1  # 출발점으로부터 몇번만에 도착한 건지 기록
    # queue가 비었는데 발견이 안된경우는 길이 없음을 의미함
    return 0

for tc in range(1, 10+1):

    TC = int(input())
    maze = [list(input()) for _ in range(16)]

    a, b = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                a = i
                b = j

    print('#{} {}'.format(tc, bfs(a, b, 16)))