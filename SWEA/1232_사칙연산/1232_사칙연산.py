# SWEA_1232. 사칙연산
# 220915

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

def cal(a, b, c):                               # 계산 편하게 하기 위한 함수
    if a == '+':
        return int(b)+int(c)
    elif a == '-':
        return int(b)-int(c)
    elif a == '*':
        return int(b)*int(c)
    elif a == '/':
        return int(b)/int(c)

def postorder(n):                               # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        if words[n] in ['+', '-', '*', '/']:    # 노드에 써진게 연산기호라면
            a = stack.pop(-2)                   # 스택의 뒷 두개를 빼서
            b = stack.pop(-1)
            stack.append(cal(words[n], a, b))   # 계산한 결과를 스택에 추가

        else:
            stack.append(words[n])              # 노드에 써진게 숫자면 그냥 스택에 추가


for tc in range(1, 10+1):
    N = int(input())

    stack = []                                  # 후위계산을 위한 스택
    words = [0]*(N+1)                           # 노드에 들어가는 숫자or기호
    ch1 = [0]*(N+1)                             # 왼쪽 자식
    ch2 = [0]*(N+1)                             # 오른쪽 자식

    for i in range(N):
        tmp = input().split()
        words[int(tmp[0])] = tmp[1]             # 노드에 뭐써있는지 기록

        if len(tmp) == 4:                       # 자식이 있는 경우 ch1, ch2에 추가
            ch1[int(tmp[0])] = int(tmp[2])
            ch2[int(tmp[0])] = int(tmp[3])

    postorder(1)

    print('#{} {}'.format(tc, int(stack[0])))