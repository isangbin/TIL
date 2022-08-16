# SWEA_3143. 가장 빠른 문자열 타이핑
# 220816


# 정답코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    A, B = input().split()
    a, b = list(A), list(B)
    # len(A)
    len_a = 0
    for i in a :
        len_a += 1

    # len(B)
    len_b = 0
    for i in b :
        len_b += 1

    tmp = ''
    cnt = 0
    # A 안에 B가 몇 번 들어가있는지 조사
    for i in range(len_a - len_b + 1) :
        tmp = a[i:i+len_b:1]

        # 글자가 겹치는 경우를 방지
        if tmp == b :
            cnt += 1
            a[i:i+len_b:1] = [0]*len_b

    # 정답 계산

    ans = len_a - (len_b * cnt) + cnt

    print('#{} {}'.format(tc, ans))

