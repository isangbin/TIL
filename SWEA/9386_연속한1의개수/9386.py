# SWEA_9386. 연속된 1의 개수
# 220812

# 정답코드

import sys

sys.stdin = open('input.txt', 'r', encoding='UTF8')

TC = int(input())
for tc in range(1, TC+1) :
    N = int(input())
    nums = input()
    
    cnt = 0
    cnt_list = []
    for i in range(N) : 
        if nums[i] == '1' : # 1을 만나면
            cnt += 1 # cnt에 1 더한 뒤
            cnt_list.append(cnt) # 리스트에 추가
        else : # 0을 만나면
            cnt = 0 # cnt를 초기화
    
    max_cnt = 0
    for i in cnt_list : # 리스트 내에 저장된 숫자중 가장 큰 값을 선정
        if max_cnt <= i :
            max_cnt = i

    print('#{} {}'.format(tc, max_cnt))