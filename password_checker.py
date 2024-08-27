import re

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_character_criteria = re.search(r'[\W_]', password)

    # Check the number of criteria met
    criteria_met = sum([
        length_criteria,
        bool(uppercase_criteria),
        bool(lowercase_criteria),
        bool(number_criteria),
        bool(special_character_criteria)
    ])

    # Determine strength based on criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_character_criteria:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Main program
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("Your password is strong and meets all criteria!")
