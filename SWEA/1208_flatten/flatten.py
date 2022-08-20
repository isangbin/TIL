# SWEA 1208. flatten
# 220809

'''
idx중 최고값을 1 빼고 최저값을 1 더한다
최저값이 중복일 땐 오른쪽부터 채운다

'''

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

def height(box) : # 현 상태에서 요소중 최댓값과 최솟값을 얻는 함수
    high = 0
    high_idx = 0
    low = box[0]
    low_idx = 0
    for i in range(0, 100) :
        if high <= box[i] :
            high = box[i]
            high_idx = i
        if low >= box[i] :
            low = box[i]
            low_idx = i
    
    return [high_idx, low_idx]


for tc in range(1, 10+1) :

    dump = int(input())
    box = list(map(int, input().split()))

    cnt = 1
    while cnt <= dump : # 최대 dump회 까지만 진행한다.
        if box[height(box)[0]] - box[height(box)[1]] > 1 : # 최댓값과 최솟값의 차가 1보다 크면
            box[height(box)[0]] -= 1 # 최댓값을 최솟값으로 1개 이동한다.
            box[height(box)[1]] += 1
            cnt += 1 # 횟수 증가
        else : # 최댓값과 최솟값의 차가 1 이하이면 그만둔다.
            break
    
    print('#{} {}'.format(tc, box[height(box)[0]] - box[height(box)[1]]))