def getWork(work):
    ran=work//2
    global array
    for i in range(1,2+1):
        array.append(ran*i)
    return array
array=[]
array.append(0)

getWork(100)
print(array)
for i in range(2):
    for j in range(array[i]+1,array[i+1]+1):
        print(j)