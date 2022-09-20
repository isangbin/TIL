# SWEA_4012. 요리사
# 220916

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def cal(food):
    sy1 = []
    sy2 = []
    for i in foods:                             # 음식 반갈
        if i in food:
            sy1.append(i)
        else:
            sy2.append(i)

    sum1 = 0
    sum2 = 0
    for i in range(N//2):                       # 각 그룹의 음식 시너지 합을 모두 더함
        for j in range(N//2):
            sum1 += synergy[sy1[i]][sy1[j]]
            sum2 += synergy[sy2[i]][sy2[j]]

    taste = abs(sum1 - sum2)                    # 그 차를 반환
    return taste


def pick(i, N, food):                           # i=현재 인덱스, N=총 재료수, food=고른음식수
    global ans
    if i == N:                                  # 다 돌았는데
        if len(food) == N // 2:                 # 고른 재료 갯수가 전체의 절반이면
            # print(food)
            tmp = cal(food)                           # 시너지합계산
            if ans >= tmp:
                ans = tmp
        return

    elif len(food) > N // 2:                    # 중간에 절반 이상을 골라버리면
        return                                  # 잘못된 부분집합이므로 가지치기

    else:
        pick(i+1, N, food)                      # i번 재료 안고르고 다음 재료 pick
        pick(i+1, N, food+[i])                  # i번 재료 고르고 다음 재료 pick

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    foods = list(range(N))
    synergy = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        synergy.append(tmp)

    ans = 1000000
    food = []
    pick(0, N, food)

    print('#{} {}'.format(tc, ans))


