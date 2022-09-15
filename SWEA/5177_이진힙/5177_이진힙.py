# SWEA_5177. 이진 힙
# 220915

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

def enq(n):                                     # 최소힙 구현
    global last
    last += 1                                   # 현재 노드위치를 1 올림
    heap[last] = n                              # last번 노드에 n을 추가

    c = last                                    # c = 마지막 노드 번호
    p = c // 2                                  # p = c의 부모 노드 번호
    while heap[p] > heap[c]:                    # 방금 추가된 c의 내용물이 부모노드의 내용물보다 클때 까지
        heap[p], heap[c] = heap[c], heap[p]     # 부모와 마지막 노드의 내용물을 교환
        c = p                                   # 방금 값을 교환한 부모자리가 자식이 됨
        p = c // 2                              # 방금 값을 교환한 부모의 부모가 부모가됨 (?)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N+1)                          # 0번을 제외하고 1~N이 들어갈 수 있는 heap공간 마련
    last = 0                                    # 현재 노드 위치는 0

    for i in nums:                              # 모든 숫자를 순서대로
        enq(i)                                  # 추가

    ans = 0
    while last != 0:                            # 루트노드에 도달할 때 까지
        ans += heap[last//2]                    # ans에 부모의 내용물을 더함
        last = last // 2                        # 현 위치를 부모의 위치로 변경

    print('#{} {}'.format(tc, ans))