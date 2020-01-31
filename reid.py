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

WORD_DIR = "/usr/share/dict/words"

# Appends cracked hashes and passwords to the output file.
def appendToFile(cracked_hashes, cracked_passwords):
    print(len(cracked_passwords))
    with open("passwords.pot", "a") as file:
        for i in range(0, len(cracked_hashes)):
            file.write(cracked_hashes[i] + ":" + cracked_passwords[i] + "\n")

# Cracks a seven-character word whose first character is capitalized and a
# single-digit number is appended.
def sevenCharWithDigit(password_hashes):
    cracked_hashes = []
    cracked_passwords = []

    # Method body.

    appendToFile(cracked_hashes, cracked_passwords)
    return password_hashes

# Cracks a single word.
def singleWord(password_hashes):
    cracked_hashes = []
    cracked_passwords = []
    # Keep track of five and seven-char words to provide as input to
    # other methods.
    five_char_words = []
    seven_char_words = []

    # Method body.

    appendToFile(cracked_hashes, cracked_passwords)
    # Running other word-based attacks from here using only words that
    # meet length requirements.
    password_hashes = sevenCharWithDigit(password_hashes)
    return fiveCharWordWithL33t(password_hashes)

# Cracks a number up to seven digits in length (may have leading zeroes).
def upToSevenDigits(password_hashes):
    cracked_hashes = []
    cracked_passwords = []

    # Method body.

    appendToFile(cracked_hashes, cracked_passwords)
    return password_hashes