# SWEA_1234. 비밀번호
# 2022-08-18

# 정답코드
import sys
sys.stdin = open('input.txt','r')

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop(-1)

for tc in range(1, 10+1):
    N, pw = map(str, input().split())               # int로 받으면 맨앞 0이 사라지므로 str로 받기
    pw = list(pw)                                   # 인덱스접근 위해 리스트화
    stack = []

    for i in range(int(N)):
        if len(stack) != 0 and pw[i] == stack[-1]:  # 스택이 비어있지않고 현재 숫자와 스택의 마지막숫자가 같으면
            pop()                                   # pop
        else:                                       # 그 외엔
            push(pw[i])                             # push

    ans = ''                                        # 언패킹
    for i in stack :
        ans += i

    print('#{} {}'.format(tc, ans))