# SWEA_1211 . Ladder2
# 220810

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10+1):
    TC = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [1, 0, 0]      # 하, 좌, 우
    dj = [0, -1, 1]

    small = 10000       # 최솟값의 초기값
    cnt_list = []
    for x in range(100):        # 첫줄에서
        if ladder[0][x] == 1:      # 값이 1이면(출발점)
            # 아래로 한칸 전진 (출발)
            i = 1
            j = x
            cnt = 1

            while j < 99:       # 마지막줄에 도달할 때 까지
                #왼쪽에 길이 있다
                if j-1 >= 0 and ladder[i][j-1] == 1:
                    while j != 0 and ladder[i][j] != 0:
                        i = i+di[1]
                        j = j+dj[1]
                        cnt += 1
                    i = i+di[0]
                    j = j+dj[0]
                    cnt += 1
                #오른쪽에 길이 있다
                elif j+1 <= 99 and ladder[i][j+1] == 1:
                    while j != 99 and ladder[i][j] != 0:
                        i = i+di[2]
                        j = j+dj[2]
                        cnt += 1
                    i = i+di[0]
                    j = j+dj[0]
                    cnt += 1
                #양쪽에 길이 없다
                else:
                    i = i+di[0]
                    j = j+dj[0]
                    cnt += 1
            cnt_list.append(cnt)
            print(cnt)
    print(cnt_list)
    for i in cnt_list:
        if small >= i:
            small = i

    print('#{} {}'.format(tc, small))