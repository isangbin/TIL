# SWEA_5688. 세제곱근을 찾아라
# 220916

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    i = int(N ** (0.33))                  # N의 3제곱근에 가장 가까운 정수에서 시작
    ans = 0

    while True:
        if i ** 3 == N:                 # i의 세제곱이 N이면 끝
            ans = i
            break
        elif i ** 3 > N:                # i의 세제곱이 N보다 커지면 N의 세제곱근은 정수가 아니므로 -1
            ans = -1
            break
        else:                           # i의 세제곱이 N보다 작으면 i+1에 대해 다시 시작
            i = i+1
    print('#{} {}'.format(tc, ans))