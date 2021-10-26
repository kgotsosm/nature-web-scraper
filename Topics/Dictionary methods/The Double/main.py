# put your python code here
from string import ascii_lowercase
values = list(ascii_lowercase)
double_alphabet = {}
for letter in values:
    
    double_alphabet[letter] = letter + letter
