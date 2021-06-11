loop=1
while loop==1:
    user=input().split(" ")
    for i in range(len(user)):
        user[i]=int(user[i])
    array=[]
    count=0
    used=[]
    for i in range(1,user[0]*2+1):
        if i%2==1:
            array.append([user[i],user[i+1]])
    for i in range(len(array)):
        for j in  range(len(array)-1):
            if array[i][1]>array[j][1]:
                array[i],array[j]=array[j],array[i]
    for i in range(array[0][1],0,-1):
        cand=[]
        for j in range(len(array)):#初選
            if array[j][1]>=i and array[j] not in used:
                cand.append(array[j])
        for j in range(len(cand)):#候選
            for k in range(len(cand)-1):
                if cand[j][0]>cand[k][0]:
                    cand[j],cand[k]=cand[k],cand[j]
        if cand!=[]:
            count+=cand[0][0]
            used.append(cand[0])
    print(count,end='')

