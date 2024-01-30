# Project 1  - Analyzing Text Files
# CS 110
# Alark Joshi 

# Imports
import re # To use Regular Expressions
import sys # To access the input provided at the command line (command line parameters)

# Print the number of parameters / arguments provided by the user at the command line
print ("Number of arguments:", len(sys.argv), "arguments")

# Print the parameters printed at the command line
print ("Argument List:", str(sys.argv))

# The name of the text file is provided as the 2nd parameter and is accessed using index 1
# Index 0 contains the first element (name of the program)
# Index 1 contains the second element (name of the text file)
filename = sys.argv[1]

# Print the name of the text file to make sure that we're reading the correct text file
print(filename)

# Open the text file
file_handler = open(filename, "r") # The file is opened in READ mode using the "r" parameter

# Create empty lists
all_words = [] # This list will contain all the words in the text file
all_characters = [] # This list will contain all the characters in the text file

# Read the text file into the program one line at a time using a for loop
for one_line in file_handler:
    
    # Add all the characters in the file to the allcharacters list, one line at a time 
    all_characters.extend(one_line)

    # split the line with a regular expression on spaces
    # For example, "Hello, How are you?" is split into six strings: "Hello", ",", "How", "are", "you", "?"
    chunks = re.findall( r'\w+|[^\s\w]+', one_line)

    # If a line is empty, then do not add any words to the allwords list 
    if len(chunks) > 0:
        all_words.extend(chunks)

# This is to check that the contents of the file have been read into the all_characters and all_words lists
# For tiny_file.txt, len(all_characters) prints 20, len(all_words) prints 6
print(len(all_characters))
print(len(all_words))

# PART 1

# Initialize 3 variables to zero - one to count commas, one to count vowels, one to count consonants,

# Helper code: The following snippet of code prints each character in the file on a separate line

comma_counter = 0 #set variable to zero (Basically an accumlator)
vowel_counter = 0
cap_vowel = 0
consonants_counter = 0

for character in all_characters: #talking about every character within the text
    if character == ',': #if the character equals a comma
        comma_counter = comma_counter + 1 # add 1 to each comma counted for
    if character.isalpha(): #input validation to check if the character is apart of the alphabet
        if character == 'a' or character =='e' or character == 'i' or character=='o' or character =='u': #if the character equals to lowercase vowels
            vowel_counter = vowel_counter + 1 #add to vowel accumulator if the vowel is lowercase
        elif character == 'A' or character =='E' or character == 'I' or character=='O' or character =='U': #if the character equals to upper case
            cap_vowel = cap_vowel + 1 #add to vowel accumulator if the vowel is upper case
        else:
            consonants_counter = consonants_counter + 1 #if the chacter does't equal to a upper case or lower case vowel count it as a consonants; add to consonants accumulator

    vowel= cap_vowel + vowel_counter #adds the lower and upper case vowels together to get full count


print(f"There is {comma_counter} commas") #outputs how much commas there are in the text file
print(f"There is {vowel} vowels") #outputs how many vowels there are in the text file
print(f"There is {consonants_counter} constants") #outputs how many consonants there are in the text file


# Iterate over the all_characters list to count the number of commas, the number of vowels, and the number of consonants

# Print the number of commas, vowels, and consonants



# Part 2
# (a) Count the number of times a user-specified word (the search key) is found in the file and display the count
# (b) Extend this using a loop to allow the user to keep entering words until the enter "exit" as the search key to exit the program


search_for_words= str(input("Please enter the word you are searching for: ")) #ask the user for input, also known as key word

while search_for_words != "exit": #used a while loop to search for the key word, however the key word doesn't equal to "exit" overlooks that word.
    search_key= 0 #sets the variable to zero in order (Basically an accumlator)
    for word in all_words: #goes over all the words within the ext file
        if word.lower()== search_for_words.lower(): #returns the lowercased strings from the text by converting each uppercase letter to lowercase.
            search_key += 1 #the search key is equal to search key plus one: accounts for each time the word that is searched by user is within the text
    print (f"The search_key was found {search_key} times in the text file. ") #tells the user the amount of times the words search for is within the text
    search_for_words=str(input("Enter a new word to search or type exit to end: ")) #ask the user if they would like to search for another word or stop the program

