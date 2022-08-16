# SWEA_4864. 문자열비교
# 220816


# 정답코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    str1 = list(input())
    str2 = list(input())

    # str1의 길이
    len_str1 = 0
    for i in str1 :
        len_str1 += 1

    # str2의 길이
    len_str2 = 0
    for i in str2 :
        len_str2 += 1

    tmp = []
    ans = 0
    # str2의 각 자리에 대하여 str1과 같은 부분이 있는지 조사
    for i in range(len_str2 - len_str1 + 1) : # indexError 방지
        for j in range(len_str1) :
            tmp.append(str2[i+j])
        # str2의 각 자리로부터 len(str1)만큼의 문자열이 str1과 같은지 여부
        if tmp == str1 :
            ans = 1
        else :
            tmp = []

    print('#{} {}'.format(tc, ans))