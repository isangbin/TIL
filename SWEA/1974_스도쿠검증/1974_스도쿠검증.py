# SWEA_1974. 스도쿠 검증
# 2022-08-19

# 정답코드
import sys
sys.stdin = open('input.txt','r')

TC = int(input())

for tc in range(1, TC+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    nums = [0]*10
    ans = 1

    # 가로선 조사
    for i in range(9):
        for j in range(9):
            if nums[sdoku[i][j]] == 0:
                nums[sdoku[i][j]] += 1

        for n in range(1, 10):
            if nums[n] != 1:
                ans = 0
                break
        nums = [0]*10

    # 세로선 조사
    for i in range(9):
        for j in range(9):
            if nums[sdoku[j][i]] == 0:
                nums[sdoku[j][i]] += 1

        for n in range(1, 10):
            if nums[n] != 1:
                ans = 0
                break
        nums = [0]*10

    # 사각형 조사
    for i in range(3):
        for j in range(3):
            for a in range(3):
                for b in range(3):
                    if nums[sdoku[i*3+a][j*3+b]] == 0:
                        nums[sdoku[i*3+a][j*3+b]] += 1
            for n in range(1, 10):
                if nums[n] != 1:
                    ans = 0
                    break
            nums = [0]*10

    print('#{} {}'.format(tc, ans))

    '''
    9개 공간에 대하여
     0 0 -> 012 012 -> a*3 
     0 1 -> 012 345
     1 0 -> 345 012
    '''
