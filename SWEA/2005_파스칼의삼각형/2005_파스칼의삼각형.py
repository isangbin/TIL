# swea_2005 파스칼의 삼각형
# 2022-08-17
import sys
sys.stdin = open('input.txt','r')
T = int(input())


for t in range(T):
    N = int(input())
    # 전단계
    pre = [1]
    # 첫 단계 프린트
    print('#{}'.format(t+1))
    print('1')

    # 첫 단계는 이미 프린트 했으니 N-1
    for i in range(N-1):
        
        # 이번 단계 공간
        new = [1]

        # 전단계의 토대로 이번단계에 숫자 추가하기
        for j in range(i):
            new.append(pre[j] + pre[j+1])
        
        # 마지막으로 1 추가
        new.append(1)

        # 현 단계를 전단계로
        pre = new
        
        # 반환
        print(*new)
