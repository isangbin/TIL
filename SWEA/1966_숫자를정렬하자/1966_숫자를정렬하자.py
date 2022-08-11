# SWEA 1966. 숫자를 정렬하자
# 220811

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

for tc in range(1, TC + 1):

    N = int(input()) # 숫자의 개수
    nums = list(map(int, input().split()))

    for i in range(N-1, 0, -1) : # 버블 정렬
        for j in range(0, i) :
            if nums[j] > nums[j+1] :
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print('#{}'.format(tc), end=' ')
    for i in nums:
        print(i, end=' ')
    print()