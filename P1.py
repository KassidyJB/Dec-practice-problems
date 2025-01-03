#Problem 1: Palindrome Checker
#DES: Create a program that checks whether a given string is a palindrome. 
# A palindrome is a word, phrase, number, or other sequence of characters that reads 
# the same forwards and backwards (ignoring spaces, punctuation, and capitalization).

##I will convert user input into a string, there's a possibility it will cause errors and overlook some edgecases 
##like empty strings.
word = str(input(f"\nEnter anything and we'll check if it is a palindrome \n>"))
reverse = word [::-1] ##This is a slice statement that will start at the end of the word and 
#subtract 1 to reverse each character in the word and return a reversed word. I will add the 'reverse' variable into 
#the conditional.

if word == " ":
    print(f"\nThis is not a valid input. Please try Again!\n")
else:
    print(reverse)