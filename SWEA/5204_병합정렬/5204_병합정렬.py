# SWEA_5204. 병합정렬
# 220927

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')


def divide(arr, N):
    if len(arr) == 1:
        return arr
    arr1 = arr[0:N//2]
    arr2 = arr[N//2:N]

    arr1 = divide(arr1, len(arr1))
    arr2 = divide(arr2, len(arr2))

    return merge(arr1, arr2)


def merge(arr1, arr2):
    global cnt
    result = []
    if arr1[-1] > arr2[-1]:
        cnt += 1

    while len(arr1) > 0 or len(arr2) > 0:

        if len(arr1) > 0 and len(arr2) > 0:

            if arr1[-1] >= arr2[-1]:
                result.append(arr1.pop())

            else:
                result.append(arr2.pop())

        elif len(arr1) > 0:
            result = result + arr1[::-1]
            arr1 = []
        elif len(arr2) > 0:
            result = result + arr2[::-1]
            arr2 = []

    return result[::-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = divide(arr, N)


    print('#{} {} {}'.format(tc, ans[N//2], cnt))