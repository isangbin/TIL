# SWEA_1225. 암호생성기
# 220824

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

def deQueue():
    return pw.pop(0)

def enQueue(item):
    pw.append(item)
    return

for tc in range(1, 10+1):
    TC = int(input())
    pw = list(map(int, input().split()))

    keepGoing = True
    while keepGoing:                # 조건 만족시까지 무한루프
        n = 1                       # 사이클 다돌면 n = 1 초기화
        while n <= 5:               # 한사이클
            if pw[0] - n <= 0:      # 작업시 0이하가 된다면
                deQueue()           # dequeue
                enQueue(0)          # enqueue
                keepGoing = False   # 조건 만족
                break               # 탈출
            else:                   # 작업시 0 이하가 되지 않으면
                tmp = deQueue()     # dequeue
                enQueue(tmp - n)    # enqueue
                n += 1              # n += 1

    print('#{} '.format(tc), end='')
    for i in pw:
        print(i, end=' ')
    print()