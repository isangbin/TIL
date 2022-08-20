# SWEA_9367. 점점 커지는 당근의 개수
# 220812

# 정답코드

import sys

sys.stdin = open('input.txt', 'r', encoding='UTF8')

TC = int(input())
for tc in range(1, TC+1) :

    carrots = int(input())
    sizes = list(map(int, input().split()))

    cnt = 1
    cnt_list = []
    for i in range(1, carrots) : # 이전 당근과 비교할 거라서 idx(1)부터 시작
        if sizes[i] > sizes[i-1] : # 이전 당근보다 크기가 크면
            cnt += 1                # cnt에 1 더한다
            cnt_list.append(cnt)    # 리스트에 저장
        else :                      # 작아진 경우는
            cnt = 1                 # cnt 초기화
    max_cnt = 1                     # 최댓값 차출
    for i in cnt_list :
        if max_cnt <= i :
            max_cnt = i

    print('#{} {}'.format(tc, max_cnt))