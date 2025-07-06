#  Project 7: Password Generator Tool

## Overview

This is a simple Python-based program that generates strong and secure passwords. The user can customize the password length, choose to include digits and special characters, and optionally save the generated password to a file.

## Features

- Allows user to choose password length.
- Option to include special characters (e.g., @, #, !).
- Option to include digits (0–9).
- Automatically ensures at least one uppercase and one lowercase letter.
- Randomly shuffles characters to increase security.
- Option to save the generated password to a text file (`password.txt`).

## Requirements

- **Python 3.x**
- No external libraries required (uses only built-in modules: `random`, `string`)

## How to Use

1. Run the script in a Python environment (Python 3.x recommended).
2. Enter the desired password length when prompted.
3. Choose whether to include special characters (`y/n`).
4. Choose whether to include digits (`y/n`).
5. Choose whether to save the password to a file (`y/n`).
6. The generated password will be displayed on the screen.
7. If saved, the password will be written to `password.txt` in the same directory.

## File

- `password_generator.py` — Main script to generate and save passwords.

## Notes

- Passwords shorter than 4 characters are discouraged for security reasons.
- The program always includes at least one lowercase and one uppercase letter.
- Shuffling ensures that required characters (like digits or special symbols) are randomly placed in the password.
- You can modify the filename parameter in the `save_to_file()` function to change the output file name or path.
