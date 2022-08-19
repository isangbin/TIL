# SWEA_1209 . sum
# 220810

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10+1) :

    TC = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    sum_i, sum_j, sum_x1, sum_x2 = 0, 0, 0, 0
    sums = []
    for i in range(100) :
        for j in range(100) :
            sum_i += arr[i][j]   # 행의 합들
            sum_j += arr[j][i]   # 열의 합들
        sums.append(sum_i)
        sums.append(sum_j)
        sum_i, sum_j = 0, 0

    for i in range(100) : # 대각선 합들
        sum_x1 += arr[i][i]
        sum_x2 += arr[i][99-i]
    sums.append(sum_x1)
    sums.append(sum_x2)
    sum_x1, sum_x2 = 0, 0

    max_sum = 0
    for i in sums : # 합들 중 최댓값
        if i >= max_sum :
            max_sum = i
    
    print('#{} {}'.format(TC, max_sum))