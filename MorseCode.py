"""Bidirectional text and Morse-code conversion utilities."""

MORSE_CODE = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "'": ".----.", "!": "-.-.--", "/": "-..-.", "@": ".--.-.",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "_": "..--.-",
    "=": "-...-", "+": ".-.-.", "-": "-....-", '"': ".-..-.",
    "(": "-.--.", ")": "-.--.-",
}
REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}


def text_to_morse(text: str) -> str:
    """Convert text to Morse, using / between words."""
    words = []
    for word in text.lower().split(" "):
        codes = []
        for character in word:
            if character not in MORSE_CODE:
                raise ValueError(f"Unsupported character: {character!r}")
            codes.append(MORSE_CODE[character])
        words.append(" ".join(codes))
    return " / ".join(words)


def morse_to_text(morse: str) -> str:
    """Convert Morse code to lowercase text; unknown codes become ^."""
    words = []
    for word in morse.strip().split("/"):
        characters = []
        for code in word.strip().split():
            characters.append(REVERSE_MORSE_CODE.get(code, "^"))
        words.append("".join(characters))
    return " ".join(words).strip()


def main() -> None:
    while True:
        print("\n___--- Morse Code ---___\n1. Text to Morse\n2. Morse to text\n3. Exit\n" + "-" * 25)
        selection = input("Enter your choice: ")
        if selection == "1":
            try:
                print(text_to_morse(input("\nEnter your text: ")))
            except ValueError as error:
                print(f"\n!! >> {error}")
        elif selection == "2":
            print(morse_to_text(input("\nEnter your morse code: ")))
        elif selection == "3":
            print("\nThank you for using Morse Code!")
            return
        else:
            print("\n!! >> Please enter a valid choice.\n")


if __name__ == "__main__":
    main()
