# SWEA_4869. 종이붙이기
# 2022-08-18
'''
함수 이름은 Fib인데 피보나치로 풀지 않아버린 것...
'''
# 정답코드
import sys
sys.stdin = open('sample_input.txt','r')

TC = int(input())

def Fib(n):

    if n == 1:                      # 10이면 1 (초기값)
        return 1
    elif n == 2:                    # 20이면 3 (초기값)
        return 3
    elif n % 2 == 0:                # 짝수번째는 이전항*2+1
        return Fib(n-1) * 2 + 1
    else:                           # 홀수번째는 이전항*2-1
        return Fib(n-1) * 2 - 1

for tc in range(1, TC+1):
    N = int(input())
    n = N//10
    print('#{} {}'.format(tc, Fib(n)))
