#Problem 1: Palindrome Checker
#DES: Create a program that checks whether a given string is a palindrome. 
# A palindrome is a word, phrase, number, or other sequence of characters that reads 
# the same forwards and backwards (ignoring spaces, punctuation, and capitalization).

##I will convert user input into a string, there's a possibility it will cause errors and overlook some edgecases 
##like empty strings.
word = input(f"Enter anything and see if it is a palindrome \n>")
reverse = word [::-1] ##This is a slice statement that will start at the end of the word and 
#subtract 1 to reverse each character in the word and return a reversed word. I will add the 'reverse' variable into 
#the conditional.

#if word == " ": #This line of code didn't work to check spaces and empty strings
if word.isspace():
    print(f"\nThis is not a valid input. Please try Again!\n")#Trying to count for empty spaces as edgecase, doesn't word
    #first try
    print("You've entered spaces, this is empty.")
else:
    print(reverse)#printing the reversed string

##Checking to see if the reversed string reads like original string

if reverse != word:
    print("This is not a palindrome")
elif reverse == word.isspace():
    print("This is not a palindrome")
elif reverse == word:
    print("This is a palindrome") #This conditional still doesn't work but the other condtionals of checking 
    #the reversed string do. MY program recognizes empty spaces and provides feedback to the user, but "This is 
    # a palindrome" still prints at the end of it. Most likely because empty strings are the same back and forth