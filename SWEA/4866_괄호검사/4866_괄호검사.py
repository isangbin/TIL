# SWEA_4866. 괄호검사
# 2022-08-17

# 정답코드
import sys
sys.stdin = open('sample_input.txt','r')

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop(-1)

TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    stack = []
    bracket1 = ['(', '[', '{']
    bracket2 = [')', ']', '}']
    ans = 1

    for i in range(len(str1)):
        # 괄호가 아니면 무시
        if str1[i] not in bracket1 and str1[i] not in bracket2:
            continue
        # 닫는괄호면
        elif str1[i] in bracket2:
            # stack의 마지막항과 짝이 맞으면 pop
            if len(stack) != 0 and stack[-1] == bracket1[(bracket2.index(str1[i]))]:
                pop()
            # 짝이 안맞으면 오류이므로 탈출, ans = 0
            else:
                ans = 0
                break
        # 여는괄호면 push
        else:
            push(str1[i])

    # for문이 끝났는데 stack에 남은게 있으면 오류이므로 ans = 0
    if len(stack) != 0:
        ans = 0
    print('#{} {}'.format(tc, ans))