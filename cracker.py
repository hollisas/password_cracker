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
##  4) Any word that is made with digits up to
##     100 digits length
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
m = hashlib.sha256()
print(m.update(b'Puzzles42'))
## Prints out 7e11ed17256ef7ee697ece97d8edc25c558108aa18583de639c96ba2769bd0c3
## At first glance this is the exact hash in the example on the homework PDF for Puzzles42
print(m.hexdigest())