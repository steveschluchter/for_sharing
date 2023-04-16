#!//opt/anaconda3/bin/python

#



from copy import copy
import re, sys

print("Welcome to the wordle assistant.")

forbidden_letters = input("Enter a string of forbidden letters.")
forbidden_letters = list(forbidden_letters.upper())
forbidden_letters = list(dict.fromkeys(forbidden_letters))

must_have_letters = input("Enter a string of letters that your word must have.")
must_have_letters = list(must_have_letters.upper())
must_have_letters = list(dict.fromkeys(must_have_letters))

ordered_letters = input("Enter a string of letters that must appear in your word, in order.\
                         Enter a question mark '?' for an unknown character.\
                         If you enter something other than a combination of\
                             letters and question marks, you'll cause problems.\
                         So, don't enter any whitespaces either.")

for i, letter in enumerate(ordered_letters):

    print(i, "  ", letter)

    if letter in "abcdefghijklmnopqrstuvwxyz":

        ordered_letters[i] = letter.upper()

    elif letter == '?':

        ordered_letters[i] = '.'

    else:

        print("You have entered something other than a string of letters\
            and question marks.")
        print("End program.")

sys.exit(1)


words = open('corncob_caps.txt')

candidates = words.readlines()

results = []


for word in candidates:

    continue_flag = False

    for letter in forbidden_letters:

        if re.search(letter, word):
            print(f"{word} has an {letter}, which is forbidden.")
            continue_flag = True
            break

    if continue_flag:

        continue

    must_have_letters_copy = copy(must_have_letters)

    for letter in must_have_letters:

        if letter not in word:

            continue_flag = True
            
            break
    
    if continue_flag:

        continue

    #if not re.match()

    

    



print(type(candidates))


