import random
import string

def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity choice"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    length = int(input("Enter the desired password length: "))
    complexity = input("Enter the desired complexity level (1: Letters, 2: Letters + Digits, 3: Letters + Digits + Special Characters): ")

    password = generate_password(length, complexity)
    
    if password != "Invalid complexity choice":
        print("Generated Password:", password)
    else:
        print(password)

if __name__ == "__main__":
    main()
