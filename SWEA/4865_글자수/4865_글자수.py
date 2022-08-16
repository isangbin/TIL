# SWEA_4865. 글자수
# 220816


# 정답코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    str1 = input()
    str2 = input()

    cnt = 0
    cnt_list = []

    # str1의 각 글자에 대하여 str2에 몇개씩 있는지 조사
    for i in str1 :
        for j in str2 :
            if i == j :
                cnt += 1
        cnt_list.append(cnt)
        cnt = 0

    # 각 글자의 개수중 최댓값 선정
    max_cnt = 0
    for cnt in cnt_list :
        if max_cnt <= cnt :
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt))