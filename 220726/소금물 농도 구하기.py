masses = []
count = 0
# Done을 입력할 때 까지 계속 퍼센트농도와 소금물의 양을 입력 받는다.
while count < 5 :

    mass = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오 : ')
    if mass == 'Done' :
        break
    else :
        masses.append(mass)
        count += 1
        

# 아래 연산에 사용할 빈 리스트 생성        
salt = []
water = []
temp=[]

# .split()을 이용해 농도와 소금물의 양을 나눈다.
for i in masses :
    temp.append(i.split('% '))

# .strip()을 이용해 소금물의 양에 붙어있는 g를 제거한 뒤 연산을 위해 int로 형변환 한다. 
for a,b in temp :
    salt.append(int(a)*int(b.strip('g')))
    water.append(int(b.strip('g')))

# 소금의 양과 소금물의 양을 구한다.
salts = 0
waters = 0
for i in salt :
    salts += i
for i in water :
    waters += i

# 농도를 계산 후 소수점 셋째자리에서 반올림한다.
percent = round(salts/waters, 2)
# 혼합물의 농도와 혼합물의 양을 출력한다.
print(f'{percent}% {waters}g')