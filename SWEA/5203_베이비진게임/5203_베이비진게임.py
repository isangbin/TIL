# SWEA_5203. 베이비진 게임
# 220922

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def babygin(p):
    if len(p) < 3:                                                          # 3개도 안모였으면 컷
        return 0
    else:
        for k in range(10):
            if p[k] >= 3:                                                   # 같은 수 3개이상이면 승리
                return 1
            elif k <= 7 and p[k] >= 1 and p[k+1] >= 1 and p[k+2] >= 1:      # 연속된 3개의 수 모였으면 승리
                return 1
        return 0                                                            # 아무것도 아니면 컷


T = int(input())
for tc in range(1, T+1):
    turn = list(map(int, input().split()))

    p1 = [0]*10
    p2 = [0]*10
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            p1[turn[i]] += 1                # 1번한테 카드주고
            if babygin(p1) == 1:            # babygin 완성했으면
                winner = 1                  # 승리
                break
        else:
            p2[turn[i]] += 1                # 2번한테 카드주고
            if babygin(p2) == 1:            # babygin 완성했으면
                winner = 2                  # 승리
                break

    print('#{} {}'.format(tc, winner))