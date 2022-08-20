# SWEA 1213. String
# 220812

# 정답코드
import sys

sys.stdin = open('input.txt', 'r', encoding='UTF8')

def Len(string) :
    length = 0
    for i in string :
        length += 1
    return length

for tc in range(1, 10 + 1):
    TC = int(input())
    target = input()
    text = input()

    cnt = 0 # text 내에서 target이 등장한 횟수
    for i in range(Len(text) - Len(target) + 1) : # text의 처음부터 끝까지 순회 (indexError 방지 필수)
        for j in range(Len(target)) : # target의 각 자리를 순회
            if text[i+j] != target[j] : # text의 현위치와 target의 글자가 같은지 확인 (target길이만큼)
                break # 다르면 탈출
        else : # for문이 break에 안걸렸으면 target이 발견된 것이므로 
            cnt += 1 # cnt에 1 추가

    print('#{} {}'.format(TC, cnt))