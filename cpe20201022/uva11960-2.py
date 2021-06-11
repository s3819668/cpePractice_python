import threading

def divFind(target):
    if  target==1:
        return 1
    i=0
    dic={}
    now=table[i]
    while target>=now:
        now = table[i]
        if target %now==0:
            target/=now
            if now not in dic:
                dic[now]=1
            else:
                dic[now]+=1
        else:
            i+=1
    d=1
    for i in dic:
        d*=dic[i]+1
    return d



def createTable(target):
    global table
    for i in range(2,target+1):
        isPrime=True
        for j in range(2,int(i**0.5)+1):
            if  i%j==0:
                isPrime=False
                break
        if  isPrime==True:
            table.append(i)

###main
table=[]
# print(table)
times=int(input())
dic={}
for i in range(times):
    table.clear()
    target=int(input())
    createTable(target)


    for j in range(1,target+1):
        dic[j]=divFind(j)



    print(dic)

