import hashlib

##Rules for passwords to have##
##
##  1) 7 character word from /usr/share/dict/words
##     gets the 1st letter capitalized & a 1-digit
##     number appended
##
##  2) 10 digit password with at least one of the
##     following special characters in the 
##     beginning: *, ~, !, #
##
##  3) 5 character word from /usr/share/dict/words
##     with the letter 'a' in it which gets
##     replaced with any special character @ and 
##     the character 'l' is substituted by the 
##     number '1'. 
##
##  4) Any number that is made with digits up to
##     10 digits length
##
##  5) Any number of characters single word from
##     /usr/share/dict/words

## Potential setup:
## Create a menu that will read user input and do guesses off of that? (This menu may be handled differently based on what Dr. X wants)
## iterate through the list of words based off of rule and try each successful match to the rule.
##  while(!cracked OR !NoMoreGuessesInFile)
##      If EndOfFileCharacter (Essentially NoMoreGuessesInFile)
##          Update the !NoMoreGuessesInFile variable to kick out of while loop
##      Else If word does not match go to next word
##          Find the next matching word
##      else hash that word then compare that to the hash portion in the line
##          If hashes match update !cracked to kick out of while loop
##  If(cracked)
##      output password
##  Else
##      Ask the user if they want to run a different rule set? (Based on requirements)
##      

## Practice and testing how to compare hashes.
## Update works may be onto something.

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
    print(line)
print("Finished reading in ", textFile)
## Close the file
hashedFile.close()

## Parse the encrypted password file here for later use
## Split at the ":" character; use join to join it together
## after finding the hashed password.


## Open the text file for the wordlist
print("Reading in text file /usr/share/dict/words...")
f = open("/usr/share/dict/words", "r")
## Read the file and split on space
words = f.read().split()
## Close the file
f.close()
print("Finished reading in text file /usr/share/dict/words...")

## Remove later used for testing the parsing of the file
## and formatting everything to required formats
exit()

#m = hashlib.sha256()
#print(list(words[102400]))


############# TO DO ###############
## Create enough threads for all the passwords/rules
## Need to figure out how to stop running application
## Once password has been found
## Potentially exit() to stop thread from continuing

## May want to look into creating a rainbow table with 
## the rules for the numbers as well.
## Thread will need to have the string stored before 
## further testing can take place
##################################


## decide how the threads will guess which rule to use
for i in range(len(words) - 1):

## Testing for one iteration Remove later
#for i in range(1):

    ## Reset the hash for every new word tested
    m = hashlib.sha256()

    ## This is the rule for 7 character word with one 
    ## digit appended to the end of the word
    if((len(words[i])) == 7):

        #print(words[i])
        newWord = words[i].capitalize()
        for j in range(10):
            ## Reset the hash for every updated
            ## run involved a new number added to end
            m = hashlib.sha256()
            
            ## Add a number between and including 0-9
            ## to the end of the word being tested.
            newWord += str(j)

            ## Encode the word because Hashlib said so
            encodedWord = newWord.encode('utf-8')

            ## Testing the word being used with added digit
            #print(newWord)

            ## Testing portion Remove later
            #ultraword = "Puzzles42"
            #print(ultraword)

            ## Update the word being hashed and compared to
            ## the hashed password in the file
            hashed = m.update(encodedWord)

            ## Testing purposes for single use for accurate results
            #hashed = m.update(ultraword.encode('utf-8'))
            #string = "c1df467d16a2ebea8b48482c10d6c640e163c69f5da3dfba4c442002e5e15fa9"
            
            ## Digest the hashed word using hexdigest()
            hashed = m.hexdigest()

            ## Test the hashed word for visual confirmation
            print(hashed)

            ## If the hashed password matches the string
            ## that was recovered from the user entered file
            ## then the password has been found.
            if(hashed == string):
                ##Testing statements Remove later##
                print("Password Should be: Atari/'s2\n")
                #print("Hashes equal each other")
                print("Password is ", newWord)


                ## Close the thread after outputting the
                ## results to a file in the correct format
                exit()
            
            ## Testing statement
            #if(ultraword == "Puzzles42"):
            #    exit()
            
            ## Reset the word back to original
            ## word without digits appended to it
            newWord = words[i].capitalize()