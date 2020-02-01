# CSCI345_HW1
### Reid Foster, Ethan Guthrie

## Usage
Run the script using the following syntax:
```
python Foster_Guthrie_HW1_passwd_cracking.py <input_file> [word_file]
```
```input_file``` is assumed to be a text file containing password hashes in the format ```Username:SHA-256_Password[:optional_parameters]```


```word_file``` is assumed to be a text file containing a list of dictionary words separated one per line which is assumed to be ```/usr/share/dict/words``` unless otherwise specified.