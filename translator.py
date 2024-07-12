MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def encode_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_code)

def decode_morse(code):
    inv_morse_code = {v: k for k, v in MORSE_CODE_DICT.items()}
    morse_words = code.split(' ')
    text = ''
    for morse_word in morse_words:
        if morse_word in inv_morse_code:
            text += inv_morse_code[morse_word]
        else:
            text += ' '
    return text

def main():
    print("1. Encode to Morse code")
    print("2. Decode from Morse code")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        text = input("Enter text to encode: ")
        encoded_text = encode_morse(text)
        print(f"Morse code: {encoded_text}")
    elif choice == '2':
        code = input("Enter Morse code to decode (separate codes with spaces): ")
        decoded_text = decode_morse(code)
        print(f"Decoded text: {decoded_text}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
