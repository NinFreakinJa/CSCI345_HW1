# reid.py
# Reid Foster
# 02/04/2020
# Provides the following methods:
#   sevenCharWithDigit()
#   singleWord()
#   upToSevenDigits()
#
# All methods will be provided with a list of hashes as input, and will exit
# once all hashes are cracked or all possibilities for that method are
# exhausted. Whenever a combination is found, it must be printed to the
# screen and written to the an output file. Additionally, each method should
# return a list of the remaining hashes. 

# fiveCharWordWithL33t() to run after singleWord() methods finds all five-
# character words.
from ethan import fiveCharWordWithL33t
from ethan import fiveDigitWithSpecial
from hashlib import sha256

WORD_DIR = "/usr/share/dict/words"

# Prints and appends cracked hashes and passwords to the output file.
def appendToFile(cracked_hashes, cracked_passwords):
    with open("passwords.pot", "a") as file:
        for i in range(0, len(cracked_hashes)):
            print(cracked_hashes[i] + ":" + cracked_passwords[i])
            file.write(cracked_hashes[i] + ":" + cracked_passwords[i] + "\n")

# Cracks a seven-character word whose first character is capitalized and a
# single-digit number is appended.
# Called within main dictionary cracking method
def sevenCharWithDigit(password_hashes,testValue):
    #returns None if nothing to test
    if not password_hashes:
        return None

    temp=testValue.capitalize()
    #Tested with each number
    for i in range(10):
        temp2=temp+str(i)
        # Hash resulting string.
        hashTest=sha256(str.encode(temp2)).hexdigest()

        # Testing for equivalence against provided hashes.
        for j in range(0, len(password_hashes)):
            if password_hashes[j] == hashTest:
                appendToFile([hashTest], [temp2])
                password_hashes.pop(j)
                return password_hashes

    return password_hashes

    '''
        # Test each password
        cracked_hashes=[j for j in password_hashes if (hashTest==j)]
        cracked_passwords=None
        #Remove found passwords
        password_hashes=[k for k in password_hashes if k not in cracked_hashes]
        for k in range(len(cracked_hashes)):
            cracked_passwords.append(temp2)
        appendToFile(cracked_hashes,cracked_passwords)
        #for j in password_hashes:
        #    if (hashTest==j):
         #           appendToFile([hashTest],[temp2])
          #          password_hashes.remove(j)
    return password_hashes
    '''

# Cracks a single word.
def singleWord(password_hashes):
    cracked_hashes = []
    cracked_passwords = []
    with open(WORD_DIR, "r") as file:
        lines = file.readlines()
    # Read each word from the dictionary
    for i in range(0, len(lines)):
        # Quits if nothing to test
        if not password_hashes:
            return None
        else:
            word=lines[i].rstrip("\n")
            # Calls other dictionary cracking methods if requirements are met
            if(len(word)==7):
                password_hashes=sevenCharWithDigit(password_hashes,word)
            elif(len(word)==5 and ("a" in word or "l" in word)):
                password_hashes=fiveCharWordWithL33t(password_hashes,word)

            # Hash word.
            hashTest=sha256(str.encode(word)).hexdigest()

            # Testing for equivalence against provided hashes.
            for j in range(0, len(password_hashes)):
                if password_hashes[j] == hashTest:
                    cracked_hashes.append(password_hashes[j])
                    cracked_passwords.append(word)
                    password_hashes.pop(j)
    
    appendToFile(cracked_hashes, cracked_passwords)
    return password_hashes

    '''
            # Test each password
            cracked_hashes=[j for j in password_hashes if (hashTest==j)]
            cracked_passwords=None
            #Remove found passwords
            password_hashes=[k for k in password_hashes if k not in cracked_hashes]
            for k in range(len(cracked_hashes)):
                cracked_passwords.append(word)
            appendToFile(cracked_hashes,cracked_passwords)
    return password_hashes
    '''

# Cracks a number up to seven digits in length (may have leading zeroes).
def upToSevenDigits(password_hashes):
    #all work is done in recursive helper function
    password_hashes=__digitHelper(password_hashes,None)
    return password_hashes

#Recursive helper function to test all possible digit combinations
def __digitHelper(password_hashes, currTest):
    #if no passwords to test return
    if not password_hashes:
        return None
    #default parameter
    elif (currTest is None):
        return __digitHelper(password_hashes,"")
    else:
        #if the string is not empty
        if currTest:
            #create and compare hashes
            hashTest=sha256(str.encode(currTest)).hexdigest()
            cracked_hashes=[j for j in password_hashes if (hashTest==j)]
            cracked_passwords=None
            password_hashes=[k for k in password_hashes if k not in cracked_hashes]
            for k in range(len(cracked_hashes)):
                cracked_passwords.append(currTest)
            appendToFile(cracked_hashes,cracked_passwords)
            #for i in password_hashes:
             #   if (hashTest==i):
              #      appendToFile([hashTest],[currTest])
               #     password_hashes.remove(i)
        #if the function is 4 digits long it will check the five digit with special requirement
        if(len(currTest)==4):
            password_hashes=fiveDigitWithSpecial(password_hashes,currTest)
        #recursively creates all possible digit combinations up to 7 digits
        if(len(currTest)<7):
            for i in range(10):
                password_hashes=__digitHelper(password_hashes,currTest+str(i))
        #returns updated list of unsolved password hashes
        return password_hashes

