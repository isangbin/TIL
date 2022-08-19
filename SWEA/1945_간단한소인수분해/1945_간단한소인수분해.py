# SWEA_1945. 간단한 소인수 분해
# 2022-08-19

# 정답코드
import sys
sys.stdin = open('input.txt','r')

TC = int(input())
n = [2, 3, 5, 7, 11]

for tc in range(1, TC+1):
    N = int(input())
    i = 0
    num = [0, 0, 0, 0, 0]   # abcde

    for i in range(5):
        while N > 1:
            if N % n[i] == 0:
                N = N // n[i]
                num[i] += 1

            else :
                break

    print('#{}'.format(tc), end=' ')
    print(*num)