"""
Created on Fri Mar 26 2021

"S'OZ TOPISH O'YINI"

@author: acer
"""

from random import choice
from uzwords import words

def get_word():
    """tasodifiy so'z tanlash"""
    word = choice(words)
    while ' ' in word or '-' in word:
        word = choice(words)
    return word.upper()
    
def display(u_letters, word):
    d_letters = ''
    for letter in word:
        if letter in u_letters.upper():
            d_letters += letter
        else:
            d_letters += '-'
    return d_letters

def play():
    word = get_word()
    u_letters = ''
    print(f"\nМен {len(word)} ҳарфли сўз ўйладим топа оласизми?\n{'-' * len(word)}")
    
    while True:
   
        if u_letters:
            print(f"{'*' * 40}\nШу пайтгача киритилган ҳарфлар : ", u_letters)
       
       
        letter = input("Ҳарф киритинг : ").upper()
        if not letter.isalpha():
            print("\nФақат ҳарф киритинг : ")
   
        elif len(letter) > 1:
            print("\nФақат битта ҳарф киритинг : ")
    
        else:
        
            if letter in u_letters:
                print(f"\nСиз {letter} ҳарфини олдин киритгансиз")
                print(display(u_letters, word))
    
            elif letter in word:
                print(f"\nТўғри топдингиз {letter} ҳарфи бор!")
                u_letters += letter
                print(display(u_letters, word))
            
            else:
                print(f"\nХато {letter} ҳарфи йўқ!")
                u_letters += letter
                print(display(u_letters, word))
        if display(u_letters, word) == word:
            print(f"\nТабриклайман сиз {word} сўзини {len(u_letters)} уринишда топдингиз!")
            break
        