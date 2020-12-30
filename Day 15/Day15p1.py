numbersSpoken = [0, 3, 6]
iterations = 2020

for i in range(len(numbersSpoken), iterations):
    if i % 1000000 == 0:
        print(iterations)
    if numbersSpoken.count(numbersSpoken[i - 1]) == 1:
        numbersSpoken.append(0)
    else:
        numbersSpoken.reverse()
        lastTimeSpoken = numbersSpoken.index(numbersSpoken[0], 1)
        numbersSpoken.reverse()
        numbersSpoken.append(lastTimeSpoken)

print('Last number spoken: {}.'.format(numbersSpoken[-1]))
