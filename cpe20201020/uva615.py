array=[]
deg1=[]
dic1=dict()
loop=1
case=1
key=-2
def creatdic(array):
    global dic1
    for i in range(len(deg1)):
        if array[i] in dic1:
            dic1[array[i]] += 1
        else:
            dic1[array[i]] = 1
def findkey(dic,val):
    for i in dic:
        if dic[i] == val:
            return i
    return -1
largeloop=1
while largeloop==1:
    print(loop)
    while loop==1:
        print("in")
        user=input().split(" ")
        if user[0]=='-1'and user[1]=='-1':
            loop=0
            largeloop=0
            break
        for i in range(len(user)):
            if i%2==0:
                if user[i]=='0'and user[i+1]=='0':
                    loop=0
                    break
            deg1.append(user[i])
            print(deg1)
    while len(deg1)>1:
        print(deg1)
        creatdic(deg1)
        key=findkey(dic1,1)
        if key==-1:
            break
        dic1.clear()
        for i in range(len(deg1)):
            if deg1[i]==str(key):
                if i%2==0:
                    del deg1[i]
                    del deg1[i]
                else:
                    del deg1[i]
                    del deg1[i-1]
                break
    if key==-1 and user[0]!='-1'and user[1]!=-1:
        print("case", case ," is not a tree")
    if int(key)>-1 and user[0]!='-1'and user[1]!=-1:
        print("case", case ," is a tree")
        key=-2
    case+=1
    user.clear()
    deg1.clear()
    loop=1

