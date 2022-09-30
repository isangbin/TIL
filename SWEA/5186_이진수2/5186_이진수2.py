# SWEA_5186. 이진수2
# 220920

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    ans = ''
    cnt = -1
    while True:
        if N == 2**cnt:
            ans += '1'
            break
        elif N > 2**cnt:
            N = N - 2**cnt
            ans += '1'
            cnt -= 1
        else:
            ans += '0'
            cnt -= 1

        if cnt < -12:
            ans = 'overflow'
            break

    print('#{} {}'.format(tc, ans))

