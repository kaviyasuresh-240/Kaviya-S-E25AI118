import re

def password_strength(password):
    score = 0

    # length check
    if len(password) >= 8:
        score += 2
        print("Length is okay")
    else:
        print("Password too short")

    # uppercase check
    if re.search(r'[A-Z]', password):
        score += 2
        print("Has uppercase letters")
    else:
        print("No uppercase letters")

    # lowercase check
    if re.search(r'[a-z]', password):
        score += 2
        print("Has lowercase letters")
    else:
        print("No lowercase letters")

    # number check
    if re.search(r'\d', password):
        score += 2
        print("Has numbers")
    else:
        print("No numbers")

    # special character check
    if re.search(r'\W', password):
        score += 2
        print("Has special characters")
    else:
        print("No special characters")

    # final result
    print("Total Score:", score)
    if score >= 10:
        print("Password is Strong")
    elif score >= 7:
        print("Password is Moderate")
    else:
        print("Password is Weak")

# input from user
pwd = input("Enter password: ").strip()
password_strength(pwd)
