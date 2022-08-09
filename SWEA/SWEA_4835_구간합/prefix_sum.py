# 4835. 구간합
# 220809

'''
숫자를 쪼개어 각각을 요소로 하는 리스트 arr생성
arr 안에 0~9가 몇 개 씩 있는지 저장한 cnt 리스트 생성
cnt를 0부터 9까지 순회하며 갯수가 가장 큰 항목에 대해 무엇이 몇 개 인지 출력
(0부터 9까지 순회하고 idx가 같을때도 갱신하므로 갯수가 같을땐 자동으로 높은 숫자가 max_idx에 저장된다) 
'''

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # tc 수

for tc in range(1, N+1) :

    N, M= map(int, input().split()) # 숫자의 자릿수
    nums = list(map(int, input().split()))
    
    mini = 0
    for i in nums :
        mini += i

    minimum = mini # 초기치를 리스트 전체의 합으로 지정 (너무 작은 값은 오류 발생 위험)
    maximum = 0
    tmp = 0

    for i in range(0, N-M+1) : # idx 0부터 N-M까지에 대하여 (indexerror 방지)
        for j in range(0, M) : # idx i부터 M개의 연속된 값을
            tmp += nums[i+j] # tmp에 합으로 저장
            
            
        if tmp <= minimum : # 가장 작은 값을 도출
            minimum = tmp
        if tmp >= maximum : # 가장 큰 값을 도출
            maximum = tmp
        
        
        tmp = 0
    
    print('#{} {}'.format(tc, maximum-minimum))