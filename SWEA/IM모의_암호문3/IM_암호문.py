import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10+1):
    N = int(input())                        # 원본 암호문의 길이
    pw = list(map(int, input().split()))    # 원본 암호문

    order_num = int(input())                # 명령어 개수
    order = list(map(str, input().split())) # 명령어

    cnt = 0
    while cnt != order_num:
        if order[0] == 'I':
            cnt += 1
            order.pop(0)
            x = int(order.pop(0))
            y = int(order.pop(0))
            s = [0] * y
            for i in range(y):
                s.append(int(order.pop(0)))

            # pw의 idx(x)에 for i in range(y): s 를 끼워넣는다.
            for i in range(y):
                pw.insert(x, s.pop(-1))

        elif order[0] == 'D':
            cnt += 1
            order.pop(0)
            x = int(order.pop(0))
            y = int(order.pop(0))

            # pw의 idx(x)부터 y개의 숫자를 삭제한다.
            for i in range(y):
                pw.remove(pw[x])

        elif order[0] == 'A':
            cnt += 1
            order.pop(0)
            y = int(order.pop(0))
            s = []
            for i in range(y):
                s.append(int(order.pop(0)))

            # pw의 맨 뒤에 y개의 s를 붙인다.
            for i in range(y):
                pw.append(s.pop(0))
        else:
            print('error')

    print('#{} '.format(tc), end='')
    for i in range(10):
        print(pw[i], end=' ')
    print()