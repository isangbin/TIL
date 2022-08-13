# SWEA 1966. 숫자를 정렬하자
# 220811
'''
우로 3칸이 1, 그뒤로 0 또는 벽
아래로 3칸이 1, 그 뒤로 0 또는 벽
'''
# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

for tc in range(1, TC + 1):

    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0] # 오른쪽, 아래쪽으로 움직일 delta
    dj = [0, 1]

    space = 0
    for i in range(N):
        for j in range(N):
