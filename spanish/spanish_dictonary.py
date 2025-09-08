from json import *
with open('spanish/dictonary', "r") as f:
    data = load(f)
choice  = input('Do you want to create a new entry or do you want to search for a word?\n').lower()
if 'create' in choice:
    spanish_word = input('What word do you want to create an entry for? (in spanish)\n')