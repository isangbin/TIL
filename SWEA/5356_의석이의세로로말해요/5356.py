# SWEA_5356. 의석이의 세로로 말해요
# 220816


# 정답코드
import sys
sys.stdin = open('sample_input.txt', 'r')

# len 함수
def llen(a) :
    x = 0
    for i in a :
        x += 1
    return x

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    letters = [list(input()) for _ in range(5)]

    # letters 중 가장 길이가 긴 것의 len 구하기
    longest = 0
    for i in letters :
        if longest <= llen(i) :
            longest = llen(i)

    ans = ''
    for k in range(longest) :
        for i in letters :
            if llen(i) >= k+1 : # i[k]가 존재한다면
                ans += str(i[k]) # ans에 그걸 더한다.

    print('#{} {}'.format(tc, ans))