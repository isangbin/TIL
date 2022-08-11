# SWEA 4837 . 부분집합의 합
# 220811

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

def len_tmp(i): # 리스트의 길이 재는 함수
    len_tmp = 0
    for _ in i :
        len_tmp += 1
    return len_tmp

def sum_tmp(i): # 리스트 내부 원소들의 총합 구하는 함수
    sum_tmp = 0
    for _ in i :
        sum_tmp += _
    return sum_tmp

for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    tmp = []
    tmp_list = []

    for i in range(1<<12): # 부분집합 총 개수
        for j in range(12): # 부분집합 1개 생성
            if i & (1<<j): # 각 부분집합에 요소 추가
                tmp.append(A[j])

        tmp_list.append(tmp) # 부분집합 모음에 부분집합 추가
        tmp = []

    ans = 0
    for i in tmp_list : # 각 부분집합에 대하여
        if (len_tmp(i) == N) and (sum_tmp(i) == K) : # 길이가 N, 합이 K일 경우
            ans += 1

    print('#{} {}'.format(tc, ans))
