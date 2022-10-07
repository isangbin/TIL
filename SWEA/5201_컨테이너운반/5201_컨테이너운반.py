# SWEA_5201. 컨테이너 운반
# 220922

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    con = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    con.sort(reverse=True)                          # 큰놈이 앞에오게 정렬
    truck.sort(reverse=True)
    cnt = 0
    n = 0

    for i in truck:                                 # 각 트럭은 담을 수 있는 화물중 가장 큰 것을 담고 나감
        while True:
            if n >= N:
                break
            elif i >= con[n]:
                cnt += con[n]
                n += 1
                break
            else:
                n += 1

    print('#{} {}'.format(tc, cnt))
