# BJ_2075. N번째 큰 수
# 22.08.20

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

# len함수
def llen(a):
    llen = 0
    for i in a:
        llen += 1
    return llen

# max함수
def mmax(a):
    mmax = 0
    for i in a:
        if mmax <= i:
            mmax = i
    return mmax

N = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
big_nums = []

# input을 세로순서로 다시 저장
new_nums = []
for j in range(N):
    col = []
    for i in range(N):
        col.append(nums[i].pop(0))          # 뽑아서 새 리스트에 저장 후 제거 (메모리초과때문..)
    new_nums.append(col)

# big_nums에 N번째 큰 수가 저장되면 종료
while llen(big_nums) < N:
    tmp = []                                # 각 줄의 최댓값이 저장될 곳
    for a in new_nums:
        tmp.append(a[-1])
    
    big_nums.append(mmax(tmp))              # 그 중에서 가장 큰 값을 big_nums에 저장
    new_nums[tmp.index(mmax(tmp))].pop(-1)  # 최댓값으로 뽑힌 줄의 마지막값을 제거

sys.stdout.write(str(big_nums[-1]))         # N번째로 저장된 값을 출력
    