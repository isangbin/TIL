# SWEA_5097. 회전
# 220825

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 맨 앞 숫자는 작업이 N번 이루어지면 다시 맨 앞으로 온다.
    # 따라서 M % N 번 수행 한 것과 결과가 같다.
    # 이 때 맨 앞 숫자는 M % N을 idx로 갖는 숫자이다.

    print('#{} {}'.format(tc, nums[M % N]))