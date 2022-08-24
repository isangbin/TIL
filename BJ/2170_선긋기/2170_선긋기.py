# BJ_2170. 선긋기
# 220824

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
lines = []
for i in range(N):
    a, b = map(int, input().split())
    lines.append([a, b])                # 줄의 정보 저장
lines.sort()
cnt = 0                                 # 선의 길이
tmp = []                                # 줄들을 누적할 공간

for i in lines:
    for j in range(i[0], i[1]):
        if j not in tmp:
            tmp.append(j)
            cnt += 1


sys.stdout.write(str(cnt))