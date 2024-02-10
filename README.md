# Workout-Project-2
The second workout project from ICS 32 class.

This program is able to encrypt or decrypt messages from text files using a transposition cipher. The program will first read in a text file and take in a secret key from the user. Then, the program will use that secret key to either scramble up the words of the text file into new positions, or rearrange the words of the text file into the positions they were originally. Finally the program will write the resulting message into another file provided by the user. The user will be able to tell the program what text file to read from and what file to write in by typing in the command line
- For Encryption: python wp2.py -e originaltext.txt newtext.txt key
- For Decryption: python wp2.py -d originaltext.txt newtext.txt key  