# SWEA_4366. 정식이의 은행업무
# 220920

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bi = list(str(input()))
    tri = list(str(input()))

    bi.reverse()                            # 반전시키면 인덱스가 각 자릿수의 제곱수가됨
    tri.reverse()                           # ex. idx 2는 3**2의 자릿수

    bi_dec = 0
    for i in range(len(bi)):                # 잘못 기억한 2진수 숫자가 몇인지
        bi_dec += (2**i) * int(bi[i])

    tri_dec = 0
    for i in range(len(tri)):               # 잘못 기억한 3진수 숫자가 몇인지
        tri_dec += (3**i) * int(tri[i])


    tris = []
    for i in range(len(tri)):               # 원래 숫자가 될 수 있는 경우를 tris에 저장
        if tri[i] == '2':
            tris.append(tri_dec - (3**i))
            tris.append(tri_dec - 2*(3**i))
        elif tri[i] == '1':
            tris.append(tri_dec - (3**i))
            tris.append(tri_dec + (3**i))
        else:
            tris.append(tri_dec + (3**i))
            tris.append(tri_dec + 2*(3**i))

    ans = 0
    for i in range(len(bi)):                # 2진수에 대해서도 같은 작업을 반복하되,
        if bi[i] == '1':                    # 3진수에서의 경우의 수와 같은 숫자가 나오면
            tmp = bi_dec - (2**i)           # 그것이 정답이 된다고 생각할 수 있음
            if tmp in tris:
                ans = tmp
                break
        else:
            tmp = bi_dec + (2**i)
            if tmp in tris:
                ans = tmp
                break

    print('#{} {}'.format(tc, ans))