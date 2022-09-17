# SWEA_1238. contact
# 220915

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

def calling(n):

    for i in nodes[n]:                                      # 전화를 건다
        if called[i] == 0 or called[i] > called[n]+1:       # 전화받은적 없거나 이전 재귀에서 전화받은 것보다 더 빨리 받을 수 있는 경우
            called[i] = called[n]+1                         # 현재 순번으로 저장
            calling(i)                                      # 전화 받은사람이 다시 전화돌리기 시작
    return

for tc in range(1, 10+1):
    N, root = map(int, input().split())
    nums = list(map(int, input().split()))

    nodes = [[] for _ in range(101)]
    for i in range(0, N, 2):
        nodes[nums[i]].append(nums[i+1])

    called = [0]*101                                        # 전화를 몇번째로 받았는지 저장할 장소
    called[root] = 1                                        # root가 첫번째로 전화를 받았다고 하고
    calling(root)                                           # 전화돌리기 시작

    ans = 0
    max_num = 0
    for i in range(101):                                    # 각 인원의 전화받은 순서 리스트 에서
        if max_num <= called[i]:                            # 전화받은 순서의 최대치를 찾고
            max_num = called[i]
            ans = i                                         # 그 때의 인덱스(가장 늦게 전화받은 사람)를 ans에 저장

    print('#{} {}'.format(tc, ans))