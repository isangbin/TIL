# SWEA_1952. 수영장
# 220923

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def M3(i):
    if i >= 12:
        return 0
    
    elif prices[i] + prices[i-1] + prices[i-2] <= mon3:
        return 0
            
    else:
        return 1


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
    print(1, prices)
    # 3개월 이용권이 이득인지 아닌지 알아본다.
    print(f'day1:{day1}, mon1:{mon1}, mon3:{mon3}, year1:{year1}')
    mon3_list = [0]*12
    i = 2
    while i < 12:
        if M3(i) == 0:
            i += 1
            
        else:
            # print(2, i)
            if M3(i+3) == 1 or (M3(i+3) == 0 and (i == 11 or (prices[i-2] >= prices[i+1] and prices[i-1] >= prices[i+2]))):
                prices[i-2] = mon3
                prices[i-1] = 0
                prices[i] = 0
                # print(2, prices)
                if i == 11:
                    break
            
                if i <= 8:
                    i += 3
                else:
                    i = 11

            elif prices[i+1] + prices[i+2] > prices[i-1] + prices[i-2]:
                prices[i] = mon3
                prices[i+1] = 0
                prices[i+2] = 0
                if i == 11:
                    break
                if i <= 6:
                    i += 5
                else:
                    i = 11

            else:
                prices[i-1] = mon3
                prices[i] = 0
                if i+1 < 12:
                    prices[i+1] = 0
                    # print(3, prices)
                if i == 11:
                    break
                if i <= 7:
                    i += 4
                else:
                    i = 11


    
    # 1년 이용권이 이득인지 아닌지 알아본다.
    ans = 0
    if sum(prices) >= year1:
        ans = year1
    else:
        ans = sum(prices)

    print('#{} {}'.format(tc, ans))