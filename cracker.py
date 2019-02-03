import hashlib
import threading

##########################################################################
##                     Rules for passwords to have                      ##
##                                                                      ##
##  1) 7 character word from /usr/share/dict/words gets the 1st letter  ##
##     capitalized & a 1-digit number appended                          ##
##                                                                      ##
##  2) 10 digit password with at least one of the following special     ##
##     characters in the beginning: *, ~, !, #                          ##
##                                                                      ##
##  3) 5 character word from /usr/share/dict/words with the letter 'a'  ##
##     in it which gets replaced with any special character @ and the   ##
##     character 'l' is substituted by the number '1'.                  ##
##                                                                      ##
##  4) Any number that is made with digits up to 10 digits length       ##
##                                                                      ##
##  5) Any number of characters single word from /usr/share/dict/words  ##
##########################################################################

## Practice and testing how to compare hashes.
## Update works may be onto something.
def main():
    ## Grab the Text File With Passwords to Decrypt
    print("Please enter the text file with the hashed passwords: ")
    textFile = input()
    print("Reading in the file ", textFile)

    ## Read in the Text File with Passwords into a variable.
    hashedFile = open(textFile, "r")
    ## Split the file into lines denoted by new line characters
    hashedLines = hashedFile.read().split("\n")

    ## Printing for accuracy
    for line in hashedLines:
        #print(line)
        a =0 #deletelater
    print("Finished reading in ", textFile)
    ## Close the file
    hashedFile.close()

    ## Parse the encrypted password file here for later use
    ## Split at the ":" character; use join to join it together
    ## after finding the hashed password.
    userArr = []
    hashedPassArr = []
    ## Create separate arrays for Users and Hashed Passwords 
    ## to be passed into threading function
    for line in hashedLines:
        seq = line.split(":")
        user , hashedPass , rest = seq[0],seq[1], seq[2:]
        userArr.append(user)
        hashedPassArr.append(hashedPass)
    
    
    threads = []
    i = 0
    for i in range(len(userArr)):
        t = threading.Thread(target = getCracked, args = (userArr[i], hashedPassArr[i], i))
        threads.append(t)
        t.start()
    #getCracked(userArr[0], hashedPassArr[0])
    #getCracked(userArr[1], hashedPassArr[1])
    #getCracked(userArr[2], hashedPassArr[2])
        


#function to run all rules (passed into each thread)
def getCracked(username, hashedPassword, threadNumber):
    ## Open the text file for the wordlist
    currThreadNum = threadNumber
    print("beginning cracking in thread " , currThreadNum , " ...\n")
    currUser = username
    currHashedPassword = hashedPassword
    print("The user is: " + currUser + " Their Password is: " + currHashedPassword + "\n")
    rule1(currUser, currHashedPassword, currThreadNum)
    rule3(currUser, currHashedPassword, currThreadNum)
    rule4(currUser, currHashedPassword, currThreadNum)
    ## Remove later used for testing the parsing of the file
    ## and formatting everything to required formats
    exit()


##################################################
## Rule 1:                                      ##
## 7 character word from /usr/share/dict/words  ##
## gets the 1st letter capitalized & a 1-digit  ##
## number appended                              ##
##################################################
def rule1(user, password, threadNum):
    print("Reading in text file /usr/share/dict/words...\n")
    
    ## Read in the dictionary of words
    ## Read the file and split on space & store into words
    ## Close the file
    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()

    print("Finished reading in text file /usr/share/dict/words...\n")
    print("Thread " , threadNum ," trying rule 1...\n")
    ## Iterate through the entire list
    for i in range(len(words) - 1):
        ## Reset the hash for every new word tested
        m = hashlib.sha256()

        ## If the word is exactly 7 characters try
        ## it as a password.
        if((len(words[i])) == 7):
            
            ## Set newWord to capitalized version of words at i
            newWord = words[i].capitalize()

            ## Iterate through and append a single digit from
            ## 0-9 to the end of the word
            for j in range(10):

                ## Reset the hash for every updated
                ## run involved a new number added to end
                m = hashlib.sha256()
            
                ## Add a number between and including 0-9
                ## to the end of the word being tested.
                newWord += str(j)

                ## Encode the word because Hashlib said so
                encodedWord = newWord.encode('utf-8')

                ## Update the word being hashed and compared to
                ## the hashed password in the file
                m.update(encodedWord)
            
                ## Digest the hashed word using hexdigest()
                hashedWord = m.hexdigest()

                ## If the hashed password matches the string
                ## that was recovered from the user entered file
                ## then the password has been found.
                if(hashedWord == password):
                    ##### Write to file??? ####
                    print("Thread", threadNum , "cracked password successfully\n")
                    print("User: ", user, "\nPassword is: ", encodedWord)

                    ## Close the thread after outputting the
                    ## results to a file in the correct format
                    exit()
            
                ## Reset the word back to original
                ## word without digits appended to it
                newWord = words[i].capitalize()

