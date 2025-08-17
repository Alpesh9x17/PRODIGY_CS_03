import re

def check_password_strength(password):
    """
    Checks the strength of a password and provides feedback.
    Returns a tuple: (strength, feedback)
    """
    length = len(password) >= 8
    lower = re.search(r'[a-z]', password) is not None
    upper = re.search(r'[A-Z]', password) is not None
    digit = re.search(r'\d', password) is not None
    special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length, lower, upper, digit, special])

    if score == 5:
        strength = "Strong"
        feedback = "Excellent! Your password is strong."
    elif score >= 3:
        strength = "Moderate"
        feedback = "Good, but consider using a longer password with uppercase, lowercase, numbers, and special symbols for more security."
    else:
        strength = "Weak"
        feedback = "Weak password. Use at least 8 characters, mix upper/lowercase, numbers, and special symbols."

    return strength, feedback


def main():
    print("=== Password Complexity Checker ===")
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Strength: {strength}\nFeedback: {feedback}")

if __name__ == "__main__":
    main()
