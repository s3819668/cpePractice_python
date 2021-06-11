def create_data(N,M):
    x=[1,2,3]
    for i in range(3,N):
        x.append((x[i-1]+x[i-2]+x[i-3])%M+1)
    return x
def create_target(k):
    y=[]
    for i in range(k):
        y.append(i+1)
    return y

times=int(input())
for i in range(times):
    #資料建立
    user=input().split()
    for j in user:
        N=int(user[0])
        M=int(user[1])
        K=int(user[2])
    data=create_data(N,M)
    target=create_target(K)
    print(data,target)
    #
    target_count = 0
    for j in range(len(data)):
        if target[target_count]==data[j]:
            data_count=j
            target_count+=1
        if target_count==len(target):
            break

    if  target_count<len(target):
        print("Case",i+1,": ","sequence nai")
    else:
        print("Case", i + 1,": ",data_count)

