"""
My Morse Code Attempt
"""
# Morse Code Dictionary
morse_dict = {
    'a': '•—',      'b': '—•••',    'c': '—•—•',    'd': '—••',     'e': '•',
    'f': '••—•',    'g': '——•',     'h': '••••',    'i': '••',      'j': '•——',
    'k': '—•—',     'l': '•—••',    'm': '——',      'n': '—•',      'o': '———',
    'p': '•——•',    'q': '——•—',    'r': '•—•',     's': '•••',     't': '—',
    'u': '••—',     'v': '•••—',    'w': '•——',     'x': '—••—',    'y': '—•——',
    'z': '——••',
    '1': '•————',   '2': '••———',   '3': '•••——',   '4': '••••—',   '5': '•••••',
    '6': '—••••',   '7': '——•••',   '8': '———••',   '9': '————•',   '0': '—————',
    ' ': '   ',
    '.': '•—•—•—',  ',': '——••——',  '?': '••——••',  '\'': '•————•', '!': '—•—•——',
    '/': '—••—•',   '@': '•——•—•',  '&': '•—•••',   ':': '———•••',  ';': '—•—•—•',
    '_': '••——•—',  '=': '—•••—',   '+': '•—•—•',   '-': '—••••—',  '"': '•—••—•',
    '(': '—•——•',   ')': '—•——•—'
}

# Reversed Morse Dictionary
reverse_morse_dict = {value: key for key, value in morse_dict.items()}

# Converts text to Morse Code
def text_to_morse(text):
    morse_code = ''
    for char in text.lower():
        morse_code += ' ' + morse_dict[char]
    return morse_code

# Converts Morse Code to text
def morse_to_text(morse):
    converted_text = ''

    # Split the line into words
    words = morse.split('     ')
    for word in words:
        # Split the word into character codes
        char_code = word.split(' ')
        for code in char_code:
            code.strip()
            # Check if code exists in reverse dict and converts
            if code in reverse_morse_dict:
                converted_text += reverse_morse_dict[code]
            else:
                converted_text += '^' # Unknown Chars
        converted_text += ' ' # Add a space after each word

    return converted_text.strip()

# Ask the user which to convert
while True:
    print("\n___--- Morse Code ---___\n1. Text to Morse\n2. Morse to text\n3. Exit\n" + '-' * 25)
    user_selection = input('Enter your choice:')
    if user_selection == '1':
        print(text_to_morse(input('\nEnter your text:')))
    elif user_selection == '2':
        print(morse_to_text(input('\nEnter your morse code:')))
    elif user_selection == '3':
        print('\nThank you for using Morse Code!')
        break
    else:
        print('\n!! >> Please enter a valid choice.\n')
        continue