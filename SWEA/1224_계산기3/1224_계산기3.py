# SWEA_1224. 계산기3
# 220823

# 정답 코드
import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 10+1):
    N = int(input())
    cal = input()

    # 우선순위를 idx로 갖고 있는 연산자들의 집합
    op = [['('], ['+', '-'], ['*', '/']]
    stack = []
    top = -1
    tmp = []

    for i in cal:
        if i in op[0]:  # i가 ( 인 경우
            stack.append(i)  # 그냥 push
            top += 1

        # i가 + or - 인 경우 스택이 비거나 ( 로끝날때까지 pop, 그게 아니면 push
        elif i in op[1]:
            while True:
                if (stack == []) or (stack[top] == '('):
                    stack.append(i)
                    top += 1
                    break
                else:
                    tmp.append(stack.pop(-1))
                    top -= 1

        # i가 * or / 인 경우 스택이 비거나 낮은 우선순위 기호로 끝날 때 까지 pop, 그게 아니면 push
        elif i in op[2]:
            while True:
                if (stack == []) or (stack[top] not in op[2]):
                    stack.append(i)
                    top += 1
                    break
                else:
                    tmp.append(stack.pop(-1))
                    top -= 1

        # i가 ) 인 경우 ( 가 나올때까지 pop, ( 가 나오면 폐기하고 종료
        elif i == ')':
            while True:
                if stack[top] == '(':
                    stack.pop(-1)
                    top -= 1
                    break
                else:
                    tmp.append(stack.pop(-1))
                    top -= 1

        # i가 피연산자인 경우 그냥 출력
        else:
            tmp.append(i)

    for i in range(len(stack)):
        tmp.append(stack.pop(-1))

    # 후위 표기법의 수식을 스택을 이용해 계산 (스택은 현재 비어있다.)
    for i in tmp:
        if i not in op[1] and i not in op[2]:
            stack.append(int(i))
            top += 1
        elif i == '+':
            new = stack.pop(-2) + stack.pop(-1)  # pop(-1)을 두번 해도 되지만, 이 경우 -, /에서 문제가 생긴다
            stack.append(new)
            top -= 1  # 2번 빠지고 1개 들어가서 -1
        else:
            new = stack.pop(-2) * stack.pop(-1)
            stack.append(new)
            top -= 1

    print('#{} {}'.format(tc, stack[0]))