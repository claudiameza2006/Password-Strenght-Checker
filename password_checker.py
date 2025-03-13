import re

# Function to check password strength
def check_password_strength(password):
    # Minimum length is 8 characters
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters."
    
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one digit
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    
    return "Password is strong!"

# Main entry point
def main():
    password = input("Enter your password to check strength: ")
    strength = check_password_strength(password)
    print(strength)

# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
