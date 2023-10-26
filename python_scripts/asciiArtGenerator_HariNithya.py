""" Creating ASCII Art from User-specified text"""
# Importing the pyfiglet library, which is used to create ASCII art from text.
# Define a function that generates ASCII art from the given text.
#Prompting the user for text.

import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    input_text = input("Enter the text to convert to ASCII art: ")
    ascii_art = generate_ascii_art(input_text)
    print(ascii_art)
