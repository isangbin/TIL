# SWEA_5202. 화물도크
# 220922

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def S(request):
    global cnt
    tmp1 = request.pop(0)           # 가장 종료시간이 빠른 것을 뽑기
    cnt += 1                        # 뽑을때마다 카운트
    tmp2 = []
    for k in request:               # 그것보다 일찍 시작해야 하는 것들 제외하고 다시 리스트 생성
        if k[1] >= tmp1[0]:
            tmp2.append(k)

    if len(tmp2) == 0:              # 더이상 진행 가능한 경우가 없으면 끝
        return
    else:                           # 새 리스트에 대해 같은 작업 반복
        S(tmp2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    request = []
    for i in range(N):
        s, e = map(int, input().split())
        request.append([e, s])
    request.sort()

    cnt = 0
    S(request)

    print('#{} {}'.format(tc, cnt))



