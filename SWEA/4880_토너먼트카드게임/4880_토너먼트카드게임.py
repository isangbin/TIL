# SWEA_4881. 토너먼트 카드게임
# 220823

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

# 1가위 2바위 3보 게임 진행
def game(a, b):
    if card[a] == 1:
        if card[b] == 2:
            return b
        else:
            return a
    elif card[a] == 2:
        if card[b] == 3:
            return b
        else:
            return a
    else:
        if card[b] == 1:
            return b
        else:
            return a

# a, b는 인덱스를 의미
def slice(a, b):
    # 같으면 혼자니까 부전승
    if b - a == 0:
        return a
    # 1이면 둘이니까 대결
    elif b - a == 1:
        return game(a, b)
    # 이외엔 두명이하 남을때까지 slice
    else:
        return game(slice(a, (a+b)//2), slice((a+b)//2 + 1, b))



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    
    # idx 0번이 1번 학생이므로 +1 해야함
    ans = slice(0, N-1) + 1

    print('#{} {}'.format(tc, ans))