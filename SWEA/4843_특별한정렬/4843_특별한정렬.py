# SWEA 4843 . 특별한 정렬
# 220811
'''
일단 정렬 후
인덱스가 짝수면 큰거부터
홀수면 작은거부터 가져오기
'''
# 정답코드
import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())  # tc 수

def bubble(arr, N) : # 버블정렬
    for i in range(N-1, 0, -1) :
        for j in range(0, i) :
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for tc in range(1, TC + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    arr = bubble(arr, N) # arr 버블정렬하기 (내림차순)
    ans = []
    for i in range(10) : # 10개까지만 표시
        if i % 2 == 0 : # idx가 짝수면
            ans.append(arr[int(i/2)]) # 앞에서 채우기
        else : # idx가 홀수면
            ans.append(arr[N-int((i+1)/2)]) # 뒤에서 채우기 (1은 arr[N - (1+1)/2] 에 위치함)

    print('#{}'.format(tc), end=' ')
    for i in ans :
        print(i, end=' ')
    print()