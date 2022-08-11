# SWEA 4836. 색칠하기
# 220811

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

for tc in range(1, TC + 1):
    N = int(input())
    areas = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        areas.append(tmp)
    total_area = list([0]*10 for _ in range(10))

    # 빨간색을 먼저 칠한다.
    for area in areas: # N개의 각 영역에 대하여
        if area[4] == 1: # 빨간색영역이면
            for a in range(area[0], area[2]+1): # 영역 내부를
                for b in range(area[1], area[3]+1):
                    total_area[a][b] = area[4] # 빨간색으로 칠한다.

    # 그 뒤 파란색을 칠한다. (빨,파를 같은 for문에 넣으면 이 코드의 경우 파란영역을 빨강이 1로 바꿔버리는 상황 발생)
    for area in areas:
        if area[4] == 2: # 파란색영역이면
            for a in range(area[0], area[2]+1): # 영역 내부를
                for b in range(area[1], area[3]+1):
                    if total_area[a][b] < 2: # 빨간색이거나 안칠해진 영역에 대해서만
                        total_area[a][b] += area[4] # 파란색을 덧칠한다.

    cnt = 0
    for i in range(10):
        for j in range(10):
            if total_area[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))

