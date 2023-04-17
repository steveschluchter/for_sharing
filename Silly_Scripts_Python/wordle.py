#!//opt/anaconda3/bin/python

#This program is designed to help the user with the game wordle.
#By: Steve Schluchter
#Date: 16.April.2023

from copy import copy
import re, sys

print("Welcome to the wordle assistant.")

word_length = int(input("Enter a length of desired word suggestions."))

forbidden_letters = input("Enter a string of forbidden letters.")
forbidden_letters = list(forbidden_letters.upper())
forbidden_letters = list(dict.fromkeys(forbidden_letters))

must_have_letters = input("Enter a string of letters that your word must have.")
must_have_letters = list(must_have_letters.upper())
must_have_letters = list(dict.fromkeys(must_have_letters))

ordered_letters = list(input(f"Enter a string of letters that must appear in your word, in order.\
Enter a question mark '?' for an unknown character.\
If you enter something other than a combination of\
letters and question marks, you'll cause problems.\
So, don't enter any whitespaces either.\
If you don't enter a string that is of length {word_length},\
you'll cause problems.").strip())

if len(ordered_letters) != word_length:
    print(f"You didn't enter a string of length {word_length}.") 

for i, letter in enumerate(ordered_letters):

    if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSDTUVWXYZ":

        ordered_letters[i] = letter.upper()

    elif letter == '?':

        ordered_letters[i] = '.'

    else:

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

print(candidates)

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

    #If the candidate word does not contain any must_have_letters, continue.
    for letter in must_have_letters:

        if letter not in word:

            continue_flag = True
            
            break
    
    if continue_flag:

        continue

    #If the word doesn't match the regular expression entered by the user, continue.
    if not re.search(f"{ordered_letters}", f"{word}"):
        continue

    results.append(word)


print("Here are your results.")
for result in results:
    print(result)

