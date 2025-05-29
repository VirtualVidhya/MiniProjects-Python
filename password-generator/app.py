import string
import secrets
import sys

def get_yes_no(prompt):
    """Prompt the user with a yes/no question and return True for 'y', False for 'n'."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ('y', 'n'):
            return ans == 'y'
        print("Please enter 'y' or 'n'.")

def get_int(prompt, minimum=0):
    """Prompt the user for an integer ≥ minimum."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value >= minimum:
                return value
            print(f"Please enter an integer ≥ {minimum}.")
        except ValueError:
            print("Invalid input; please enter an integer.")

def generate_password(length, use_upper, use_lower, use_digits, use_specials,
                      min_digits, min_specials, avoid_ambiguous):
    # Define character pools
    uppercase = set(string.ascii_uppercase)
    lowercase = set(string.ascii_lowercase)
    digits    = set(string.digits)
    specials  = set("!@#$%^&*")

    ambiguous = {'O', '0', 'l', '1', 'I'}
    pools = []

    if use_upper:
        pools.append(list(uppercase))
    if use_lower:
        pools.append(list(lowercase))
    if use_digits:
        pools.append(list(digits))
    if use_specials:
        pools.append(list(specials))

    if not pools:
        raise ValueError("At least one character type must be enabled.")

    # Optionally remove ambiguous characters
    if avoid_ambiguous:
        pools = [[c for c in pool if c not in ambiguous] for pool in pools]

    # Flatten combined pool for filling the rest
    combined_pool = [c for pool in pools for c in pool]

    if len(combined_pool) == 0:
        raise ValueError("No characters available after removing ambiguous ones.")

    if min_digits + min_specials > length:
        raise ValueError("Sum of minimum digits and specials exceeds total length.")

    password_chars = []

    # Enforce minimum digits
    if use_digits and min_digits > 0:
        digit_pool = [c for c in digits if (not avoid_ambiguous or c not in ambiguous)]
        for _ in range(min_digits):
            password_chars.append(secrets.choice(digit_pool))

    # Enforce minimum special characters
    if use_specials and min_specials > 0:
        special_pool = [c for c in specials if (not avoid_ambiguous or c not in ambiguous)]
        for _ in range(min_specials):
            password_chars.append(secrets.choice(special_pool))

    # Fill the rest of the password
    remaining = length - len(password_chars)
    for _ in range(remaining):
        password_chars.append(secrets.choice(combined_pool))

    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

def main():
    print("# Password Generator #")
    length = get_int("Enter password length: ", minimum=1)
    use_upper  = get_yes_no("Include uppercase letters? (y/n): ")
    use_lower  = get_yes_no("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_specials = get_yes_no("Include special characters? (y/n): ")
    min_digits   = get_int("Minimum number of digits: ", minimum=0)
    min_specials = get_int("Minimum number of special characters: ", minimum=0)
    avoid_amb = get_yes_no("Avoid ambiguous characters? (y/n): ")

    try:
        pwd = generate_password(
            length,
            use_upper, use_lower, use_digits, use_specials,
            min_digits, min_specials,
            avoid_amb
        )
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print("\nGenerated password:", pwd)

if __name__ == "__main__":
    main()
