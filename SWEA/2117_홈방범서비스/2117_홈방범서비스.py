# SWEA_2117. 홈방범서비스
# 220923

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def check(i, j, k):
    global h_cnt, ans
    for h in houses:
        if abs(i - h[0]) + abs(j - h[1]) < k:               # 현 좌표로부터 어떤 집까지의 거리가 k보다 작으면
            h_cnt += 1                                      # 그 집은 방범 범위안에 들어와 있는 것
    if (k**2 + (k-1)**2) <= h_cnt * M:                      # 범위안에 들어온 집이 비용을 충당할 수 있는 상황이면
        if ans <= h_cnt:                                    # 현재까지의 최대 집수와 비교해서 더 큰값으로 ans 갱신
            ans = h_cnt            
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                        # N: 도시크기 M: 비용

    city = [[] for _ in range(N)]
    for i in range(N):
        tmp = list(map(int, input().split()))
        city[i] = tmp

    houses = []                                             # 집이 있는 좌표
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append([i, j])
    
    ans = 0                                                 # 최종 제출될 답
    for i in range(N):
        for j in range(N):
            k = 0                                           # k는 0부터 시작해서 while문을 통해 1씩 늘어난다.
            while True:
                if (k**2 + (k-1)**2) > len(houses) * M:     # 모든 집이 포함되어도 비용을 지불할 수 없어지면 
                    break                                   # k는 더이상 늘지않고 종료된다.
                else:   
                    h_cnt = 0                               # 범위 안에 들어온 집의 개수
                    check(i, j, k)                          # 함수 발동
                    k += 1                                  # k를 1 늘려서 다시 진행

    print('#{} {}'.format(tc, ans))