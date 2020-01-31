# ethan.py
# Ethan Guthrie
# 02/04/2020
# Provides the following methods:
#   fiveCharWordWithL33t()
#   fiveDigitWithSpecial()
#   getInfoFromFile()
#
# All methods will be provided with a list of hashes as input, and will exit
# once all hashes are cracked or all possibilities for that method are
# exhausted. Whenever a combination is found, it must be printed to the
# screen and written to the an output file. Additionally, each method should
# return a list of the remaining hashes.

# Appends cracked hashes and passwords to the output file.
def appendToFile(cracked_hashes, cracked_passwords):
    print(len(cracked_passwords))
    with open("passwords.pot", "a") as file:
        for i in range(0, len(cracked_hashes)):
            file.write(cracked_hashes[i] + ":" + cracked_passwords[i] + "\n")

# Cracks a five-character word where the letter 'a' is converted to '@' and
# 'l' is converted to '1'.
def fiveCharWordWithL33t(password_hashes):
    cracked_hashes = []
    cracked_passwords = []

    # Method body.

    appendToFile(cracked_hashes, cracked_passwords)
    return password_hashes

# Cracks a five-digit password with at least one of the following characters
# in the beginning: * ~ ! #
# means 4 numbers with a special character in front
# method is called from inside upToSevenDigits function if on a 4 digit number so that number generation is only needed once
def fiveDigitWithSpecial(password_hashes,testValue):
    cracked_hashes = []
    cracked_passwords = []

    # Method body.

    appendToFile(cracked_hashes, cracked_passwords)
    return password_hashes

# Gets hashes from the provided text file which follow the below format:
#   Username:SHA-256_Password[:optional_parameters]
def getHashesFromFile(inFile):
    with open(inFile, "r") as file:
        lines = file.readlines()
    for i in range(0, len(lines)):
        line = lines[i].split(':')
        lines[i] = line[1]
    return lines