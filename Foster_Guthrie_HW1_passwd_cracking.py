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
    # Checking command line arguments.
    if len(argv) != 2 and len(argv) != 3:
        print("Usage: python3 Foster_Guthrie_HW1_passwd_cracking.py <input_file> [word_file]")
        return -1

    # Getting password hashes from file.
    password_hashes = getHashesFromFile(argv[1])

    # Testing to make sure hashes provided haven't already been solved in a
    # previous run. This is not intended to function as a rainbow table, as
    # it only works on consecuitive runs of the code.
    try:
        with open("passwords.pot", "r") as file:
            passwords_pot = file.readlines()
        reused = []
        for pair in passwords_pot:
            cracked_hash = pair.rstrip('\n').split(":")[0]
            for i in range(0, len(password_hashes)):
                if cracked_hash == password_hashes[i]:
                    reused.append(password_hashes[i])
                    if len(reused) == 1:
                        print("Some hashes have already been cracked during a previous run! These entries entries will be skipped (see passwords.pot for cracked hashes)!")
        password_hashes = list(set(password_hashes).difference(reused))
    except Exception as e:
        pass

    print("Starting....\n")
    # singleWord() located in reid.py
    password_hashes = singleWord(password_hashes, getWordDir(argv))

    # upToSevenDigits() located in reid.py
    password_hashes = upToSevenDigits(password_hashes)

    print("\n....done!")
    if password_hashes:
        print("Not all passwords could be cracked!")
    else:
        print("All passwords have been cracked!")

def getWordDir(args):
    if len(args) == 3:
        return argv[2]
    else:
        return "/usr/share/dict/words"

main()