#Problem 3: Unique Characters in a String
#DES:Create a function that determines whether all characters in a given string are unique.
#  If the string has all unique characters, return True; otherwise, return False.

##Thinking####
# if the string is unique, but hello doesn't work, this could mean characters cannot be repeated.

def unique():
    word = str(input(f"\nEnter a word: \n"))
    for l in word:#Using a for loop so the words' characters are iterated and checked over
        print(l)
    if word.count(l) == 1: #check to make sure each letter only appears once, prints out true
        print(True) 
    elif word.count(l) > 1: #condition, using count to check if the letters(l) in the user's word is repeated 
        print(False)
unique()

#any other word with the same letter repeated prints out false, except Hello. 