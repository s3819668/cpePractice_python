def decoder(num,bef,aft):
    ten = 0
    for i in range(len(user[0])):
        if user[0][i] == "A":
            ten+=10*bef**(len(user[0]) - i - 1)
        elif user[0][i] == "B":
            ten += 11 * bef ** (len(user[0]) - i - 1)
        elif user[0][i] == "C":
            ten += 12 * bef ** (len(user[0]) - i - 1)
        elif user[0][i] == "D":
            ten += 13 * bef ** (len(user[0]) - i - 1)
        elif user[0][i] == "E":
            ten += 14 * bef ** (len(user[0]) - i - 1)
        elif user[0][i] == "F":
            ten += 15 * bef ** (len(user[0]) - i - 1)
        else:
            ten += int(user[0][i]) * bef ** (len(user[0]) - i - 1)
    result=""
    while ten>aft:
        remainder=ten%aft
        ten//=aft
        result=re(remainder)+result
    remainder=ten%aft
    result=re(remainder)+result
    return result
def re(num):
    if num==15:
        return "F"
    elif num==14:
        return "E"
    elif num==13:
        return "D"
    elif num==12:
        return "C"
    elif num==11:
        return "B"
    elif num==10:
        return "A"
    else:
        return str(num)
loop=1
while loop==1:
    user=input().split(" ")
    result=decoder(user[0],int(user[1]),int(user[2]))
    if len(result)>7:
        print("ERROR")
    else:
        print(result)

