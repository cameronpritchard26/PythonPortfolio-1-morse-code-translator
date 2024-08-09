# Description: This program allows a user to translate text from plain text to Morse code and vice versa.

# Defining the morse code dictionary
MORSE_CODE_TABLE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': '/'
}

# Loop break indicator
BREAK_INDICATOR = 'exit program'

# Defining the translation function
def translate(message):
    # If the message is in plain text
    if message.isalpha():
        # Converting the message to uppercase
        message = message.upper()
        # Creating an empty string to store the translated message
        translated_message = ''
        # Looping through the message
        translated_message = ' '.join(MORSE_CODE_TABLE[letter] for letter in message)
    # If the message is in Morse code
    else:
        # Creating an empty string to store the translated message
        translated_message = ''
        # Splitting the message by spaces
        message = message.split(' ')
        # Looping through the message
        for segment in message:
            # Looping through the dictionary
            for letter, morse_code in MORSE_CODE_TABLE.items():
                # If the morse code matches
                if segment == morse_code:
                    # Adding the letter to the translated message
                    translated_message += letter
    # Returning the translated message
    return translated_message.capitalize()

while True:
    # Getting the user's input
    message = input('Enter a message to translate to Morse code or vice versa: ')
    # Checking if the user wants to exit the program
    if message.lower() == BREAK_INDICATOR:
        break
    # Translating the message
    translated_message = translate(message)
    # Printing the translated message
    print(translated_message)