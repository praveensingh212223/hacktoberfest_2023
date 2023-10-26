""" Python Program for Creating ASCII Art from User-specified text"""

# Importing the pyfiglet library, which is used to create ASCII art from text.
import pyfiglet

# Define a function that generates ASCII art from the given text.
def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art


if __name__ == "__main__":
    
    #Prompting the user for text.
    input_text = input("Enter the text to convert to ASCII art: ")
    ascii_art = generate_ascii_art(input_text) # Calling the function 
    print(ascii_art) # Printing the art
