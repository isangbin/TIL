# SWEA 2001. 파리 퇴치
# 220811

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

for tc in range(1, TC + 1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    for i in range(N-M+1): # N*N필드에 대하여 (해당 위치에서 M*M만큼 볼 것이므로 indexerror방지
        for j in range(N-M+1):
            fly = 0
            for di in range(M): # M*M 속 파리의 총 마릿수
                for dj in range(M):
                    fly += arr[i+di][j+dj]
            if max_fly <= fly: # 최댓값 갱신
                max_fly = fly

    print('#{} {}'.format(tc, max_fly))