# SWEA_1859. 백만장자프로젝트
# 220816
'''
뒤에서부터 센다
나보다 큰값이 나올때 까지
나와의 차를 profit에 저장
'''
# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

# len 함수
def llen(a) :
    x = 0
    for i in a :
        x += 1
    return x

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    N = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    big = prices[-1] # 마지막항을 최댓값이라고 일단 지정
    for i in range(llen(prices)-1, -1, -1) : # 뒤에서부터 순회
        if prices[i] <= big : # 현재 값이 최댓값보다 작으면 (같을때는 0을 누적하는거라 분리 안해도 상관없음)
            profit += big - prices[i] # 이익 누적
        elif prices[i] > big : # 현재 값이 최댓값보다 크면
            big = prices[i] # 최댓값을 갱신

    print('#{} {}'.format(tc, profit))

