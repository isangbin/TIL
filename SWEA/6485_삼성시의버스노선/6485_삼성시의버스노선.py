# SWEA_6485. 삼성시의 버스 노선
# 2022-08-19

# 정답코드
import sys
sys.stdin = open('s_input.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    buses = []
    for i in range(N):
        a, b = map(int, input().split())
        buses.append([a, b])

    stops = [0]*5001                        # stops[0]은 무시

    want = []                               # 조사할 정류장 번호
    P = int(input())
    for i in range(P):
        want.append(int(input()))

    for i in buses:                         # 각 버스가 지나간 자리 기록
        for j in range(i[0], i[1]+1):
            stops[j] += 1

    ans = []
    for i in want:                          # 조사할 정류장에 버스가 몇번 지나갔는지 확인
        ans.append(stops[i])

    print('#{}'.format(tc), end=' ')
    print(*ans)