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

from hashlib import sha256

# Prints and appends cracked hashes and passwords to the output file.
def appendToFile(cracked_hashes, cracked_passwords):
    with open("passwords.pot", "a") as file:
        for i in range(0, len(cracked_hashes)):
            print(cracked_hashes[i] + ":" + cracked_passwords[i])
            file.write(cracked_hashes[i] + ":" + cracked_passwords[i] + "\n")

# Cracks a five-character word where the letter 'a' is converted to '@' and
# 'l' is converted to '1'.
def fiveCharWordWithL33t(password_hashes, test_value):

    # Swapping characters for l33t characters.
    for i in range(0, len(test_value)):
        if test_value[i] == "a":
            test_value = test_value[:i] + "@" + test_value[i + 1:]
        elif test_value[i] == "l":
            test_value = test_value[:i] + "1" + test_value[i + 1:]

    # Hashing resulting string.
    test_value_hash = sha256(str.encode(test_value)).hexdigest()

    # Testing for equivalence against provided hashes.
    for i in range(0, len(password_hashes)):
        if password_hashes[i] == test_value_hash:
            appendToFile([test_value_hash], [test_value])
            password_hashes.pop(i)
            break

    return password_hashes

# Cracks a five-digit password with at least one of the following characters
# in the beginning: * ~ ! #
# This method is called from inside upToSevenDigits function on a 4-digit
# number so that number generation is only needed once.
def fiveDigitWithSpecial(password_hashes, test_value):
    special_characters = ['*', '~', '!', '#']
    for i in special_characters:
        test_value_hash = sha256(str.encode(i + test_value)).hexdigest()
        for j in range(0, len(password_hashes)):
            if password_hashes[j] == test_value_hash:
                appendToFile([test_value_hash], [i + test_value])
                password_hashes.pop(j)
                return password_hashes

    return password_hashes

# Gets hashes from the provided text file which follow the below format:
#   Username:SHA-256_Password[:optional_parameters]
def getHashesFromFile(inFile):
    with open(inFile, "r") as file:
        lines = file.readlines()
    for i in range(0, len(lines)):
        line = lines[i].split(':')
        lines[i] = line[1]
    file.close()
    return lines