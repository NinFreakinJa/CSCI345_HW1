# Foster_Guthrie_HW1_passwd_cracking.py
# Reid Foster, Ethan Guthrie
# 02/04/2020
# Cracks passwords which are generated using any one of the following rules:
#   1)  A seven-character word whose first character is capitalized and a
#       single-digit number is appended.
#   2)  A five-digit password with at least one of the following characters
#       in the beginning: * ~ ! #
#   3)  A five-character word where the letter 'a' is converted to '@' and
#       'l' is converted to '1'.
#   4)  A number up to seven digits in length (may have leading zeroes).
#   5)  A single word.
#
# IMPORTANT NOTE: For rules 1, 3, and 5, all words will be taken from a text
# file assumed to be in the directory '/usr/share/dict/words'.
#
# Passwords will be provided in a text file, one per line, following the
# below format:
#   Username:SHA-256_Password[:optional_parameters]

# Libraries named after authors of this assignment contain methods written
# by the author after whom the file was named.
from ethan import *
from reid import *
# The sys library allows for python to access command-line arguments.
from sys import argv

def main():
    # getInfoFromFile() located in ethan.py
    password_hashes = getHashesFromFile(argv[1])

    # singleWord() located in reid.py
    password_hashes = singleWord(password_hashes)

    # sevenCharWithDigit() located in reid.py
    password_hashes = sevenCharWithDigit(password_hashes)

    # fiveDigitWithSpecial() located in ethan.py
    password_hashes = fiveDigitWithSpecial(password_hashes)

    # fiveCharWordWithL33t() located in ethan.py
    password_hashes = fiveCharWordWithL33t(password_hashes)

    # upToSevenDigits() located in reid.py
    password_hashes = upToSevenDigits(password_hashes)

main()