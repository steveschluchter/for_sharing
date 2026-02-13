#!/opt/anaconda3/bin/python

#This program looks for words that use the user's letters, and no other letters.
#Author: Steve Schluchter
#Date begun: 15.April.2023

import re


words = open('corncob_caps.txt')
candidates = words.readlines()
results = []

user_letters = list(input("Enter your list of included letters. ").upper())
needed_letters = list(input("Enter the necessary letter(s)").upper())

for word in candidates:

    word = word.strip()

    test_word = word

    missing_needed_letter = False

    for letter in needed_letters:
        if letter not in test_word:
            #print("Your word list has no words that contain all of your necessary letters.")
            missing_needed_letter = True
            break
    
    if missing_needed_letter:
        continue

    for letter in user_letters:

        #Here we scrape out all if the requisite letters.
        #If any letters remain, then the word contains extra letters.

        test_word = re.sub(letter, '', test_word)

    if not test_word:

        results.append(word)


results = sorted(results, key=len)

if not results:

    print("You have no words using your letters and only your letters.")

else:

    print("Here is your list of words using your letters and only your letters.")

    for result in results:

        print(f"{result} has length {len(result)} and \
{str(len(dict.fromkeys(list(result))))} distinct letters.")