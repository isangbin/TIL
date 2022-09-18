# SWEA_1861. 정사각형 방
# 220915

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

def move(i, j):
    global cnt
    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni = i + di
        nj = j + dj
        # print('1cnt:{}, i:{}, j:{}, ni:{}, nj:{}'.format(cnt, i, j, ni, nj))
        if 0<=ni<N and 0<=nj<N and rooms[i][j]+1 == rooms[ni][nj]:
            cnt += 1
            # print('2cnt:{}, i:{}, j:{}, ni:{}, nj:{}'.format(cnt, i, j, ni, nj))
            move(ni, nj)
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        rooms.append(tmp)

    max_cnt = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            # print('초기화! cnt:{}, i:{}, j:{}'.format(cnt, i, j))
            move(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                ans = rooms[i][j]
            elif max_cnt == cnt:
                if ans > rooms[i][j]:
                    ans = rooms[i][j]

    print('#{} {} {}'.format(tc, ans, max_cnt))
