import sys
N = int(sys.stdin.readline())


def pick(classes):
    global cnt
    tmp1 = classes.pop(0)
    for k in classes:
        if k[1] >= tmp1[0]:
            tmp2.append(k)
        else:
            tmp3.append(k)

    if len(tmp2) == 0:
        if len(tmp3) != 0:
            cnt += 1
            pick(tmp3)
        else:
            return
    else:
        pick(tmp2)


classes = [0]*N
for i in range(N):
    S, T = map(int, sys.stdin.readline().split())
    classes[i] = [T, S]

classes.sort()
tmp2 = []           # 같은 강의실
tmp3 = []           # 다른 강의실에서 들어야만 하는 강의들
cnt = 1
pick(classes)

print(cnt)