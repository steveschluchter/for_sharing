#!//opt/anaconda3/bin/python

#This program is designed to help the user with the game wordle.
#By: Steve Schluchter
#Date begun: I forgot. :(

from copy import copy
import re, sys

def word_score(input_word):

    input_word = dict.fromkeys(list(input_word))
        
    score = 0

    letter_frequency_array = ['E','T','A','O','I','N','S',\
                              'R','H','D','L','U','C','M',\
                              'F','Y','W','G','P','B','V',\
                              'K','X','Q', 'J', 'Z']

    input_word_list = list(input_word)

    for letter in input_word_list:
        
        score += 25 - letter_frequency_array.index(letter)

    return score

def where_are_the_letters(input_string):
    """
    returns a list of zero-indexed integer indices
    of letters in the input_string
    """
    input_string = input_string.lower()
    return_this = []
    for tup0, tup1 in enumerate(input_string):
        #print(tup0)
        #print(tup1)
        if tup1.isalpha():
            #print("ding ding ding")
            return_this.append(tup0)
    #print(return_this)
    return return_this

def get_letter_integer_pairs(input_string):
    """
    returns a list of tuples of letters and integers in which the
    letters are found in the input string
    """
    
    letter_indices = where_are_the_letters(input_string)
    #use the letter indices to start slicing the strings ...
     
    print("1 "+input_string)
    
    return_this = []
    #string_popper = input_string.lower().split()
    string_popper = input_string
    

    while string_popper:
        x = re.search(r"\b[A-Z]\d+",string_popper)
        if not x:
            print('validation problem!')
            break

        string_popper = re.sub(r"\b[A-Z]\d+","",string_popper)
        str = x.group()
        
        #print(x.group())
        
        
        print(string_popper)
        
        return_this.append((str[0],int(str[1:])))
       
        #tup0 = string_popper.pop()
        #tup1 = # regex out the first number in the string and stash it
        #return_this.append((tup0, tup1))
        #string_popper.pop()

    #print("Return this!") 
    #print(return_this)
    return return_this

                   


#where_are_the_letters('a1p2p3l4e5')
#get_letter_integer_pairs('a1p2p3l4e5')

#sys.exit(1)

print("Welcome to the wordle assistant.")

word_length = int(input("Enter a length of desired word suggestions."))

forbidden_letters = input("Enter a string of forbidden letters.")
forbidden_letters = list(forbidden_letters.upper())
forbidden_letters = list(dict.fromkeys(forbidden_letters))

must_have_these = input("""Enter a string of pairs of included letters and indices within the string that the letters cannot appear.\n
For example: a1p2p3l4e5 means that:\\n
the letter a appears, but not in the first position;\\n
the letter p appears, but not in the second position;\\n
the letter l appears, but not in the 4th position;\\n
the letter e appears, but not in the 5th position.\\n
If you have nothing to enter here, enter a blank space.""")

print(must_have_these)


must_have_these = get_letter_integer_pairs(must_have_these.strip().upper())

print(must_have_these)

#must_have_letters = list(dict.fromkeys(must_have_letters))

ordered_letters = list(input(f"Enter a string of letters that must appear in your word, in order.\
Enter a question mark '?' for an unknown character.\
If you enter something other than a combination of\
letters and question marks, you'll cause problems.\
So, don't enter any whitespaces either.\
If you don't enter a string that is of length {word_length},\
you'll cause problems.").strip().upper())

print(ordered_letters)
x = input("2")

if len(ordered_letters) != word_length:
    print(f"You didn't enter a string of length {word_length}.") 

for i, letter in enumerate(ordered_letters):

    if letter == '?':

        ordered_letters[i] = '.'

    elif letter not in "ABCDEFGHIJKLMNOPQRSDTUVWXYZ":
        
        print("You have entered something other than a string of letters\
              and question marks.")
        print("End program.")
        sys.exit(1)



ordered_letters = ''.join(ordered_letters)

words = open('corncob_caps.txt')

candidates = words.readlines()

candidates = [candidate.strip() for candidate in candidates]

#This is a constraint specific to wordle.  The word lengths are all 5.
candidates = [candidate for candidate in candidates if len(candidate) == word_length]

results = []


for word in candidates:

    continue_flag = False


    #If the candidate word contains any forbidden_letters, continue.
    for letter in forbidden_letters:

        if re.search(letter, word):
            continue_flag = True
            break

    if continue_flag:

        continue

    print("2 " + str(must_have_these))

    #If the candidate word does not contain any must_have_letters, continue.
    for letter in must_have_these:

        print(letter)

        if letter[0] not in word:

            continue_flag = True
            
            break

        if letter[1] == word[letter[1] - 1]:

            continue_flag = True

            break






    #for pair in  

    if continue_flag:

        continue

    #If the word doesn't match the regular expression entered by the user, continue.
    if not re.search(f"{ordered_letters}", f"{word}"):
        continue


    


    results.append(word)


results.sort(key=word_score)

print("Here are your results.")

for result in results:
    print(result)

