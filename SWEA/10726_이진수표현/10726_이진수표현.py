# SWEA_10726. 이진수 표현
# 220920

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    m = list(str(bin(M)))
    m.pop(0)
    m.pop(0)
    if len(m) < N:
        while len(m) < N:
            m.insert(0, '0')

    ans = 'ON'
    for i in range(len(m)-1, len(m)-N-1, -1):
        if m[i] != '1':
            ans = 'OFF'
            break

    print('#{} {}'.format(tc, ans))