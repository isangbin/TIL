# SWEA 4839 . 이진탐색
# 220811

# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

for tc in range(1, TC + 1):

    P, A, B = map(int, input().split())

    obj = [A, B] # 오브젝트
    cnt = [0, 0] # 각 오브젝트의 검색 시행 횟수
    for i in range(2):
        l = 1 # 왼쪽끝
        r = P # 오른쪽끝

        while True: # break될때까지 무한 반복
            if (l+r)//2 < obj[i]: # 중간값보다 목표값이 더 크면
                l = (l+r)//2 # 중간값 아래를 버림
                cnt[i] += 1 # 검색횟수 +1
            elif (l+r)//2 > obj[i]: # 중간값보다 목표값이 더 작으면
                r = (l+r)//2 # 중간값 위를 버림
                cnt[i] += 1 # 검색횟수 +1
            else: # 둘다 아닌경우 = 중간값이 목표값일 경우
                break # 반복문을 종료
    winner = ''
    if cnt[0] < cnt[1]: # 승자가 누구인지
        winner = 'A'
    elif cnt[0] > cnt[1]:
        winner = 'B'
    else :
        winner = 0
    print('#{} {}'.format(tc, winner))

