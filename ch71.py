import re

phoneNumRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo= phoneNumRegex.search('My number is 455-567-4242')
print('Phone Number found '+ mo.group())





'''
def isPhoneNumber(text):
    if(len(text) != 12):
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


number=input()
print(isPhoneNumber(number))
'''

