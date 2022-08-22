# SWEA_1223. 계산기2
# 220822

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10+1):
    N = int(input())
    cal = input()

    stack = []
    op = ['+', '*']
    top = -1

    tmp = ''
    for i in cal:
        # i가 피연산자인 경우 그냥 추가
        if i not in op:
            tmp += i

        # i가 +인 경우 스택이 비어있지 않으면 pop, 비었으면 push
        elif i == '+':
            while True:
                if stack == []:
                    stack.append(i)
                    top += 1
                    break
                else:
                    tmp += stack.pop(-1)
                    top -= 1

        # i가 *인 경우 스택이 비어있거나 +로 끝나지 않으면 pop, 이외엔 push
        else:
            while True:
                if (stack == []) or (stack[top] == '+'):
                    stack.append(i)
                    top += 1
                    break
                else:
                    tmp += stack.pop(-1)
                    top -= 1
    for i in range(len(stack)):
        tmp += stack.pop(-1)

    # 후위 표기법의 수식을 스택을 이용해 계산 (스택은 현재 비어있다.)
    for i in tmp:
        if i not in op:
            stack.append(int(i))
            top += 1
        elif i == '+':
            new = stack.pop(-2) + stack.pop(-1)     # pop(-1)을 두번 해도 되지만, 이 경우 -, /에서 문제가 생긴다
            stack.append(new)
            top -= 1                                # 2번 빠지고 1개 들어가서 -1
        else:
            new = stack.pop(-2) * stack.pop(-1)
            stack.append(new)
            top -= 1

    print('#{} {}'.format(tc, stack[0]))
