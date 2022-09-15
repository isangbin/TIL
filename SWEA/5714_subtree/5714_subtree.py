# SWEA_5714. subtree
# 220915

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))

    ch1 = [0]*(E+2)                         # 노드는 E+1개 있고, 0번은 안쓸거니까 E+2개 생성
    ch2 = [0]*(E+2)
    for i in range(E):
        if ch1[tmp[2*i]] == 0:
            ch1[tmp[2*i]] = tmp[2*i+1]
        else:
            ch2[tmp[2*i]] = tmp[2*i+1]

    cnt = 0
    preorder(N)
    print('#{} {}'.format(tc, cnt))
