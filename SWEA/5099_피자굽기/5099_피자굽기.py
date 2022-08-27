# SWEA_5099 - 피자 굽기
# 220825

# 정답 코드
import sys
sys.stdin = open('sample_input.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())            # N=화덕크기, M=피자개수

    # idx 0번이 1번 피자임을 잊지 말자.
    cheese = list(map(int, input().split()))
    pizza = [0]*M
    for i in range(M):
        pizza[i] = [cheese[i], i+1]             # 피자 = [치즈, 피자번호]

    oven = [0]*N
    for i in range(N):                          # 오븐 꽉채우기
        oven[i] = pizza.pop(0)

    cnt = 0                                     # 완성 피자 수
    while cnt != M-1:                           # 피자 1개남을때까지 돌림

        if oven[0][0] != 0:                        # 맨앞피자가 미완성이면
            tmp = oven.pop(0)                   # 꺼내서
            tmp[0] = tmp[0] // 2                # 치즈 녹이기
            oven.append(tmp)                    # 그것을 맨뒤로 보냄

        else:                                   # 맨앞피자가 완성이면
            if len(pizza) != 0:                 # 새피자가 남았으면
                oven.pop(0)                     # 완성피자 꺼낸 뒤
                cnt += 1                        # 피자 완성 체크
                tmp = pizza.pop(0)              # 새피자 넣고
                tmp[0] = tmp[0] // 2            # 치즈 녹이기
                oven.append(tmp)                # 그것을 맨뒤로 보냄

            else:                               # 새피자 안남았으면
                oven.pop(0)                     # 완성피자만 꺼냄
                cnt += 1                        # 피자 완성 체크

    print('#{} {}'.format(tc, oven[0][1]))


