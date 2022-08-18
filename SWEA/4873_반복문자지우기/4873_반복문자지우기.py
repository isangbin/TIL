# SWEA_4873. 반복문자 지우기
# 2022-08-18

# 정답코드
import sys
sys.stdin = open('sample_input.txt','r')

TC = int(input())

# push
def push(item) :
    stack.append(item)
# pop
def pop() :
    if len(stack) == 0 :
        return
    else :
        return stack.pop(-1)


for tc in range(1, TC+1):
    str1 = list(input())

    stack = []

    for i in range(len(str1)) :                         # 문자열의 각 항목에 대해
        if len(stack) != 0 and str1[i] == stack[-1] :   # stack에 뭔가 있고, 그중 마지막 것과 같으면 pop
            pop()
        else :                                          # 그 외엔 push
            push(str1[i])

    print('#{} {}'.format(tc, len(stack)))