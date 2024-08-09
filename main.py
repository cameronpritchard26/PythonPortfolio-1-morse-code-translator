# Description: This program allows a user to translate text from plain text to Morse code and vice versa.

from tkinter import *

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

# Defining the translation function
def translate():
    # Determine if the user wants to translate from text to Morse code or vice versa
    if text_input.get():
        text = text_input.get().upper()
        morse = ''
        for char in text:
            if char in MORSE_CODE_TABLE:
                morse += MORSE_CODE_TABLE[char] + ' '
        morse_input.delete(0, END)
        morse_input.insert(0, morse)
    elif morse_input.get():
        morse = morse_input.get().split(' ')
        text = ''
        for code in morse:
            for char, value in MORSE_CODE_TABLE.items():
                if code == value:
                    text += char
        text_input.delete(0, END)
        text_input.insert(0, text)
    else:
        text_input.delete(0, END)
        morse_input.delete(0, END)

window = Tk()
window.title('Morse Code Translator')
window.geometry('500x300')

main_label = Label(window, text='Morse Code Translator', font=('Arial', 24))
main_label.grid(row=0, column=1)

text_label = Label(window, text='Enter a message to translate:', font=('Arial', 16))
text_label.grid(row=1, column=0)
text_input = Entry(window, font=('Arial', 16))
text_input.grid(row=1, column=1)
translate_button_1 = Button(window, text='Translate', font=('Arial', 16), command=translate)
translate_button_1.grid(row=1, column=2)

morse_label = Label(window, text='Enter a message to translate:', font=('Arial', 16))
morse_label.grid(row=2, column=0)
morse_input = Entry(window, font=('Arial', 16))
morse_input.grid(row=2, column=1)
translate_button_2 = Button(window, text='Translate', font=('Arial', 16), command=translate)
translate_button_2.grid(row=2, column=2)

window.mainloop()