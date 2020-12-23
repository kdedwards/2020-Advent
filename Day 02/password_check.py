with open("password_db.dat") as passwordData:
    passwordEntries = passwordData.read().split('\n')

passwordOK = 0
passwordBad = 0

for entry in passwordEntries:
    charMin = int(entry.split('-')[0])
    charMax = int(entry.split('-')[1].split(' ')[0])
    char = entry.split(' ')[1].split(':')[0]
    password = entry.split(' ')[2]
    # print('Line: {} charMin: {} charMax: {} char: {} password: {}'.format(entry, charMin, charMax, char, password))
    if(password.count(char) >= charMin and password.count(char) <= charMax):
        passwordOK += 1
    else:
        passwordBad += 1

print('Good passwords: {} Bad passwords: {}'.format(passwordOK, passwordBad))

passwordOK = 0
passwordBad = 0

for entry in passwordEntries:
    charFirst = int(entry.split('-')[0])
    charSecond = int(entry.split('-')[1].split(' ')[0])
    char = entry.split(' ')[1].split(':')[0]
    password = entry.split(' ')[2]
    # print('Line: {} charMin: {} charMax: {} char: {} password: {}'.format(entry, charFirst, charSecond, char, password))

    if((len(password) >= charFirst and password[charFirst - 1] == char) ^ (len(password) >= charSecond and password[charSecond - 1] == char)):
        passwordOK += 1
    else:
        passwordBad += 1

print('Good passwords: {} Bad passwords: {}'.format(passwordOK, passwordBad))
