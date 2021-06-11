





def div_find(num):
    if num==1:
        return 1
    dic={}
    now=2
    while num>1:

        for i in range(now,num+1):
            if num%i==0:
                now=i
                num=int(num/i)
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
                break



        #for< 校正
        if now==num:
            dic[num]+=1
            num=int(num/now)
        d=1
        for k in dic:
            d*=dic[k]+1
    return d
times=int(input())
for i in range(times):
    number={}
    user=int(input())
    for j in range(1,user+1):
        number[j]=div_find(j)

    number=sorted(number.items(),key=lambda x:x[1],reverse=True)
    best_value=0
    best_number=0
    for j in number:
        if  j[1]>=best_value and j[0]>best_number:
            best_value=j[1]
            best_number=j[0]
        else:
            break
    print(best_number)


