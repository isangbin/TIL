# 4835. 전기버스
# 220809

'''
K칸만큼 전진한 뒤 충전소가 있는지 확인한다
있으면 K만큼 전진
없으면 1만큼 후진
충전소가 있는지 확인한다
있으면 K만큼 전진
없으면 1만큼 후진
K-1번 반복 후 충전소가 없으면 결과는 0
있으면 다음 idx에서 다시 처음부터 진행
현 위치가 N보다 크면 충전소 횟수 출력
'''

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

times = int(input()) # tc 수

for tc in range(1, times+1) :

    K, N, M= map(int, input().split())# 숫자의 자릿수 # 숫자
    charge = list(map(int, input().split()))
    busstop = [0]*(N+1)
    for i in charge :
        busstop[i] = 1
    
    idx = 0 # 현위치
    cnt = 0 # 충전 횟수
    stack = 0 # 뒷걸음 횟수
    answer = ''
    while True :
        if idx+K < N :
            if busstop[idx+K] == 1 : # K만큼 전진했을때 충전소 있으면 그곳을 현위치로 수정
                idx = idx+K
                cnt += 1
                stack = 0
            else : # 충전소가 없으면 뒤로 한걸음
                idx -= 1
                stack += 1 # 뒷걸음 수 측정 (뒷걸음질을 K번 이상 하게되면 목적지 도달이 불가능)
                if stack >= K : # 목적지 도달이 불가능할 경우 0 출력
                    answer = 'A'
                    break
        else :
            break

    if answer == 'A' :
        print('#{} 0'.format(tc))
    else :
        print('#{} {}'.format(tc, cnt))