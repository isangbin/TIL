int_list = list(map(int, input().split()))

idx_list = []
a_list = []

d = 0

for i in enumerate(int_list) :
   idx_list.append(i)

for j in idx_list :
    if j[0] == 0 :
        a_list.append(j[1])
        d = j[1]

    elif j[1] != d :
        a_list.append(j[1])
        d = j[1]
    
    else :
        continue
print(a_list)

