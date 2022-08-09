# 4834. 숫자카드
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

    Len = int(input()) # 숫자의 자릿수
    num = int(input()) # 숫자
    
    arr = [0]*Len
    for i in range(0, Len) : # 숫자의 자릿수를 각각 쪼개어 저장
        arr[i] = num % 10
        num = num // 10

    cnt = [0]*10
    for i in arr :  # 0~9가 몇개씩 있는지 저장 (idx가 숫자, 값이 갯수가 된다)
        cnt[i] += 1

    max_cnt = 0
    max_idx = 0
    for i in range(0, 10) : # 갯수가 가장 높은 항목에 대한 조사
        if cnt[i] >= max_cnt : # 갯수가 같아도 갱신하므로 최댓값이 복수일땐 가장 높은 idx가 차출됨
            max_cnt = cnt[i]
            max_idx = i
        
    print('#{} {} {}'.format(tc, max_idx, max_cnt))

