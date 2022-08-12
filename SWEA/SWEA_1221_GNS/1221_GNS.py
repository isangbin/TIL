# SWEA 1213. String
# 220812

# 정답코드
import sys

sys.stdin = open('input.txt', 'r', encoding='UTF8')

TC = int(input())

for tc in range(1, TC + 1):
    a, N = map(str, input().split())
    text = list(map(str, input().split()))

    list1 = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    ans = []
    for i in range(10) : # 0부터 9까지 순서로
        for j in range(int(N)) : # text의 요소 j에 대하여
            if list1.index(text[j]) == i : # 해당 요소가 의미하는게 i 이면
                ans.append(text[j]) # ans에 추가한다. (0부터 9까지 순서대로 추가가 된다.)
    
    print('#{}'.format(tc))
    for i in ans :
        print(i, end=' ')
    print()