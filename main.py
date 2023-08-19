import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        password_length = int(input("Enter the password length: "))

        if password_length < 6:
            print("Password length must be at least 6 characters.")
        else:
            generated_password = generate_password(password_length)
            print("Generated password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid password length.")
