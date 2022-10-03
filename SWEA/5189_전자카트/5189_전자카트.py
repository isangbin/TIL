# SWEA_5189. 전자카트
# 220922

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def npr(i, k, r):                                   # p[i]부터 p[r-1]까지를 a[0]~a[k]의 순열로 채움
    global min_cnt
    if i == r:                                      # 순열이 완성되었으면 p는 [0, 1, 2, 3, 4, 0]의 형태.
        cnt = 0
        print(p)
        for n in range(len(p)-1):                   # 01, 12, 23, 34, 40의 비용을 더한다.
            cnt += charge[p[n]][p[n+1]]
            if cnt >= min_cnt:
                return
        if cnt <= min_cnt:
            min_cnt = cnt

    else:                                           # 완성이 아직 안되었으면 순열만들기
        for j in range(k):                          # 순회하기
            if used[j] == 0:                        # 쓴적없는 숫자면
                used[j] = 1                         # 썼다는 표시 후
                p[i] = a[j]                         # i번째 자리는 a[j]로 채움
                npr(i+1, k, r)                      # 다음자리 채우러가기
                used[j] = 0                         # 다음차례를 위해 원상복귀

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    charge = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        charge.append(tmp)

    used = [0]*N
    a = list(range(1, N))
    p = [0]*(N+1)                                   # 0~N번 인덱스 존재
    min_cnt = 100*N
    npr(1, N-1, N)                                  # p[0], p[N]은 0으로 고정, p[1]~p[N-1]을 순열로 채움

    print('#{} {}'.format(tc, min_cnt))