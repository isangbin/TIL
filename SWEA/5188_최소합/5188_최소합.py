# SWEA_5188. 최소합
# 220921

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')
sys.setrecursionlimit(10**6)

def move(i, j):
    if i == N - 1 and j == N - 1:
        return
    else:
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + board[ni][nj]
                else:
                    if visited[ni][nj] >= visited[i][j] + board[ni][nj]:
                        visited[ni][nj] = visited[i][j] + board[ni][nj]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        board.append(tmp)

    visited = [[0]*N for _ in range(N)]
    delta = [[1, 0], [0, 1]]
    visited[0][0] = board[0][0]

    for i in range(N):
        for j in range(N):
            move(i, j)

    print('#{} {}'.format(tc, visited[N-1][N-1]))


