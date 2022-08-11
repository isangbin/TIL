# SWEA 1210. ladder1
# 220811
'''
1. fail
값이 2인 곳에서 역으로 출발
default : 올라간다
if 좌or우에 1이 있으면 방향을 튼다
i=0에 도착하면 그 때의 j값이 도착점 idx가 될 것이다?
XXXX 가로선에 들어가는 순간 왼쪽 오른쪽에 둘다 1이 있어서 못빠져나옴

2.
값이 2인곳에서 역으로 출발
올라가다가 좌우 1 만나면 꺾어 앞에 0나오면 반대로 꺾어
올라가다가  '' 그대로
위작업을 반복

'''
# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 10+1):

    TC = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]

    di = [-1, 0, 0] # 위, 좌, 우
    dj = [0, -1, 1]

    loc = [0, 0]
    for i in range(100): # 출발점 찾기
        for j in range(100):
            if ladders[i][j] == 2:
                loc[0], loc[1] = i, j

    while loc[0] != 0: # 맨 윗줄에 도착할 때 까지 진행

        if loc[1] != 0 and ladders[loc[0]+di[1]][loc[1]+dj[1]] == 1: # 왼쪽길이 있을 경우
            while ladders[loc[0]+di[1]][loc[1]+dj[1]] == 1: # 왼쪽길이 막다를때 까지
                loc[0] += di[1] # 왼쪽으로 감
                loc[1] += dj[1]
                if loc[1] == 0:
                    break

            loc[0] += di[0]  # 가만있으면 다시 돌아가므로 위로 한칸 감
            loc[1] += dj[0]

        elif loc[1] != 99 and ladders[loc[0]+di[2]][loc[1]+dj[2]] == 1: # 오른쪽길이 있을 경우
            while ladders[loc[0]+di[2]][loc[1]+dj[2]] == 1: # 오른쪽길이 막다를때 까지
                loc[0] += di[2] # 오른쪽으로 감
                loc[1] += dj[2]
                if loc[1] == 99:
                    break

            loc[0] += di[0]  # 가만있으면 다시 돌아가므로 위로 한칸 감
            loc[1] += dj[0]

        else : # 왼, 오른쪽에 길이 없을경우
            loc[0] += di[0] # 위로 감
            loc[1] += dj[0]

    print('#{} {}'.format(tc, loc[1]))