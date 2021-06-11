times=int(input())
for i in range(times):
    tarray=[]
    setA=set()
    days=int(input())
    teams=int(input())
    for j in range(teams):
        dt=int(input())
        for k in range(dt,days+1,dt):
            setA.add(k)
    tarray=list(setA)
    tarray.sort()
    for j in range(6,days,7):
        if  j in setA:
            setA.remove(j)
    for j in range(7,days,7):
        if  j in setA:
            setA.remove(j)
    print(len(setA))