loop=1
timeCount=0
while loop!=0:
    timeCount+=1
    ##
    ansLine=int(input("輸入答案行數"))
    ansArr=[]
    ansWord=[]
    for i in range(ansLine):
        ansStr=input("輸入答案")
        ansArr.append(ansStr)
        ansWord.append(len(ansStr))
    print(ansArr)
    print(ansWord)
    teamLine=int(input("輸入隊伍行數"))
    teamArr=[]
    teamWord = []
    ##
    for i in range(teamLine):
        teamStr=input("輸入隊伍答案")
        teamArr.append(teamStr)
        teamWord.append(len(teamStr))
    print(teamArr)
    print(teamWord)

    ##
    sumAnsWord=0
    for i in range(len(ansWord)):
        sumAnsWord+=ansWord[i]
    sumTeamWord=0
    for i in range(len(teamWord)):
        sumTeamWord+=teamWord[i]
    ##
    ansSapce=0
    for i in range(len(ansArr)):
        for j in ansArr[i]:
            if  j==" ":
                ansSapce+=1
    teamSapce=0
    for i in range(len(teamArr)):
        for j in teamArr[i]:
            if j==" ":
                teamSapce+=1
    ##
    consequence = "Accepted"
    # for i in range(len(teamArr)):
    if teamArr[i] != ansArr[i]:
        consequence = "Wrong Answer"

    if ansSapce!=teamSapce:
        consequence= "Presentation Error"

    print(teamSapce,ansSapce)
    print("Run #"+str(timeCount)+":",consequence, sumAnsWord)