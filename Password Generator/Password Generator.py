import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user for the password length
    length = input("How long do you want your password to be? ")
    
    try:
        length = int(length)
        
        if length <= 0:
            print("Please enter a positive number for the length.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print("Your generated password is:", password)
    
    except ValueError:
        print("Oops! That doesn't look like a number. Please try again.")

if __name__ == "__main__":
    main()
