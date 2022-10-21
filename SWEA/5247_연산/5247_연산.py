import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')


def dfs(N):
    q = deque()
    q.append((N, 0))                                        # (현재 숫자, 여기까지 오기위해 연산한 횟수)
    visited = [0]*1000001
    while q:
        i, level = q.popleft()
        if 0 < i+1 <= 1000000 and visited[i+1] == 0:        # 연산결과가 범위안에 있고 다룬적 없을 경우
            if i+1 == M:                                    # 그런데 그게 원하는 답이면
                return level + 1                            # level은 지금까지 연산횟수이고, 여기서 한번 더해서 M이 나오는거니까 level+1 리턴
            q.append((i+1, level+1))                        # M이 아니면 큐에 추가하고
            visited[i+1] = 1                                # 방문 표시
        if 0 < i-1 <= 1000000 and visited[i-1] == 0:        # 이하 동문
            if i-1 == M:
                return level + 1
            q.append((i-1, level+1))
            visited[i-1] = 1
        if 0 < i*2 <= 1000000 and visited[i*2] == 0:
            if i*2 == M:
                return level + 1
            q.append((i*2, level+1))
            visited[i*2] = 1
        if 0 < i-10 < 1000000 and visited[i-10] == 0:
            if i-10 == M:
                return level + 1
            q.append((i-10, level+1))
            visited[i-10] = 1
            

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    ans = dfs(N)
    print('#{} {}'.format(tc, ans))
