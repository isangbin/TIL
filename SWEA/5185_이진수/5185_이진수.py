# SWEA_5185. 이진수
# 220920

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def bit_code(n):
    ans = ''
    ans += str(n // 8)
    ans += str((n % 8) // 4)
    ans += str(((n % 8) % 4 ) // 2)
    ans += str((((n % 8) % 4 ) % 2) // 1)
    return ans

T = int(input())
for tc in range(1, T+1):
    N, num = map(str, input().split())
    N = int(N)
    result = ''

    sixteen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(N):
        result += bit_code(sixteen.index(num[i]))

    print('#{} {}'.format(tc, result))