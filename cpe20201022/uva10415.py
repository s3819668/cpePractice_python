# times=int(input())

times=1
song=input()
#當前命令
def english(capital):
    a = -1
    b = -1
    for i in range(len(capital)):
        if i%2==0:
            a=capital[i]
        if i%2==1:
            b=capital[i]
        # print(a,b)
        if a != -1 and b >= a:
            for j in range(a-1, b):
                now[j]+=1
    compare(now,past)
#命令比較
def compare(now,past):
    for i in range(len(now)):
        if  now[i]==1 and past[i]!=now[i]:
            finger[i]+=1

    print("now is",now)
    print("past is",past)
    print("finger is:",finger)
    print()
#input轉換數字
def dict(eng):
    if eng=="c":
        return [2, 4, 7, 10]
    if eng=="d":
        return [2, 4, 7, 9]
    if eng=="e":
        return [2, 4, 7, 8]
    if eng=="f":
        return [2, 4, 7, 7]
    if eng=="g":
        return [2, 4]
    if eng=="a":
        return [2, 3]
    if eng=="b":
        return [2, 2]
    if eng=="C":
        return [3, 3]
    if eng=="D":
        return [1, 4, 7, 9]
    if eng=="E":
        return [1, 4, 7, 8]
    if eng=="F":
        return [1, 4, 7, 7]
    if eng=="G":
        return [1, 4]
    if eng=="A":
        return [1, 3]
    if eng=="B":
        return [1, 2]
    else:
        pass

for i in range(times):
    global finger
    finger = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # global now
    now=[0,0,0,0,0,0,0,0,0,0]
    # global past
    past=[0,0,0,0,0,0,0,0,0,0]
    for j in range(len(song)):
        now = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        english(dict(song[j]))
        past=now

