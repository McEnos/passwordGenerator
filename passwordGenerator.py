import random
passwordList = []
def password(passlength):
    word = ''
    for letter in range(passlength):
        word += chr(random.choice(range(65,122)))
    passwordList.append(word)
    
#####function to generate a number of passwords
def passwordvalues(number,length):
    for i in range(number):
        password(length)
    return passwordList
