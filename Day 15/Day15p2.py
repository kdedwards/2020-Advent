# Set some intitial variables
lstNumbersSpoken = [15, 5, 1, 4, 7, 0]
firstSpoken = True
iterations = 30000000
numbersSpoken = {}

# Build dictionary from the list given above, exlcuding the last element to be used to prime the loop below
for i in range(0, len(lstNumbersSpoken) - 1):
    numbersSpoken[lstNumbersSpoken[i]] = i
lastNumber = lstNumbersSpoken[-1]
# Run through the iterations updating the dictionary as needed
for i in range(len(numbersSpoken), iterations - 1):
    # This is not a new number, but we need to capture it's last position as it will be overwritten with the current iteration
    if firstSpoken is False:
        lastTimeSpoken = numbersSpoken[lastNumber]
    numbersSpoken[lastNumber] = i
    # Based on the rules, if it's the first time the number is said, the next number spoken will be 0, otherwise it will be the distance from the last time it was spoken
    if firstSpoken is True:
        nextNumber = 0
    else:
        nextNumber = i - lastTimeSpoken
    # Check to see if the nextNumber has already been said
    if nextNumber in numbersSpoken:
        firstSpoken = False
    else:
        firstSpoken = True
    # Debugging
    # print('Turn: {} lastNumber: {} nextNumber {}: numbersSpoken: {}'.format(i, lastNumber, nextNumber, numbersSpoken))
    # Setup the next iteration
    lastNumber = nextNumber
print('Last number spoken: {}. In the end {} unique numbers were said.'.format(lastNumber, len(numbersSpoken)))
