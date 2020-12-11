with open("customsanswers.dat") as customsData:
    customsAnswersRaw = customsData.readlines()

answerGroups=[]
thisAnswerGroup=[]

for line in customsAnswersRaw:
    if(line=='\n'):
        answerGroups.append(thisAnswerGroup)
        thisAnswerGroup=[]
    else:
        thisAnswerGroup.extend(line.replace('\n','').split(' '))
answerGroups.append(thisAnswerGroup)

groupSummaries=[]

for answerGroup in answerGroups:
    groupSummary={}
    groupSummary['answerCount']=0
    for answer in answerGroup:
        groupSummary['answerCount']+=1
        answers=list(answer)
        for answer in answers:
            if(answer in groupSummary):
                groupSummary[(answer)]+=1
            else:
                groupSummary[(answer)]=1
    groupSummaries.append(groupSummary)

allYesTotal=0
for groupSummary in groupSummaries:
    for key in groupSummary:
        if(groupSummary[key] == int(groupSummary['answerCount']) and key != 'answerCount'):
            allYesTotal+=1

print('Total answers that are all Yes: {}'.format(allYesTotal))
