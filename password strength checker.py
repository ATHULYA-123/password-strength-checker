import re

def password_strength(password):
    # Initial strength score
    strength = 0
    
    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        print("Password should contain at least one digit.")
    
    # Check for uppercase characters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("Password should contain at least one uppercase letter.")
    
    # Check for lowercase characters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        print("Password should contain at least one lowercase letter.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print("Password should contain at least one special character.")
    
    # Password strength score
    return strength

def rate_password(password):
    score = password_strength(password)
    
    if score <= 2:
        return "Weak Password"
    elif score == 3:
        return "Medium Password"
    elif score >= 4:
        return "Strong Password"

def main():
    password = input("Enter your password: ")
    rating = rate_password(password)
    print(f"Your password strength is: {rating}")

if __name__ == "__main__":
    main()
