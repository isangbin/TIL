# SWEA_1265. 달란트2
# 220913

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    x = N // P  # 몫
    y = N % P   # 나머지

    ans = x ** (P-y) * (x+1) ** y

    print('#{} {}'.format(tc, ans))