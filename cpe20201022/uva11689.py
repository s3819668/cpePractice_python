times=int(input())

while times>0:
    times-=1
    user=input().split(" ")
    for i in range(len(user)):
        user[i]=int(user[i])
    bottle=user[0]+user[1]
    change=user[2]
    soda=0
    while bottle>=change:
        freeSoda=int(bottle/change)
        soda+=freeSoda
        bottle=bottle%change
        bottle+=freeSoda
    print(soda)
