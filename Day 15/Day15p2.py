# numbersSpoken = [0, 3, 6]
numbersSpoken = {
    0: 0,
    3: 1,
    6: 2
}
iterations = 5
lastNumber = list(numbersSpoken.keys())[-1]

for i in range(len(numbersSpoken), iterations):
    print('Last number: {}.'.format(lastNumber))
    if lastNumber not in numbersSpoken:
        lastNumber = 0
        numbersSpoken[0] = i
    elif numbersSpoken[lastNumber] != i - 1:

# for i in range(len(numbersSpoken), iterations):
#    if numbersSpoken.count(numbersSpoken[i - 1]) == 1:
#        numbersSpoken.append(0)
#    else:
#        numbersSpoken.reverse()
#        lastTimeSpoken = numbersSpoken.index(numbersSpoken[0], 1)
#        numbersSpoken.reverse()
#        numbersSpoken.append(lastTimeSpoken)

print(numbersSpoken)

#print('Last number spoken: {}.'.format(numbersSpoken[-1]))
