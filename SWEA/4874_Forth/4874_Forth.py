# SWEA_4874. Forth
# 220823

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    cal = list(map(str, input().split()))
    stack = []
    top = -1
    op = ['+', '-', '*', '/']
    ans = 0
    for i in cal:
        # i가 .이면 에러 검사
        if i == '.':
            if top != 0:        # 연산이 끝났을 때 stack에는 계산 결과만 있어야함
                ans = 'error'
            else:
                ans = stack[0]

        # 피연산자는 정수화 하여 stack에 추가
        elif i not in op:
            stack.append(int(i))
            top += 1
        # 덧셈
        elif i == '+':
            if top < 1:      # 계산불가능
                ans = 'error'
                break
            else:
                new = stack.pop(-2) + stack.pop(-1)
                stack.append(new)
                top -= 1
        # 뺄셈        
        elif i == '-':
            if top < 1:      # 계산불가능
                ans = 'error'
                break
            else:
                new = stack.pop(-2) - stack.pop(-1)
                stack.append(new)
                top -= 1
        # 곱셈        
        elif i == '*':
            if top < 1:      # 계산불가능
                ans = 'error'
                break
            else:
                new = stack.pop(-2) * stack.pop(-1)
                stack.append(new)
                top -= 1
        # 나눗셈
        elif i == '/':
            if top < 1:      # 계산불가능
                ans = 'error'
                break
            else:
                new = stack.pop(-2) // stack.pop(-1)    # 몫으로 처리해야 float이 되지 않음
                stack.append(new)
                top -= 1

    print('#{} {}'.format(tc, ans))