def rule2(user, password, threadNum):
    ## Read in txt file that was created and submitted
    ## Store them into guesses then close the file
    f = open("rule2passwords.txt", "r")
    guesses = f.read().split("\n")
    f.close()
    print("Thread " , threadNum , " trying rule 3...\n")

    ## Iterate through every line in the array
    for guess in guesses:
        ## Begin the hashlib 256 function
        m = hashlib.sha256()
        
        ## Encode the guess into 'utf-8'
        ## update it into m
        ## Hash the guess
        encodedGuess = guess.encode('utf-8')
        m.update(encodedGuess)
        hashedGuess = m.hexdigest()

        ## If the password hash in the file
        ## equals the hashed guess found a
        ## a match
        if(password == hashedGuess):
            print("\nThread", threadNum , "cracked password successfully")
            print("User: ", user, "\nPassword is: ", guess)
            exit()

##################################################
## Rule 3:                                      ##
## 5 character word from /usr/share/dict/words  ##
## with the letter 'a' in it which gets replaced## 
## with any special character @ and the         ##
## character 'l' is substituted by the number 1 ## 
##################################################
def rule3(user, password, threadNum):
    
    ## Read in txt file that was created and submitted
    ## Store them into guesses then close the file
    f = open("5charsReplaced.txt", "r")
    guesses = f.read().split("\n")
    f.close()
    print("Thread " , threadNum , " trying rule 3...\n")

    ## Iterate through every line in the array
    for guess in guesses:
        ## Begin the hashlib 256 function
        m = hashlib.sha256()
        
        ## Encode the guess into 'utf-8'
        ## update it into m
        ## Hash the guess
        encodedGuess = guess.encode('utf-8')
        m.update(encodedGuess)
        hashedGuess = m.hexdigest()

        ## If the password hash in the file
        ## equals the hashed guess found a
        ## a match
        if(password == hashedGuess):
            print("\nThread", threadNum , "cracked password successfully")
            print("User: ", user, "\nPassword is: ", guess)
            exit()


##################################################
## Rule 4:                                      ##
## Any number that is made with digits up to    ##
## 10 digits length                             ##
##################################################
def rule4(user, password, threadNum):
    ## Read in txt file that was created and submitted
    ## Store them into guesses then close the file
    f = open("6digits.txt", "r")
    guesses = f.read().split("\n")
    f.close()
    print("Thread " , threadNum , " trying rule 4...\n")
    ## Iterate through every line in the array
    for guess in guesses:
        ## Begin the hashlib 256 function
        m = hashlib.sha256()
        
        ## Encode the guess into 'utf-8'
        ## update it into m
        ## Hash the guess
        encodedGuess = guess.encode('utf-8')
        m.update(encodedGuess)
        hashedGuess = m.hexdigest()

        ## If the password hash in the file
        ## equals the hashed guess found a
        ## a match
        if(password == hashedGuess):
            print("\nThread", threadNum , "cracked password successfully")
            print("User: ", user, "\nPassword is: ", guess)
            exit()


##################################################
## Rule 5:                                      ##
## Any number of characters single word from    ##
## /usr/share/dict/words                        ##
##################################################
def rule5(user, password, threadNum):
    print("Reading in text file /usr/share/dict/words...")
    
    ## Read in the dictionary of words file
    ## Store it into words and split on "\n"
    ## Close the file
    f = open("/usr/share/dict/words", "r")
    words = f.read().split("\n")
    f.close()
    print("Thread " , threadNum , " trying rule 5...\n")
    ## Iterate through all the words in the file
    for word in words:
        
        ## Update m every new word that is being tested
        m = hashlib.sha256()
        
        ## Check for match if NO spaces are in the word
        if(" " not in word):
            
            ## Encode the word into 'utf-8'
            ## Update m with encoded word
            ## Hash the word
            encodedWord = word.encode('utf-8')
            m.update(encodedWord)
            hashedWord = m.hexdigest()

            ## Compare hashedWord with hash in file
            ## If they match it is the password
            if(password == hashedWord):
                print("Thread", threadNum , "cracked password successfully")
                print("User: ", user, "\nPassword is: ", guess)
                exit()

            
main()