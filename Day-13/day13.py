import string
import random

def check_password_strength(password):
    length_score = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([length_score, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    test_password = "User@1234"
    strength = check_password_strength(test_password)
    
    print("=== Day 14: Password Utility ===")
    print(f"Tested Password : {test_password}")
    print(f"Password Strength: {strength}")

    new_password = generate_strong_password(16)
    print(f"Generated Random Password: {new_password}")
    print(f"New Password Strength   : {check_password_strength(new_password)}")