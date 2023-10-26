import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    input_text = input("Enter the text to convert to ASCII art: ")
    ascii_art = generate_ascii_art(input_text)
    print(ascii_art)
