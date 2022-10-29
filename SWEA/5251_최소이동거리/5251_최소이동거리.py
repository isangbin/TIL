# SWEA_5251. 최소이동거리
# 220929

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def dijk(start, end):

    Used = [start]                                                      # 최단거리를 알아낸 녀석들
    D[start] = 0                                                        # 출발점의 최단거리는 0
    for v in range(1000):                                               # 일단 출발점으로부터의 거리를 D에 저장
        D[v] = roads[start][v]

    while end not in Used:                                              # 목표지점까지의 최단거리를 알아낼 때 까지만 수행
        small = 10002                                                   # 이번 순회에서 가장 가까운녀석까지의 거리
        small_idx = 0                                                   # 그놈의 번호
        for i in range(1000):                                           # 모든 정점에 대하여
            if i not in Used and D[i] < small:                          # 최단거리 알아낸적 없는놈인데 지금까지중 가장 가깝다면?
                small = D[i]                                            # 가장 가까운녀석 후보 등록
                small_idx = i                                           # 그놈 번호도 기억
        Used.append(small_idx)                                          # 다돌면 가장 가까운녀석이 뽑혔을 것이고 그녀석을 Used에 추가

        for v in range(1000):                                           # 모든 정점에 대하여
            D[v] = min(D[v], D[small_idx] + roads[small_idx][v])        # 이전단계에서의 그 정점까지 거리와 방금 뽑은녀석을 지나는 길의 거리중 짧은 것을 D에 저장


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    roads = [[11]*1000 for _ in range(1000)]
    for i in range(E):
        s, e, w = map(int, input().split())
        roads[s][e] = w

    D = [10001]*1000
    dijk(0, N)
    print('#{} {}'.format(tc, D[N]))
