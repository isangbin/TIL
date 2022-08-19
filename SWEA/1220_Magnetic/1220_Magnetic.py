# SWEA_1220. Magnetic
# 2022-08-19

# 정답코드
import sys
sys.stdin = open('input.txt','r')

# push
def push(item):
    stack.append(item)
# pop
def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop(-1)
# len
def llen(a):
    llen = 0
    for i in a:
        llen += 1
    return llen

for tc in range(1, 10+1):
    edge = int(input())
    mags = [list(map(int, input().split())) for _ in range(edge)]
    stack = []
    cnt = 0 # 교착상태의 개수

    for j in range(100):
        for i in range(100):            # 위에서 아래로 순회
            if mags[i][j] == 1:         # N자성체인 경우
                if llen(stack) == 0:    # stack이 비어있으면 (이미 있을경우 어차피 하나의 교착만 발생할 거라서 더하면안됨)
                    push(mags[i][j])    # push

            elif mags[i][j] == 2:       # S자성체인 경우
                if llen(stack) == 0:    # stack이 비어있으면
                    continue            # 떨어지거나 다른 교착점에 붙게되므로 no count
                else:                   # 마주보고 있는 N자성체가 존재하면
                    pop()               # N자성체를 pop
                    cnt += 1            # 교착1개 발생

        stack = []                      # 한 column 조사가 끝나면 stack을 비워줘야함
                                        # 남아있는 것은 떨어지거나 다른 교착점에 붙은 N자성체임
    print('#{} {}'.format(tc, cnt))
