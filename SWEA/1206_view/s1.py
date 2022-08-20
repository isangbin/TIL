# 1206_view
# 220808

'''
한 idx당 좌우 2개씩 4개의 인접 idx중 최댓값과 비교
현재 idx가 인접 idx의 최댓값보다 클 경우
idx - maximum이 조망권이 확보된 가구의 수
전체 idx에대해 수행한 후 합을 구하면 될 것
'''

# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

def idxmax(idx) : # 인접 idx중 최댓값을 찾는 함수
    idxmax = 0
    tmp = [bdg[idx-2], bdg[idx-1], bdg[idx+1], bdg[idx+2]]
    for i in tmp :
        if idxmax <= i :
            idxmax = i

    return idxmax

for tc in range(1, 10+1):
    Len = int(input()) # textcase 번호
    bdg = list(map(int, input().split())) # data
    accept = 0
    
    for idx in range(2, Len-2) :
        if bdg[idx] > idxmax(idx) : # 현재 idx값과 인접최댓값 비교
            accept += bdg[idx]-idxmax(idx) # 조망권 확보된 가구 수에 추가

    print(f'#{tc} {accept}')