import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score

def interpret_score(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

def evaluate_password(password):
    score = check_password_strength(password)
    strength = interpret_score(score)
    return score, strength

if __name__ == "__main__":
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        
        score, strength = evaluate_password(password)
        print(f"Password strength: {strength}")
        print(f"Score: {score}/5")
        print("------------------------------------------")
    
    print("Program finished.")