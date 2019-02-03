# password_cracker

IMPORTANT NOTES

1) In order to use the script please specify the text file that you are using with the extension when asked after launching the script.

    EX. hashedPasses.txt

2) The text file must NOT have an empty line at the end of the file.

3) cracker.py, rule2passwords.txt, 6digits.txt and 5charsReplaced.txt need to all be in the same folder.

4) The script is run using Python3.

5) The file that contains the hashed passwords of users must be in the same folder as cracker.py or the correct path must be provided.

6) The main dictionary that the cracker.py uses is /usr/share/dict/words and must be in that path for the script to work.

Running The Script

1) CD into the directory that contains cracker.py

2) In the terminal type: python3 cracker.py

3) Enter the path to the file that contains the hashed passwords of users if it is not in the same folder as cracker.py. 
   If the file is in the same folder just enter the name of the file along with its extension.

4) Wait for the cracker to crack the passwords or finish running through its rules.