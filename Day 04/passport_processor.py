import re
with open("C:\\Users\\dedwards\\projects\\2020-Advent\\Day 04\\passports.dat") as passportData:
    passportsRaw = passportData.readlines()


def validatePassport(passport):
    passportFields={'byr':[],'iyr':[],'eyr':[],'hgt':[],'hcl':[],'ecl':[],'pid':[],'cid':[],'valid':[]}
    fieldCount=0
    dataValid=True
    for field in passport:
        key=field.split(':')[0]
        value=field.split(':')[1]
        passportFields[key]=value
        fieldCount+=1
    if(((fieldCount==8) or (fieldCount==7 and passportFields['cid']==[]))):
        allFieldsPresent=True
    else:
        allFieldsPresent=False
        #print('Failed field check')

    if(allFieldsPresent):
        #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if(re.match(r'^\d{4}$',passportFields['byr'])==None or int(passportFields['byr']) < 1920 or int(passportFields['byr']) > 2002):
            dataValid=False
            #print('Failed byr (len!=4, outside 1920-2002)')

        #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if(re.match(r'^\d{4}$',passportFields['iyr'])==None  or int(passportFields['iyr']) < 2010 or int(passportFields['iyr']) > 2020):
            dataValid=False
            #print('Failed iyr (len!=4, outside 2010-2020)')

        #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if(re.match(r'^\d{4}$',passportFields['eyr'])==None  or int(passportFields['eyr']) < 2020 or int(passportFields['eyr']) > 2030):
            dataValid=False
            #print('Failed eyr (len!=4, outside 2020-2030)')

        #hgt (Height) - a number followed by either cm or in:
            #If cm, the number must be at least 150 and at most 193.
            #If in, the number must be at least 59 and at most 76.
        if(re.match(r'^\d{2,3}(in|cm)$',passportFields['hgt'])!=None):
            height=int(passportFields['hgt'][0:len(passportFields['hgt'])-2])
            if(re.match(r'^\d{2,3}cm$',passportFields['hgt'])!=None):
                if(height < 150 or height > 193):
                    dataValid=False
                    #print('Failed hgt (cm) 150-193')
            elif(re.match(r'^\d{2,3}in$',passportFields['hgt'])!=None):
                if(height < 59 or height > 76):
                    dataValid=False
                    #print('Failed hgt (in) 59-76')
            else:
                dataValid=False
                #print('Failed hgt invalid unit')
        else:
            dataValid=False
            #print('Failed hgt match')

        #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if(re.match(r'^#[0-9,a-f]{6}$',passportFields['hcl'])==None):
            #re.match(regex, content) is not None:
            dataValid=False
            #print('Failed hcl pattern match')

        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        validEyeColors=['amb','blu','brn','gry','grn','hzl','oth']
        if(passportFields['ecl'] not in validEyeColors):
            dataValid=False
            #print('Failed ecl valid list')

        #pid (Passport ID) - a nine-digit number, including leading zeroes.
        if(re.match(r'^[0-9]{9}$',passportFields['pid'])==None):
            #re.match(regex, content) is not None:
            dataValid=False
            #print('Failed pid pattern match')

        #cid (Country ID) - ignored, missing or not.

    if(allFieldsPresent and dataValid):
        passportFields['valid']=True
    else:
        passportFields['valid']=False
    if(passportFields['valid']==True):
        print(str(passportFields))
    return passportFields

passports=[]
thisPassport=[]

for line in passportsRaw:
    if(line=='\n'):
        passports.append(thisPassport)
        #print(thisPassport)
        thisPassport=[]
    else:
        thisPassport.extend(line.replace('\n','').split(' '))
passports.append(thisPassport)

validPassports=0
invalidPassports=0
for passport in passports:
    passportFields=validatePassport(passport)
    if(passportFields['valid']):
        validPassports+=1
    else:
        invalidPassports+=1

print('Valid passports: {} Invalid passports: {}'.format(validPassports, invalidPassports))
