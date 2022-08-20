# SWEA_9489. 고대 유적
# 220812

# 정답코드

import sys

sys.stdin = open('input.txt', 'r', encoding='UTF8')

TC = int(input())
for tc in range(1, TC+1) :
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    cnt_list = []
    for i in range(N) : # 가로로 늘어선 1들의 길이 측정
        for j in range(M-1) :
            if field[i][j] == 1 and field[i][j+1] == 1 :
                cnt += 1
                cnt_list.append(cnt)
            else : 
                cnt = 0
    
    for i in range(N-1) : # 세로로 늘어선 1들의 길이 측정
        for j in range(M) :
            if field[i][j] == 1 and field[i+1][j] == 1 :
                cnt == 1
                cnt_list.append(cnt)
            else :
                cnt = 0

    max_cnt = 0
    for i in cnt_list :
        if max_cnt <= i :
            max_cnt = i
    
    print('#{} {}'.format(tc, max_cnt))