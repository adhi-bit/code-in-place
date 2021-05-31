'''
CODE IN PLACE 2021 Final projects
AUTOMATIC PASSWORD GENERATOR -BY KALIVARADHARAJAN g
'''

import random   # importing random library
import string

adjectives = ['frisky' , 'metal','zombie','geeky','fluffy','black','red']  # creating list  of adjective
nouns=['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda'] # creating list of nouns

def main():
    print('Welcome to Password generator')
    while True:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        password = adjective + noun + str(number) + special_char
        print('Your new auto generated password is : '+password ,file=open("auto.txt","a")) # saving password directly on the txt file for future purpose
        response = input('Would you like to regenerate password ? enter any key:')
        if response == "n":
            break





if __name__ == '__main__':
    main()
