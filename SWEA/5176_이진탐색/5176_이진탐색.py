# SWEA_5176. 이진탐색
# 220915

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def inorder(n):                     # 중위순회
    global cnt
    if n:
        inorder(ch1[n])
        cnt += 1
        nodes[n] = cnt
        inorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    nodes = [0]*(N+1)               # 노드별 숫자를 저장할 공간
    ch1 = [0]*(N+1)                 # 왼쪽 자식
    ch2 = [0]*(N+1)                 # 오른쪽 자식

    for i in range(1, N+1):
        if i == 1:                  # 1번노드는 루트노드이므로 부모를 갖지 않음
            pass
        elif i % 2 == 0:            # 짝수번 노드의 부모는 2로 나눈 값을 번호로 갖는 노드
            ch1[i//2] = i
        else:                       # 홀수번 노드의 부모는 2로 나눈 값에 1을 더한 값을 번호로 갖는 노드
            ch2[i//2] = i

    cnt = 0
    inorder(1)
    print('#{} {} {}'.format(tc, nodes[1], nodes[N//2]))