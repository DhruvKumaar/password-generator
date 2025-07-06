import random
import string

def generate_password(length, use_special, use_digits):
    if length < 4:
        return "Password length should be at least 4 for better security."

    characters = list(string.ascii_letters)
    required = []

    if use_special:
        characters += list(string.punctuation)
        required.append(random.choice(string.punctuation))

    if use_digits:
        characters += list(string.digits)
        required.append(random.choice(string.digits))

    required.append(random.choice(string.ascii_lowercase))
    required.append(random.choice(string.ascii_uppercase))

    if not characters:
        return "Error: No character sets selected."

    while len(required) < length:
        required.append(random.choice(characters))

    random.shuffle(required)
    return ''.join(required[:length])

def save_to_file(password, filename="password.txt"):
    with open(filename, 'w') as file:
        file.write(password)
    print(f"Password saved to {filename}")

def main():
    print("=== Strong Password Generator ===")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    save_option = input("Save password to file? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_special, use_digits)

    if "Error" in password or "should be at least" in password:
        print(password)
    else:
        print("\nGenerated Password:", password)
        if save_option:
            save_to_file(password)

if __name__ == "__main__":
    main()