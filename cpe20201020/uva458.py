loop=1
while loop==1:
    ori=input()##ord 轉數字 chr 轉ascii
    last=ord(ori[-1])
    lastcheck=ord('.')
    dif=last-lastcheck
    str1=""
    for i in range(len(ori)):
        str1+=chr((ord(ori[i]))-dif)
    print(str1)
