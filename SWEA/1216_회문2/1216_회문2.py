# SWEA_1216. 회문2
# 220816


# 정답코드
import sys
sys.stdin = open('input.txt', 'r')

# len 함수
def llen(a) :
    x = 0
    for i in a :
        x += 1
    return x

for tc in range(1, 10+1) :
    TC = int(input())
    letters = [list(input()) for _ in range(100)]

    tmp = []
    pelin = []
    
    # 가로로 검사
    for i in range(100) :
        for j in range(100) : # 어떠한 지점으로부터
            for k in range(100-j+1) : # 0부터 지점에서 끝까지의 거리 사이의 길이 k에 대하여
                for l in range(k) : # 지점에서 k길이만큼의 문자열이
                    tmp.append(letters[i][j+l])
                a = ''.join(tmp)
                tmp.reverse()
                b = ''.join(tmp)
                if a == b : # 회문이면 그 길이를 저장
                    pelin.append(llen(tmp))
                    tmp = []
                else :
                    tmp = []
    
    # 세로로 검사, 위와 같은 과정
    for j in range(100) :
        for i in range(100) :
            for k in range(100-i+1) :
                for l in range(k) :
                    tmp.append(letters[i+l][j])
                a = ''.join(tmp)
                tmp.reverse()
                b = ''.join(tmp)
                if a == b :
                    pelin.append(llen(tmp))
                    tmp = []
                else :
                    tmp = []

    max_pelin = 0
    for i in pelin : # 저장한 회문의 길이들에 대하여 최댓값 찾기
        if max_pelin <= i :
            max_pelin = i

    print('#{} {}'.format(TC, max_pelin))