# SWEA_1231. 중위순회
# 220913

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

def inorder(n):                                 # 중위 순회
    if n:
        inorder(ch1[n])
        print(words[n], end='')
        inorder(ch2[n])

for tc in range(1, 10+1):
    N = int(input())

    words = ['']*(N+1)                          # 노드별로 글자를 저장할 공간
    ch1 = [0]*(N+1)                             # 왼쪽 자식 리스트
    ch2 = [0]*(N+1)                             # 오른쪽 자식 리스트
    for i in range(1, N+1):
        tmp = list(map(str, input().split()))   # parent, word, kid1, kid2
        words[int(tmp[0])] = tmp[1]
        if len(tmp) == 3:                       # 자식이 1명이면
            ch1[int(tmp[0])] = int(tmp[2])
        if len(tmp) == 4:                       # 자식이 2명이면
            ch1[int(tmp[0])] = int(tmp[2])
            ch2[int(tmp[0])] = int(tmp[3])

    print('#{} '.format(tc), end='')
    inorder(1)
    print()