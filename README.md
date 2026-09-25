# Morse Code Converter - Interactive CLI Utility

A lightweight Python application for bidirectional conversion between alphanumeric text and Morse code. This project features programmatic dictionary inversion, string tokenization, dynamic error handling for unsupported characters, and an interactive command-line interface.

## Features

* Bidirectional Translation: Converts plain text into Morse code and decodes Morse code sequences back to standard text.

* Automated Dictionary Inversion: Dynamically constructs the reverse lookup map at runtime using Python dictionary comprehension for $O(1)$ decoding operations.

* Interactive CLI Menu: Continuous user-prompt loop allowing seamless switching between encoding, decoding, and program exit.

* Error Handling & Formatting: Features fallback character handling (`^`) for unknown inputs, automatic case normalization, and word/character delimiter tokenization.

## Code Architecture

* `morse_dict`: Primary hash map storing key-value pairs for characters, numbers, and special symbols to Morse representations.

* `reverse_morse_dict`: Dynamically generated inverse hash map mapping Morse patterns back to standard characters.

* `text_to_morse()`: Iterates through normalized string characters and builds formatted Morse output sequences.

* `morse_to_text()`: Tokenizes input Morse code by word and character spaces, retrieving decoded values via reverse lookup.

## Project Structure

* `MorseCode.py`: Complete module containing data structures, translation logic, and the interactive terminal menu interface.

## Tech Stack

* Language: Python 3

* Concepts: Hash Maps / Dictionaries, String Tokenization & Parsing, Algorithm Design, Interactive CLI
