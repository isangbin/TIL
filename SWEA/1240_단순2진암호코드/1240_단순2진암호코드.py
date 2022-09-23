# SWEA_1240. 단순 2진 암호코드
# 220920

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        x = list(str(input()))
        arr.append(x)

    tmp = []
    for i in range(N-1, -1, -1):                # 뒤에서부터 읽어서 1이 나오는 순간
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                for k in range(55, -1, -1):     # 거기부터 56개의 코드를 저장함
                    tmp.append(arr[i][j-k])
                break

    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    pw = [[''] for _ in range(8)]
    for i in range(8):
        a = ''
        for j in range(i*7, (i+1)*7):           # 추출한 암호코드를 7개씩 묶음
            a += tmp[j]
        pw[i] = a

    ans = []
    for i in pw:                                # 7개씩 묶인 8개의 암호를 해당 의미를 갖는 숫자로 변환
        ans.append(code.index(i))

    odd = 0
    even = 0
    for i in range(8):                          # 짝수번째 숫자와 홀수번째 숫자를 나눔 (짝수번째 idx가 홀수번째 숫자임)
        if i % 2 == 0:
            odd += ans[i]
        else:
            even += ans[i]

    result = odd * 3 + even
    if result % 10 == 0:                        # 올바른 암호 조건에 맞는지 확인 후 그에 맞는 출력
        print('#{} {}'.format(tc, sum(ans)))
    else:
        print('#{} {}'.format(tc, 0))