with open("customsanswers.dat") as customsData:
    customsAnswersRaw = customsData.readlines()

answerGroups=[]
thisAnswerGroup=[]

for line in customsAnswersRaw:
    if(line=='\n'):
        answerGroups.append(thisAnswerGroup)
        #print(thisPassport)
        thisAnswerGroup=[]
    else:
        thisAnswerGroup.extend(line.replace('\n','').split(' '))
answerGroups.append(thisAnswerGroup)

groupSummaries=[]

for answerGroup in answerGroups:
    groupSummary=[]
    for answer in answerGroup:
        answers=list(answer)
        for answer in answers:
            if(answer not in groupSummary):
                groupSummary.append(answer)
    groupSummary.sort()
    groupSummaries.append(groupSummary)
    #print('List: {} Len: {}'.format(str(groupSummary), len(groupSummary)))

total=0
for groupSummary in groupSummaries:
    print('List: {} Len: {}'.format(str(groupSummary), len(groupSummary)))
    total+=len(groupSummary)
    #print(groupSummary.count())

print('Total answers: {}'.format(total))
