#!/usr/bin/python3


#This program translates text to a string of 0s and 1s that look like Morse code.

#Author: Steve Schluchter

#Begun: 28.Feb.2023

#Notes:  Characters from the input text that can't be uppercased and are not 
#        present in the MORSE_ALPHABET will be removed or ignored by the 
#        translation program.
#        
#        Execute this program by running the command 
#            python morse_code_translator.py <filename.txt>


#import statements
from sys import argv
import string
import re


#global constants
DIT = '-'
DAH = '---'
CHARACTER_GAP = '0'
LETTER_GAP  = '000'
WORD_GAP = '0000000'
REGEX_PUNCTUATION = f"[{string.punctuation}]"

MORSE_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                  'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 

MORSE_CODE = {
        'A': [DIT],
        'B': [DAH, DIT],
        'C': [DAH, DIT, DIT],
        'D': [DIT],
        'E': [DIT],
        'F': [DIT, DIT, DAH, DIT],
        'G': [DAH, DAH, DIT],
        'H': [DIT, DIT, DIT, DIT],
        'I': [DIT, DIT],
        'J': [DIT, DAH, DAH, DAH],
        'K': [DAH, DIT, DAH],
        'L': [DIT, DAH, DIT, DIT],
        'M': [DAH, DAH],
        'N': [DAH, DIT],
        'O': [DAH, DAH, DAH],
        'P': [DIT, DAH, DAH, DIT],
        'Q': [DAH, DAH, DIT, DAH],
        'R': [DIT, DAH, DIT],
        'S': [DIT, DIT, DIT],
        'T': [DAH],
        'U': [DIT, DIT, DAH],
        'V': [DIT, DIT, DIT, DAH],
        'W': [DIT, DAH, DAH],
        'X': [DAH, DIT, DIT, DAH],
        'Y': [DAH, DIT, DAH, DAH],
        'Z': [DAH, DAH, DIT, DIT],
        '1': [DIT, DAH, DAH, DAH, DAH],
        '2': [DIT, DIT, DAH, DAH, DAH],
        '3': [DIT, DIT, DIT, DAH, DAH],
        '4': [DIT, DIT, DIT, DIT, DAH],
        '5': [DIT, DIT, DIT, DIT, DIT],
        '6': [DAH, DIT, DIT, DIT, DIT],
        '7': [DAH, DAH, DIT, DIT, DIT],
        '8': [DAH, DAH, DAH, DIT, DIT],
        '9': [DAH, DAH, DAH, DAH, DIT],
        '0': [DAH, DAH, DAH, DAH, DAH]
        }

#begin functions

#translates a letter to morse code
def translate_letter(letter):
   
    returnLetter = ""

    for beep in MORSE_CODE[letter][0:-1]:

        returnLetter += beep
        returnLetter += CHARACTER_GAP

    returnLetter += MORSE_CODE[letter][-1]

    return returnLetter


#translates a word to morse code
def translate_word(word):

    returnString = ""


    for letter in word[0:-1]:
            
            if letter in MORSE_ALPHABET:

                returnString += translate_letter(letter)
                returnString += LETTER_GAP

    if word[-1] in MORSE_ALPHABET:
        
        returnString += translate_letter(word[-1])

    return returnString

#begin main script
if __name__ == "__main__":
    try:

        input_file = argv[1]

    except Exception as e:
    
        print("You didn't enter a file or the file you entered wasn't found")
        exit(1)

    morseText = ""


    with open(input_file, 'r') as f:
    
        #clean up text input for translation to morse code
        text = f.read().upper()
        text = re.sub(REGEX_PUNCTUATION, '', text)
        text = re.sub("\s+", ' ', text)
        text = text.strip()
        text = text.split(' ')
     

        #translate the text into Morse code

        for word in text[0:-1]:
    
            morseText += translate_word(word)
            morseText += WORD_GAP


        morseText += translate_word(word[-1])




print("""
      This is the text after it was preprocessed and prepared for
      translation into Morse code.  Characters not present in the
      Morse code's alphabet were either removed or were ignored 
      by the translator.
      """)

print(text)

print("""
      This is the text after it was translated into Morse code.
      """)

print(morseText)
