# SWEA_4615. 재미있는 오셀로 게임
# 220920

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def game(a, b, color):
    board[a][b] = color
    delta = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for di, dj in delta:
        ni = a + di
        nj = b + dj
        stack = []
        while 0<=ni<N and 0<=nj<N:                              # 게임판 끝까지 가서 멈춤
            if board[ni][nj] == color:                          # 나랑 같은색 만나면
                while stack:                                    # 지나온 길(스택)을 내색깔로 칠함
                    tmp = stack.pop()
                    board[tmp[0]][tmp[1]] = color
                break
            elif board[ni][nj] == 0:                            # 같은색보다 0 먼저만나면 그냥 끝
                break
            else:                                               # 다른 색이면 스택에 저장
                stack.append([ni, nj])
                ni += di
                nj += dj

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0]*N for _ in range(N)]                           # 게임 세팅
    board[N//2][N//2] = 2
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2] = 1
    
    turns = []
    for i in range(M):
        tmp2 = list(map(int, input().split()))
        tmp2[0] -= 1                                            # index 맞추기 위한 작업
        tmp2[1] -= 1
        turns.append(tmp2)
    
    for i in turns:                                             # 게임 진행
        game(i[0], i[1], i[2])
    
    black = 0
    white = 0
    for i in range(N):                                          # 게임 종료 후 돌의 갯수 세기
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    
    print('#{} {} {}'.format(tc, black, white))