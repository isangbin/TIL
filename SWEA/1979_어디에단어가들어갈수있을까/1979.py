# SWEA_1979. 어디에 단어가 들어갈 수 있을까
# 2022-08-19

# 정답코드
import sys
sys.stdin = open('input.txt','r')

TC = int(input())

# 1이 K개가 나오면 1, 아니면 0을 return (가로용)
def wow(i, j):
    wow = []
    for k in range(K):
        wow.append(puzzle[i][j+k])
    for k in wow:
        if k == 0:
            return 0
    else:
        return 1

# 1이 K개가 나오면 1, 아니면 0을 return (세로용)
def wow2(i, j):
    wow = []
    for k in range(K):
        wow.append(puzzle[i+k][j])
    for k in wow:
        if k == 0:
            return 0
    else:
        return 1

for tc in range(1, TC+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 가로로 K글자 자리 조사
    for i in range(N):
        for j in range(N-K+1):
            # 왼벽에 붙은 경우 1이 K개, 그 다음 0이면 인정
            if j == 0:
                if wow(i, j) == 1 and puzzle[i][j+K] == 0:
                    cnt += 1
            # 오른벽에 붙은 경우 0 다음에 1이 K개면 인정
            elif j == N-K:
                if wow(i, j) == 1 and puzzle[i][j-1] == 0:
                    cnt += 1
            # 그 외의 경우 0 다음 K개의 1 다음 0 나오면 인정
            else:
                if wow(i, j) == 1 and puzzle[i][j-1] == 0 and puzzle[i][j+K] == 0:
                    cnt += 1

    # 세로로 K글자 자리 조사 (가로와 같은 매커니즘)
    for i in range(N-K+1):
        for j in range(N):
            if i == 0:
                if wow2(i, j) == 1 and puzzle[i+K][j] == 0:
                    cnt += 1
            elif i == N-K:
                if wow2(i, j) == 1 and puzzle[i-1][j] == 0:
                    cnt += 1
            else:
                if wow2(i, j) == 1 and puzzle[i-1][j] == 0 and puzzle[i+K][j] == 0:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))