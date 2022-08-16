# SWEA_5432. 쇠막대기 자르기
# 220816
'''
시간초과 해결해야함
'''
# 정답코드
import sys
sys.stdin = open('sample_input.txt', 'r')

# len 함수
def llen(a) :
    x = 0
    for i in a :
        x += 1
    return x

TC = int(input()) # tc 수

for tc in range(1, TC+1) :
    pipes = input()

    #pipes = pipes.replace('()','1') # 헷갈리니까 레이저를 1로 바꾸고
    pipes = list(pipes) # index 접근 위해 리스트화

    cnt, c = 0, 1 # 아래 for문에서 pipes의 마지막항 )를 순회하지 않으므로 c에 미리 1 더해줌

    for i in range(llen(pipes) - 1) : # 전체에 대하여
        if pipes[i] == '(' and pipes[i+1] == ')' : # 현재 위치에 ()이 있으면
            c -= 1
            for j in range(i) : # 현재 위치 바로 앞까지 중에서
                # 레이저 하나는 a-b개만큼의 새로운 조각을 만들어냄
                if pipes[j] == '(' : # (의 개수 세기 : a
                    cnt += 1
                elif pipes[j] == ')' : # )의 개수 세기 : b
                    cnt -= 1
        elif pipes[i] == ')' : # )가 나오는 만큼 파이프가 스스로 끊어져 분할됨
            c += 1 # 레이저()에 있는 )는 위에 if에서 빼줬음

    ans = cnt + c
    print('#{} {}'.format(tc, ans))

