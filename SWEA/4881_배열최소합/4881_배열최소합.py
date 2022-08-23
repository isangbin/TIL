# SWEA_4881. 배열 최소합
# 220823

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input())

# 순열을 통해 각 줄의 몇번째 요소를 pick할건지 결정
def f(i, N):
    if i == N:                              # 순열 1개 완성할때마다
        my_sum = 0
        for k in range(N):                  # k번째 줄의 pick[k]번째 항을
            my_sum += arr[k][pick[k]]       # my_sum에 누적
            if len(sum_list) != 0 and my_sum > sum_list[-1]:
                break                       # 누적하다가 최솟값보다 커지면 관둠
        else:
            sum_list.append(my_sum)         # 관둬지지 않았으면 합리스트에 추가


    else:
        my_sum = 0
        for k in range(i):                  # 위와 같은 구조지만 N까지가 아니라 i까지(현재까지)의 합을
            my_sum += arr[k][pick[k]]       # my_sum에 누적
            if len(sum_list) != 0 and my_sum > sum_list[-1]:
                break                       # 누적하다가 최솟값보다 커지면 관둠 (가지치기)
        else:
            for j in range(i, N):               # pick[i]에 들어갈 숫자 결정
                pick[i], pick[j] = pick[j], pick[i]
                f(i+1, N)
                pick[i], pick[j] = pick[j], pick[i]

for tc in range(1, TC+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]

    pick = list(range(N))                   # 각 줄의 pick할 idx를 0 ~ N-1의 순열로 표현
    sum_list = []
    f(0, N)

    print('#{} {}'.format(tc, sum_list[-1]))


