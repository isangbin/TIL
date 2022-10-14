# SWEA_1952. 수영장 (dp)
# 220923

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    day1, mon1, mon3, year1 = map(int, input().split())
    plan = list(map(int, input().split()))

    prices = [0]*12
    # 우선 월별 최저가를 저장한다.
    for i in range(12):
        if plan[i]*day1 <= mon1:
            prices[i] = plan[i]*day1
        else:                       # i*day > mon1:
            prices[i] = mon1
    
    dp = [0]*12
    dp[0] = prices[0]
    dp[1] = dp[0] + prices[1]
    dp[2] = min(dp[1] + prices[2], mon3)
    for i in range(9):
        dp[3+i] = min(dp[2+i]+prices[3+i], dp[i]+mon3)
    
    ans = 0
    if dp[11] <= year1:
        ans = dp[11]
    else:
        ans = year1
    
    print('#{} {}'.format(tc, ans))