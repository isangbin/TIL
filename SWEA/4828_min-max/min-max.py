# 4828. min-max
# 220809

'''
최댓값과 최솟값을 각각 저장한 뒤 차를 출력
'''

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # tc 수

for tc in range(1, N+1) :

    Len = int(input())
    nums = list(map(int, input().split()))

    min_num = nums[0] # 최솟값을 저장할 곳
    max_num = 0 # 최댓값을 저장할 곳

    for i in range(0, Len) :
        if min_num >= nums[i] : # nums[i]가 이전최솟값보다 작으면 갱신
            min_num = nums[i]
        elif max_num <= nums[i] : # nums[i]가 이전최댓값보다 크면 갱신
            max_num = nums[i]
        else :
            continue
    
    ans = max_num - min_num

    print('#{} {}' .format(tc, ans))
