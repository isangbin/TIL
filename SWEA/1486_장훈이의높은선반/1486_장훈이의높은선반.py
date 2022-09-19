# SWEA_1486. 장훈이의 높은 선반
# 220916

# 정답 코드
import sys  # [1, 2, 3, 4, 5] = human
sys.stdin = open('input.txt', 'r')

def stacking(i, N, summ, B):                    # i=현재 인덱스, N=원소 갯수, summ=지금까지의 합, B=선반 높이
    global ans                                  # 선반보다 높은 경우의 수중 가장 작은 값
    if i == N:                                  # 마지막원소까지 고려가 완료된 후이면
        if summ >= B:                           # 합이 선반보다 높을경우
            if ans >= summ:                     # 현재의 ans(최소값) 보다 작으면               summ =
                ans = summ                      # ans를 갱신
        return                                  # 경우의수 종료

    elif summ >= ans:                           # 도중에 키의 합이 ans를 넘어갈 경우 가지치기
        return                                  # 종료

    else:                                       # 원소도 남아있고 키의 합도 B에 도달하지 않은 경우
        stacking(i+1, N, summ+human[i], B)      # 다음 사람을 얹는 경우              [1, ] summ =0+1 -> stacking(2,summ)
        stacking(i+1, N, summ, B)               # 다음 사람을 안얹는 경우             [ ] summ= 0 -> stacking(2, summ)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    human = list(map(int, input().split()))

    ans = 100000000
    summ = 0                                    # 키의 합
    stacking(0, N, summ, B)

    print('#{} {}'.format(tc, ans - B))