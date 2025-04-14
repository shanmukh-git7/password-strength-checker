import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 12 characters")

    # Uppercase, lowercase
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Add numbers")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Add special characters")

    # Final rating
    if strength >= 6:
        rating = "Strong"
    elif strength >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, suggestions

# Main loop
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    rating, tips = check_password_strength(pwd)

    print(f"\nPassword strength: {rating}")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(f" - {tip}")
