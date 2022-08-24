# BJ_1946. 신입사원
# 220824

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort()                           # 서류심사 등수순으로 정렬하면 첫항부터 순회하면서
                                            # 면접 등수만을 고려하면 된다.

    second = [0]*N                          # 각 인원의 면접 등수의 집합
    second[0] = scores[0][1]                # 첫항 먼저 넣어놓기
    total = N                               # 모두 합격으로 가정, 탈락자 발생시마다 1씩 감소시킬 예정

    for i in range(1, N):                   # 각 인원의 면접심사 등수에 대하여
        for j in range(i):                  # 이전 사람들의 면접 등수보다
            if second[j] < scores[i][1]:    # 못본게 한번이라도 적발되면
                total -= 1                  # 합격자수 한명 제거 (탈락 1명 증가)
                break                       # 이사람은 더 볼것도 없으니 가지치기
        second[i] = scores[i][1]            # 면접 등수를 리스트 추가

    print(total)