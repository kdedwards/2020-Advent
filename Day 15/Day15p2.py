# numbersSpoken = [0, 3, 6]
numbersSpoken = {
    0: 0,
    3: 1,
    6: 2
}
iterations = 7
lastNumber = list(numbersSpoken.keys())[-1]
print('Starting number: {}'.format(lastNumber))
print(numbersSpoken)
for i in range(len(numbersSpoken), iterations):
    print('Iteration: {} numbersSpoken: {}'.format(i, numbersSpoken))
    if (lastNumber not in numbersSpoken.keys()) != (numbersSpoken[lastNumber] == (i - 1)):
        print('Number {} never spoken.'.format(lastNumber))
        lastNumber = 0
    elif (lastNumber in numbersSpoken) and (numbersSpoken[lastNumber] == (i - 1)):
        lastNumber = i - numbersSpoken[lastNumber]
        print('1-Number {} was exact previous number'.format(lastNumber))
    else:
        print('2-Number {} was not previous number'.format(lastNumber))
    numbersSpoken[lastNumber] = i
    print('Last number: {}.'.format(lastNumber))
print(numbersSpoken)

# for i in range(len(numbersSpoken), iterations):
#    if numbersSpoken.count(numbersSpoken[i - 1]) == 1:
#        numbersSpoken.append(0)
#    else:
#        numbersSpoken.reverse()
#        lastTimeSpoken = numbersSpoken.index(numbersSpoken[0], 1)
#        numbersSpoken.reverse()
#        numbersSpoken.append(lastTimeSpoken)
#print('Last number spoken: {}.'.format(numbersSpoken[-1]))
