# SWEA_4861. 회문
# 220816


# 정답코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    N, M = map(int, input().split())
    letters = [list(input()) for _ in range(N)]

    tmp = []
    a = ''
    b = ''
    ans = ''
    # 세로방향 조사
    for i in range(N-M+1) :
        for j in range(N) :
            for k in range(M) :
                tmp.append(letters[i+k][j])
            # 조사 내용이 회문인지 검사
            a = ''.join(tmp)
            tmp.reverse()
            b = ''.join(tmp)
            if a == b :
                ans = a
                break
            else :
                tmp = []

    # 가로방향 조사
    for j in range(N-M+1) :
        for i in range(M) :
            for k in range(M) :
                tmp.append(letters[i][j+k])
            # 조사 내용이 회문인지 검사
            a = ''.join(tmp)
            tmp.reverse()
            b = ''.join(tmp)
            if a == b :
                ans = a
                break
            else:
                tmp = []

    print('#{} {}'.format(tc, ans))
