# SWEA_5789. 현주의 상자 바꾸기
# 2022-08-19

# 정답코드
import sys
sys.stdin = open('sample_input.txt','r')

TC = int(input())

for tc in range(1, TC+1):
    N, Q = map(int, input().split())

    boxes = [0]*(N+1)                       # idx와 상자번호를 맞추기 위함. idx0은 무시
    change = [0]                            # 바뀔 번호를 idx로 갖게 하기 위해 idx0에 0을 넣어둠 
    for i in range(Q):                      # 바뀔 번호를 idx로 갖는 리스트에 바꿀 상자를 저장
        L, R = map(int, input().split())
        change.append([L, R])

    for i in range(1, Q+1):
        for j in range(change[i][0], change[i][1]+1):
            boxes[j] = i                    # 번호 변경

    print('#{} '.format(tc), end='')
    for i in range(1, N+1):
        print(boxes[i], end=' ')
    print()