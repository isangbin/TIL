# SWEA_동철이의 일분배
# 220927

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')


def npr(i, k, r):                                   # p[i]부터 p[r]까지를 a[0]~a[k]의 순열로 채움
    global max_cnt, cnt
    if i == r:                                      # 순열이 완성되었으면

        if cnt >= max_cnt:                          # 최댓값인지 확인
            max_cnt = cnt
        else:
            return

    elif cnt < max_cnt:                             # 가지치기
        return

    else:                                           # 완성이 아직 안되었으면 순열만들기
        for j in range(k):                          # 순회하기
            if used[j] == 0 and arr[i][j] != 0:     # 쓴적없는 숫자면

                used[j] = 1                         # 썼다는 표시 후
                cnt *= arr[i][j] / 100
                npr(i+1, k, r)                      # 다음자리 채우러가기
                used[j] = 0                         # 다음차례를 위해 원상복귀
                cnt /= arr[i][j] / 100


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    used = [0]*N

    max_cnt = 0
    cnt = 1
    npr(0, N, N)

    print('#{} {:.6f}'.format(tc, max_cnt*100))